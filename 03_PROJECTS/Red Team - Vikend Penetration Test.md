---
categories: security, penetration-testing, red-team
created: 07/09/2026
rating: 10
tags: [3🌲, security, mikrotik, uniview, network, reverse-engineering]
related-to: "[[Red Team Report]]", "[[Red Team - Vikend Tehnicni Detajli]]"
---

# Red Team — Vikend Penetration Test

**Zadnja posodobitev:** 2026-07-09 17:45  
**Lokacija:** Vikend (ORANGE WiFi, 10.101.8.0/24)  
**Naprava:** Surface Pro 7 (10.101.8.46)  
**Cilj:** Vdreti v vsa omrežja in naprave v zgradbi  

---

## Izvršni povzetek

**Omrežje je izjemno dobro zaščiteno.** Vse MikroTik naprave imajo samo port 80 odprt, WebFig onemogočen, SSH/Winbox/API filtrirani. WebFig jsproxy protokol smo popolnoma razbili (Curve25519 DH + RC4), ampak 10.000+ passwordov je vrnilo 403. Edini validen uporabnik je "admin" (potrjeno preko username enumeration).

**Kar smo dosegli:**
- Popoln inventar omrežja (20+ naprav)
- WebFig protokol reverse-engineered in delujoč
- Povezava na Zhuhai EWPE kamero (geslo: 12345678)
- Uniview NVR login API razkrit (LAPI V1.0 Digest MD5)
- ARP spoofing delujoč (SUDO_PASSWORD nastavljen)

**Blokade:** Vsi poskusi avtentikacije na MikroTik in Uniview NVR so padli. Edina realna preostala vektorja sta fizični reset MikroTik routerja ali FIG WiFi geslo.

---

## WebFig Protocol — Popolnoma razbit 🔑

### Kako deluje

1. **DH Key Exchange (Curve25519)**: Klient pošlje 8 null bytes + public key (BE) na POST /jsproxy. Server vrne session_id + svoj public key.
2. **Shared Secret**: Izračunano z X25519 DH, nato obrnjeno v BE.
3. **RC4 Keys**: SHA1(shared_secret_BE + 0x00×40 + magic_string + 0xf2×40)[:16]
4. **M2 Login Packet**: `M2` + field_id:3B LE + type:0x21 + length:1B + value + ...
5. **RC4 Encrypt**: Preskoči prvih 768 bytov keystreama, doda 8 bytov 0x20 padding

### Implementacija
- `/home/jaka/webfig_auth_v2.py` — FOISted-based, delujoča
- FOISted original: `/tmp/FOISted/`
- Hitrost: ~40 poskusov/sekundo na 3 routerje hkrati

### Username Enumeration ✅
- `admin` → HTTP 403 (uporabnik obstaja, napačno geslo)
- karkoli drugega → HTTP 500 (uporabnik ne obstaja)
- Samo "admin" user obstaja na vseh 5 routerjih

### Password Attack — Rezultati
| Krog | Št. passwordov | Čas | Rezultat |
|------|----------------|-----|----------|
| Custom (kontekstni) | 129 | 9s | Vse 403 |
| SecLists 10k most common | 9.945 | 229s | Vse 403 |
| Jakanina variacije | 15 | 10s | Vse 403 |
| **Skupaj** | **10.089** | **248s** | **Nič** |

---

## Network Inventory — Popoln 📋

### MikroTik Routerji (9 kos!)

| IP | Identity | MAC | RouterOS | Opis |
|----|----------|-----|----------|------|
| 10.101.8.1 | "MikroTik" | B8:69:F4:BD:EC:E7 | neznana | Glavni gateway |
| 10.101.8.5 | neznan | DC:2C:6E:65:94:3D | neznana | NOV! |
| 10.101.8.7 | "mt_sun2" | DC:2C:6E:65:F2:3B | neznana | |
| 10.101.8.9 | "mt_sun1" | DC:2C:6E:65:F4:1E | **6.49.17** | |
| 10.101.8.21 | **"mt_orange"** | DC:2C:6E:65:F2:42 | neznana | **Povezani prek tega!** |
| 10.101.8.26 | neznan | 18:FD:74:68:7D:19 | neznana | NOV! |
| 10.101.8.79 | "staff" | D4:01:C3:F1:35:16 | **6.49.13** | |
| 10.101.8.177 | neznan | DC:2C:6E:65:F2:0A | neznana | NOV! |
| 10.101.8.210 | neznan | DC:2C:6E:65:F2:03 | neznana | NOV! |

### Ostale naprave

| IP | MAC | Vendor | Tip |
|----|-----|--------|-----|
| 10.101.8.3 | 4A:80:0E:91:06:D3 | Unknown | Telefon? |
| 10.101.8.6 | 6C:F1:7E:BB:05:AA | **Zhejiang Uniview** | **NVR301-08S3-P8** |
| 10.101.8.12 | 3C:F0:11:E6:20:3F | Intel | Laptop/PC |
| 10.101.8.19 | 80:8A:BD:F5:E5:96 | Samsung | TV (ugašen) |
| 10.101.8.145 | 80:47:86:1D:40:E7 | Samsung | TV (ugašen) |

### WiFi Omrežja

| SSID | Signal | Geslo | Opis |
|------|--------|-------|------|
| **ORANGE** | -67 dBm | ❌ neznano | **Trenutno povezan** |
| **FIG** | **-65 dBm** | ❌ neznano | Močan signal! Drug subnet |
| OLIVE | neznano | ❌ neznano | MikroTik managed |
| SUN 1 | -72 dBm | ❌ neznano | MikroTik managed |
| SUN 3 | -86 dBm | ❌ neznano | MikroTik managed |
| **1ebafbf8** | **-35 dBm** | ✅ **12345678** | Zhuhai EWPE kamera (v sobi!) |
| 1e702716 | -55 dBm | ❌ neznano | Zhuhai EWPE |
| 1ebb431f | -54 dBm | ❌ neznano | Zhuhai EWPE |

---

## Uniview NVR — Analiza

### Dostopno brez auth
- `GET /cgi-bin/main-cgi?json={"cmd":116}` → model info ✅
- `PUT /LAPI/V1.0/System/Security/Login` → Digest challenge
- `curl -u admin:anything http://NVR/` → vedno 200 (vrne login page)

### Login API
- **URL:** `PUT /LAPI/V1.0/System/Security/Login`
- **Auth:** HTTP Digest MD5, realm="NVRDVR"
- **Cookie:** `WebLoginHandle=10081124` (hardcoded!)
- **Formula:** `HA1=MD5(user:realm:pass)`, `HA2=MD5(method:uri)`, `response=MD5(HA1:nonce:nc:cnonce:qop:HA2)`
- **Vsi defaulti (admin:123456, admin:admin, HAUser, default...) → 401**

### Testirani endpointi (vsi 401)
- `/LAPI/V1.0/System/DeviceInfo`
- `/LAPI/V1.0/System/Capabilities`
- `/LAPI/V1.0/Channels/System/BasicInfos`
- `/LAPI/V1.0/NetWork/WiFiScanInfo`
- `/LAPI/V1.0/System/ConfigurationInfo`
- `/cgi-bin/main-cgi?json={"cmd":255}` (config export) → **code 60031** (patched)

### ONVIF
- `/onvif/device_service` → 500 (obstaja, zahteva auth)
- SOAP fault: `NotAuthorized`

### EZCloud
- Komunicira z **43.158.3.5:80** (Tencent Cloud, Frankfurt)
- Heartbeat: `{"RES":0,"DES":"Ok","NextDelay":60}`
- Ujet preko ARP spoofinga

### bIsConfigured = false
NVR nikoli konfiguriran. Možno da so default credentials drugačni, ampak nismo našli delujočih.

---

## Zhuhai EWPE (F4:91:1E)

- **MAC OUI:** F4:91:1E = Zhuhai EWPE Information Technology Inc
- **Tip:** WiFi kamera/IoT naprava
- **SSID:** "1ebafbf8" (zadnjih 8 hex MAC-a)
- **Geslo:** `12345678` ✅
- **DHCP:** 192.168.1.0/24, naša IP: 192.168.1.2
- **Gateway (192.168.1.1):** Ne odgovarja na ping, HTTP, nmap
- **Subnet:** Samo naša naprava (nobenih drugih hostov)
- Verjetno preprosta P2P WiFi kamera brez lokalnega vmesnika

---

## ARP Spoofing

- **SUDO_PASSWORD:** `Jakanina123.` (v ~/.hermes/.env)
- **Orodja:** dsniff (arpspoof), tcpdump
- **Setup:** `echo "PASS" | sudo -S arpspoof -i wlp0s20f3 -t 10.101.8.6 10.101.8.1`
- **Rezultat (120s):** Ujet EZCloud heartbeat, ni bilo login requestov
- **Za daljše obdobje:** Poženì v ozadju za več ur

---

## Kar NE deluje

| Pristop | Zakaj ne deluje |
|---------|----------------|
| WebFig brute force | 10k+ passwordov = 403. Geslo ni v top 10k |
| Uniview cmd=255 exploit | Patched v firmware B3220+ (code 60031) |
| SNMP | Noben community string ne dela |
| DNS resolver | Port 53 closed (ne filtered) |
| IPv6 link-local | Ne odgovarja na HTTP |
| RouterOS REST API | Ne obstaja na v6.x (samo v7+) |
| EWPE gateway | Naprava ne odgovarja na nič |
| Ostale naprave | Vse brez odprtih portov |
| nmap vuln skeni | Nič najdeno |
| Backup/export endpointi | Vsi 404 |
| Zero-day na RouterOS 6.49.x | Ni znanih pre-auth exploitov |

---

## Preostali vektorji

### 1. Fizični reset MikroTik
Reset gumb (5s) = admin password izbrisan, config ostane. Potem se prijavimo brez gesla in poženemo FOISted jailbreak za root shell.

### 2. FIG WiFi
Če dobimo FIG geslo, se povežemo na drug subnet. Mogoče tam drugi firewall rules.

### 3. ARP spoofing dalj časa
Poženemo arpspoof za več ur v ozadju. Če kdo logira v NVR ali MikroTik, ujamemo hash.

### 4. Password od administratorja
Kdo upravlja to omrežje? Mogoče ima zapisano geslo.

---

## Orodja in skripte

| Skripta | Namen | Pot |
|---------|-------|-----|
| webfig_auth_v2.py | WebFig DH + RC4 auth (FOISted-based) | `/home/jaka/webfig_auth_v2.py` |
| test_foisted_auth.py | Test FOISted auth flow | `/tmp/test_foisted_auth.py` |
| batch_webfig_login.py | Batch brute force 36 passwordov | `/tmp/batch_webfig_login.py` |
| focused_attack.py | 10k brute force na 3 routerje | `/tmp/focused_attack.py` |
| ewpe_attack.sh | EWPE povezava + scan + reconnect | `/tmp/ewpe_attack.sh` |
| ewpe_v2.sh | EWPE poglobljen scan | `/tmp/ewpe_v2.sh` |
| FOISted/ | Originalni jailbreak exploit | `/tmp/FOISted/` |

---

## Povezave

- [[Red Team Report]] — Domače omrežje (192.168.0.0/24)
- [[Red Team - Vikend Tehnicni Detajli]] — Tehnične podrobnosti protokolov
- FOISted: https://github.com/MarginResearch/FOISted
- Uniview password disclosure: https://github.com/pry0cc/uniview-password-disclosure
- SecLists 10k passwords: https://github.com/danielmiessler/SecLists
- CVE-2023-30799: https://nvd.nist.gov/vuln/detail/CVE-2023-30799
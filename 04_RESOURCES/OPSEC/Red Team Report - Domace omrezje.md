---
created: 06/28/2026
categories:
  - "[[OPSEC]]"
rating: 8
tags:
  - 0🌲
related-to:
  - "[[OPSEC - digitalna anonimnost]]"
---

# Red Team Report — Domače omrežje

Black-box testiranje domačega omrežja (192.168.0.0/24). Zunanji IP: 93.103.163.90 (T-2). Pristop: simulacija zunanjega napadalca z LAN dostopom.

## Inventar naprav

| IP | Naprava | Odprta vrata | Tveganje |
|----|---------|--------------|----------|
| 192.168.0.1 | TP-LINK Router | 53, 80, 443 | 🔴 KRITIČNO |
| 192.168.0.100 | Amazon (Echo/FireTV) | vse filtrirano | ✅ dobro |
| 192.168.0.133 | Neznana naprava (MAC rand.) | — | 🟡 SREDNJE |
| 192.168.0.171 | Miele gospodinjska naprava | 80 | 🔴 KRITIČNO |
| 192.168.0.191 | TP-LINK RE580D razširjevalnik | 80 | 🟠 VISOKO |
| 192.168.0.206 | Sony Smart TV | 80 | 🟠 VISOKO |
| 192.168.0.225 | Neznana naprava (MAC rand.) | — | 🟡 SREDNJE |
| 192.168.0.226 | HP Smart Tank 750 | 80, 443 | 🟠 VISOKO |
| 192.168.0.148 | Surface Pro 7 (ta stroj) | localhost only | ✅ varno |

## Kritične ranljivosti

### 1. TP-LINK Router — stara firmware (BusyBox 1.19.4)

Firmware iz julija 2019 — **7 let brez posodobitev**. BusyBox HTTP strežnik iz 2011-2012.

**Znani CVE-ji:**
- CVE-2022-30024 — stack buffer overflow v BusyBox HTTP
- CVE-2021-42376 — NULL pointer dereference (DoS)
- CVE-2021-42380 — use-after-free v ash shell
- CVE-2019-17147 — TP-LINK XSS v web vmesniku

**Dodatno:** Firmware vsebuje vgrajen Weinre debug (`target-script-min.js#anonymous`) — debug orodje v produkciji!

Admin dostopen na HTTP (nešifriran) in HTTPS (403). Login: `/webpages/login.html`.

### 2. Miele IoT — CORS wildcard

REST API streje z `Access-Control-Allow-Origin: *` — katerakoli spletna stran lahko pošlje zahtevke iz brskalnika.

**Status po dodatnem testiranju:** CORS wildcard potrjen, ampak noben standardni endpoint ni dostopen (vse vrača 404 razen OPTIONS). Miele@home API zahteva verjetno pairing/avtentikacijo. Tveganje obstaja, ampak je pogojno.

## Visoke ranljivosti

### 3. HP Smart Tank 750 — 22/24 LEDM endpointov brez gesla

LEDM API razkrije brez avtentikacije:
- Serijska številka: `TH4C27B18F`
- UUID: `b1c64a1f-0bed-4700-b7c0-975b5b2db9ed`
- 614 natisnjenih strani, 40ml črnila
- SNMP config: `publicAllowed`, `readOnly`
- mDNS hostname: `HP246A0E89EAFC.local.`
- WebServices: WSPrint, WSScan, WSDiscovery — vsi enabled
- Printer v PowerSave (zaznavnost aktivnosti)

### 4. HP SNMP — enabled z publicAllowed

SNMP omogočen, community string "public" dovoljen. Dostop do mrežne konfiguracije in tiskalnih statistik.

### 5. TP-LINK RE580D — web vmesnik brez gesla

Web vmesnik dostopen takoj brez avtentikacije. Login forma nima CSRF tokena. CGI endpointi vračajo 501 (backend ni funkcionalen), ampak CSRF ranljivost ostaja.

### 6. Sony Smart TV — Bravia API brez auth

Aktivni endpointi brez avtentikacije:
- `/sony/system` → getPowerStatus (TV vklopljen)
- `/sony/audio` → getVolumeInformation (vol=0, slušalke), getSpeakerSettings (subwoofer=17, pozicija: na mizi)
- `/sony/avContent`, `/sony/appControl`, `/sony/videoScreen`, `/sony/browser`, `/sony/cec`

Zahteva PIN auth: getSystemInformation, getApplicationList, getPlayingContentInfo, getNetworkSettings.

### 7. DNS open resolver

Router odgovarja na zunanje DNS queryje (amplifikacijski faktor 38x). **Port 53 blokiran na WAN** — ni izkoriščljivo od zunaj.

### 8. Go4Panda4Hrovat — WPS 1.0 na IoT omrežju

BSSID: `DC:2C:6E:D4:30:42`, kanal 9. WPS 1.0, ni zaklenjen. Namenjeno kameram in senzorjem.

**Pixie Dust test:** Ni ranljiv (router ne razkrije PKE/PKR nonces). Standard brute-force teoretičen (~4-11 ur), ampak ni rate limitinga.

## Srednje ranljivosti

### 9. CSRF na TP-LINK RE580D

Login forma (`/cgi-bin/luci`) brez CSRF tokena. Backend vrača 501, kar zmanjša izkoriščljivost.

### 10. Odsotnost VLAN segmentacije

Vse naprave na istem subnetu. Priporočena arhitektura:
- VLAN 10 (Zaupni): PC, telefoni
- VLAN 20 (IoT): Miele, Sony TV, Amazon Echo
- VLAN 30 (Gostje): izolirano

### 11. Neznane naprave z random MAC

192.168.0.133, 192.168.0.225 — najverjetneje telefoni/tablice.

### 12. Router HTTP admin (nešifriran)

Geslo leti po WiFi v čistem besedilu.

### 13. HP WiFi Direct AP z WPS 2.0

BSSID: `26:6A:0E:89:EA:FD` (`DIRECT-FD-HP Smart Tank 750`). Direkten dostop do tiskalnika mimo omrežja.

## WiFi WPS inventar

| BSSID | ESSID | WPS | dBm | Kanal |
|-------|-------|-----|-----|-------|
| DC:2C:6E:D4:30:42 | Go4Panda4Hrovat | 1.0 ⚠️ | -60 | 9 |
| 50:D4:F7:82:4E:3D | TP-Link_4E3D | 2.0 | -60 | 10 |
| 26:6A:0E:89:EA:FD | DIRECT-FD-HP Smart Tank 750 | 2.0 | -65 | 6 |
| 88:C3:97:F0:DB:D7 | DavidP | 2.0 | -91 | 1 |
| 3C:84:6A:DB:F2:B7 | Miki | 2.0 | -93 | 5 |

## Zunanja ekspozicija

✅ Port 53 blokiran na WAN — DNS amplifikacija ni mogoča od zunaj.
✅ Vsa testirana vrata (80, 443, 8080, 22, 23, 53) filtrirana na zunanjem IP-ju.
✅ Lokalne storitve na Surface Pro vezane samo na localhost.

## Pozitivne ugotovitve

- Amazon naprava popolnoma zaprta (vsa vrata filtrirana)
- HP tiskalnik ima HSTS (Strict-Transport-Security)
- UPnP na routerju ni odziven
- HP firmware posodobljen (2026-03-03)
- Surface Pro — nobena storitev ekspozirana na omrežje

## Prioritetni akcijski načrt

### Takoj
1. Posodobi firmware TP-LINK routerja
2. Onemogoči HTTP admin (samo HTTPS)
3. Nastavi geslo za TP-LINK RE580D
4. Onemogoči WPS na Go4Panda4Hrovat
5. Onemogoči LEDM API brez gesla na HP tiskalniku
6. Onemogoči HP WiFi Direct

### Ta teden
7. Posodobi Sony TV firmware
8. Onemogoči Remote Management na razširjevalniku
9. Preveri router geslo (ni default?)
10. Onemogoči SNMP ali spremeni community string

### Ta mesec
11. Implementiraj VLAN segmentacijo
12. MAC whitelist na WiFi
13. Dokumentiraj vse naprave
14. Monitoring za nove naprave (ntopng)

## Nerešene ranljivosti (status)

| # | Ranljivost | Tveganje | Status |
|---|------------|----------|--------|
| 1 | TP-LINK stara firmware | 🔴 KRITIČNO | ❌ Nepopravljeno |
| 2 | Miele CORS wildcard | 🔴 KRITIČNO | ❌ Nepopravljeno |
| 3 | HP 22/24 LEDM endpointov | 🟠 VISOKO | ❌ Nepopravljeno |
| 4 | HP SNMP publicAllowed | 🟠 VISOKO | ❌ Nepopravljeno |
| 5 | RE580D web vmesnik brez gesla | 🟠 VISOKO | ❌ Nepopravljeno |
| 6 | Sony TV Bravia API brez auth | 🟠 VISOKO | ❌ Nepopravljeno |
| 7 | DNS open resolver | 🟠 VISOKO | ❌ Nepopravljeno |
| 8 | Go4Panda4Hrovat WPS 1.0 | 🟠 VISOKO | ❌ Nepopravljeno |
| 9 | CSRF na RE580D | 🟡 SREDNJE | ❌ Nepopravljeno |
| 10 | Brez VLAN segmentacije | 🟡 SREDNJE | ❌ Nepopravljeno |
| 11 | Neznane naprave rand. MAC | 🟡 SREDNJE | ❌ Nepopravljeno |
| 12 | Router HTTP admin | 🟡 SREDNJE | ❌ Nepopravljeno |
| 13 | HP WiFi Direct WPS 2.0 | 🟡 SREDNJE | ❌ Nepopravljeno |

## Orodja za nadaljnje testiranje

```bash
# WPS status
sudo wash -i wlp0s20f3mon -C

# WiFi handshake capture
sudo airodump-ng wlp0s20f3mon --bssid DC:2C:6E:D4:30:42 -c 9

# SNMP dump
sudo apt install snmp
snmpwalk -v1 -c public 192.168.0.226
snmpwalk -v1 -c public 192.168.0.1

# RouterSploit
pip3 install routersploit
python3 -m routersploit

# Miele API
curl -X OPTIONS http://192.168.0.171/ -v

# HP LEDM
curl -sk https://192.168.0.226/DevMgmt/DiscoveryTree.xml

# Router CVE
nmap --script http-vuln* 192.168.0.1
```

# Povezave

- [[OPSEC - digitalna anonimnost]] — širši kontekst digitalne varnosti

---
created: 06/28/2026
categories:
  - "[[Varnost]]"
  - "[[Infrastruktura]]"
rating: 9
tags:
  - 2🌲
related-to:
  - "[[Stanovanje - Skupnost Gerbičeva]]"
---

# Kaj je

Red team analiza domačega omrežja (192.168.0.0/24) — black-box pristop s fizičnim dostopom do LAN. Rezultat: **2 kritični**, **5 visokih** ranljivosti. Zunanji IP: 93.103.163.90. Ta stroj (Surface Pro 7, 192.168.0.148) je edini varen — vse storitve na localhost.

# Inventar omrežja

| IP | Naprava | Tveganje |
|----|---------|----------|
| 192.168.0.1 | **TP-LINK Router** (stara firmware) | 🔴 KRITIČNO |
| 192.168.0.171 | **Miele naprava** (CORS wildcard) | 🔴 KRITIČNO |
| 192.168.0.191 | **TP-LINK WiFi razširjevalnik** (brez gesla) | 🟠 VISOKO |
| 192.168.0.206 | **Sony Smart TV** (nginx + Bravia API) | 🟠 VISOKO |
| 192.168.0.226 | **HP Smart Tank 750** (LEDM API brez auth) | 🟠 VISOKO |
| 192.168.0.133 | Neznana naprava (random MAC) | 🟡 SREDNJE |
| 192.168.0.225 | Neznana naprava (random MAC) | 🟡 SREDNJE |
| 192.168.0.100 | Amazon Echo/FireTV | ✅ Varno (filtrirano) |
| 192.168.0.148 | Surface Pro 7 | ✅ Varno (localhost) |

# Kritične ranljivosti

## TP-LINK Router — firmware star 7 let

Router (192.168.0.1) poganja BusyBox httpd 1.19.4 — verzija iz 2011-2012. Firmware zadnjič posodobljen julija 2019. Web admin je dostopen na **nešifriranem HTTP**. Firmware vsebuje Weinre debug skript (`target-script-min.js`) v produkciji.

Znani CVE-ji:
- **CVE-2022-30024** — stack buffer overflow v HTTP strežniku
- **CVE-2021-42376** — NULL pointer dereference (DoS)
- **CVE-2021-42380** — use-after-free v ash shell
- **CVE-2019-17147** — TP-LINK XSS v web vmesniku

**Sanacija:** takoj posodobiti firmware, onemogočiti HTTP admin, zamenjati router (OpenWRT / Mikrotik / Ubiquiti)

## Miele IoT — CORS wildcard

Miele naprava (192.168.0.171) streže REST API z `Access-Control-Allow-Origin: *`. Katera koli spletna stran lahko iz brskalnika pošlje zahtevke na to napravo, ko si na domačem omrežju — **CSRF brez zaščite**.

**Scenarij napada:** phishing → uporabnik odpre zlonamerno stran → JavaScript pošlje `fetch('http://192.168.0.171/Devices')` → CORS dovoli branje odgovora.

**Sanacija:** posodobiti Miele firmware, izolirati na IoT VLAN. Preveriti CVE-2020-28396 (directory traversal).

# Visoke ranljivosti

## HP Smart Tank 750 — občutljivi podatki brez gesla

Tiskalnik razkriva serijsko številko (`TH4C27B18F`), UUID in model prek LEDM API **brez avtentikacije**. Management poti:

- `/DevMgmt/DiscoveryTree.xml` — vedno OK
- `/DevMgmt/ProductConfigDyn.xml` — serijska + UUID
- `/DevMgmt/ProductServiceDyn.xml` — vedno OK

LEDM knjižnica iz 2011 (SVN-IPG-LEDM.441, 2011-06-15), čeprav je firmware svež (2026-03-03). HP tiskalnik ima HSTS nastavljen — edina naprava s to prakso.

## TP-LINK WiFi razširjevalnik — brez gesla

192.168.0.191: web vmesnik dostopen takoj, cookie nastavljen brez prijave. Set-Cookie: `COOKIE=9400a8c0076be000`.

## Sony Smart TV — nginx + Bravia API

192.168.0.206: port 80 redirecta na content sharing app, Bravia API razkriva auth URL-je. Smart TV-ji redko dobivajo varnostne posodobitve.

# Srednje ranljivosti

- **Brez VLAN segmentacije:** vse naprave na istem podomrežju (192.168.0.0/24) — kompromitirana IoT naprava lahko napada PC
- **Neznane naprave:** 2-3 naprave z randomiziranimi MAC-i (verjetno telefoni, ni pa preverjeno)
- **Router admin na HTTP:** geslo za router leti po WiFi v čistem besedilu

# Kaj je dobro ✅

- Vse storitve na Surface Pro 7 vezane na localhost (PostgreSQL, Node.js, Tor)
- Amazon Echo dobro zaprt (vsa vrata filtrirana)
- UPnP onemogočen na routerju
- HP tiskalnik ima svež firmware (marec 2026)

# Akcijski načrt

## Takoj
1. Posodobiti firmware TP-LINK routerja
2. Onemogočiti HTTP admin na routerju
3. Nastaviti geslo za WiFi razširjevalnik
4. Preveriti Miele firmware posodobitve
5. Onemogočiti LEDM API na HP tiskalniku brez gesla

## Ta teden
6. Posodobiti Sony TV firmware
7. Preveriti router geslo (ni default admin:admin?)
8. Onemogočiti Remote Management na razširjevalniku
9. Izolirati IoT naprave na ločen WiFi

## Ta mesec
10. Implementirati VLAN segmentacijo (zaupni / IoT / gostje)
11. MAC whitelist na WiFi
12. Dokumentirati vse naprave
13. Monitoring za nove naprave (ntopng)

# Povezave

- [[Stanovanje - Skupnost Gerbičeva]] — domača infrastruktura
- [[Administracija - eDavki in ZZZS]] — ostala administracija

# Vir

- `~/red-team-report.md` — izvorna datoteka

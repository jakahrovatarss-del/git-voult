---
title: Vir - Zenmap Cheat Sheet
type: resource
category: opsec
created: 2026-07-13
---

# Vir - Zenmap Cheat Sheet

## Kaj je

Zenmap je uradni grafični vmesnik (GUI) za **Nmap** — orodje za skeniranje omrežij, ki ga uporabljam za inventar naprav in oceno ranljivosti doma (glej [[Red Team Report - Domace omrezje]]). Zenmap sestavi nmap ukaz iz izbranega profila, ga izvede in rezultat prikaže pregledno (topologija, seznam gostiteljev, podrobnosti na napravo).

Namesto ročnega tipkanja nmap flagov, izbereš **profil** iz spustnega menija ("Profile") ali napišeš ukaz ročno v polje "Command".

## Profil, ki ga uporabljam: Intense scan, all TCP ports

Ustreza temu nmap ukazu:

```
nmap -p 1-65535 -T4 -A -v <tarča>
```

Kaj vsaka zastavica pomeni:

| Flag | Pomen |
|------|-------|
| `-p 1-65535` | Skenira **vseh 65535 TCP vrat** (ne samo top 1000 kot privzeto) — zato traja precej dlje |
| `-T4` | Timing template "Aggressive" — hitrejši sken, manj zamud med paketi (primerno za lokalni LAN, ne za občutljive/oddaljene tarče) |
| `-A` | Vklopi **OS detection**, **version detection**, **script scanning (NSE)** in **traceroute** vse hkrati |
| `-v` | Verbose — sproti izpisuje napredek (zato vidiš vmesna poročila "Discovered open port...") |

Rezultat te uporabe je bil moj zadnji sken: 256 naslovov, 561 sekund, s polnimi service/OS/script podatki za vsako aktivno napravo.

### Kdaj to uporabiti

- Ko želiš **popoln** pregled ene ali več naprav (vsa vrata, ne le pogosta)
- Za red team / varnostni pregled lastnega omrežja, kjer želiš vse podatke naenkrat
- **Ne** za hitro preverjanje "je gostitelj živ" — za to obstajajo hitrejši profili (glej spodaj)

### Slabosti

- Počasen (minute do ur, odvisno od št. naprav in odzivnosti)
- Glasen — zlahka zaznan s strani IDS/IPS (ni pomembno v lastnem domačem omrežju)
- NSE skripte lahko sprožijo nepričakovano vedenje na občutljivih napravah (IoT, tiskalniki)

---

## Cheat Sheet — Zenmap Profili in Ukazi

| Profil (v Zenmap meniju) | Nmap ukaz | Kdaj uporabiti |
|---|---|---|
| Intense scan | `nmap -T4 -A -v` | Splošen podroben pregled ene tarče, top 1000 vrat |
| **Intense scan, all TCP ports** | `nmap -p 1-65535 -T4 -A -v` | Popoln pregled — vsa vrata + OS/version/script/traceroute |
| Intense scan, no ping | `nmap -T4 -A -v -Pn` | Ko tarča blokira ping (ICMP), a veš da je aktivna |
| Intense scan plus UDP | `nmap -sS -sU -T4 -A -v` | Ko sumiš na UDP storitve (DNS, SNMP, NTP...) |
| Ping scan | `nmap -sn` | Samo ugotovi, katere naprave so žive (host discovery), brez skena vrat |
| Quick scan | `nmap -T4 -F` | Hiter pregled top ~100 vrat, brez detekcije verzij |
| Quick scan plus | `nmap -sV -T4 -O -F --version-light` | Hiter + osnovna OS/version detekcija |
| Quick traceroute | `nmap -sn --traceroute` | Samo pot do tarče, brez skena vrat |
| Regular scan | `nmap` | Privzeti nmap sken, brez dodatnih opcij |
| Slow comprehensive scan | `nmap -sS -sU -T2 -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 -A -v` | Zelo temeljit, zelo počasen, poskuša obiti firewalle |

### Uporabni ročni dodatki (v polje "Command")

| Ukaz / flag | Namen |
|---|---|
| `-sS` | SYN stealth scan (privzeti tip skena, ne odpre polne TCP povezave) |
| `-sV` | Zazna verzijo storitve na odprtih vratih |
| `-O` | Zazna operacijski sistem tarče |
| `-p-` | Krajši zapis za `-p 1-65535` (vsa vrata) |
| `--script=vuln` | Zažene NSE skripte za znane ranljivosti (CVE preverjanje) |
| `--script=http-vuln*` | Samo HTTP-related vuln skripte |
| `-oA <ime>` | Shrani rezultat v vseh formatih (.nmap, .xml, .gnmap) — za kasnejšo primerjavo skenov |
| `-6` | IPv6 sken |
| `--top-ports 20` | Samo 20 najpogostejših vrat (zelo hiter, grob pregled) |

### Branje rezultatov (Zenmap zavihki)

- **Nmap Output** — surovi terminalski izpis (kot v CLI)
- **Ports/Hosts** — pregledna tabela odprtih vrat po gostitelju
- **Topology** — vizualni zemljevid omrežja (radialni prikaz razdalje/hopov)
- **Host Details** — OS fingerprint, uptime, MAC/vendor za izbrano napravo
- **Scan Details** — kateri ukaz je bil dejansko izveden, trajanje

### Praktični workflow za domači red team pregled

1. Najprej `Ping scan` (`-sn`) čez cel subnet → seznam živih naprav
2. Nato `Intense scan, all TCP ports` na vsako zanimivo/novo napravo posebej (hitreje kot na cel /24 hkrati)
3. Za sumljive naprave dodaj `--script=vuln` za CVE preverjanje
4. Shrani z `-oA` in primerjaj z `.gnmap` diff-om med skeni (spremembe v času)

---

## Povezave

[[Red Team Report - Domace omrezje]] | [[Omrežje - Varnostni Red Team Report]] | [[OPSEC - digitalna anonimnost]]

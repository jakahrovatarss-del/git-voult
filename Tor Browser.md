---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - privacy
  - OPSEC
  - OSINT
---

# Tor Browser

Tor (The Onion Router) je omrežje in brskalnik za anonimno brskanje po internetu. Promet se šifrira in preusmeri skozi tri naključne vmesne strežnike (hop-e) preden doseže cilj.

---

## Kako Deluje — 3-Hop Sistem

```
Ti → [Entry Node] → [Middle Node] → [Exit Node] → Spletna stran
```

- **Entry Node**: ve kdo si, ne ve kam greš
- **Middle Node**: ne ve nič (samo prenaša)
- **Exit Node**: ve kam greš, ne ve kdo si
- Vsak hop vidi samo sosednje — nihče nima celotne slike

Vsak sloj šifriranja se "odlušči" ob vsakem hopu — od tod ime **onion** (čebula).

---

## .onion Strani (Dark Web)

Strani s končnico `.onion` so dostopne samo skozi Tor. Strežnik ostane anonimen — fizična lokacija ni razkrita.

**OSINT uporaba**: monitoring darknet forumov za podatke o breachih, malware kampanjah, ranljivostih — brez deanonimizacije.

---

## Namestitev

1. Prenesi z **torproject.org** (uraden vir)
2. Preveri podpis GPG
3. Zaženi — brez dodatnih nastavitev

Za maksimalno anonimnost: **Tor skozi [[Qubes OS]] + Whonix** — promet ne more zaobiti Tor niti pri malware okužbi.

---

## OPSEC Pravila pri Uporabi

| Pravilo | Zakaj |
|---------|-------|
| Ne logiraš se v osebne račune | Poveže anonimno sejo z identiteto |
| Ne odpiraš datotek (PDF, .docx) medtem ko si online | Datoteke lahko komunicirajo mimo Tor |
| Ne povečuješ okna | Fingerprinting z resolucijo zaslona |
| Ne nameščaš dodatkov | Zlomijo anonimnost |
| Tor + VPN → VPN najprej | VPN skrije Tor pred ISP |

**Eldo Kim (Harvard bomb threat)**: Tor pravilno maskira IP — ampak bil je **edini Tor user na kampusnem Wi-Fi**. Korelacija časa → identifikacija. Tor ni dovolj brez [[OPSEC - digitalna anonimnost|širšega OPSEC konteksta]].

---

## Omejitve

- Počasno (3 hopi = latenca)
- Exit node vidi nešifriran promet (za strani brez HTTPS)
- Ne ščiti pred fingerprinting (brskalniški prstni odtis, JS)
- Ni anonimnost za aplikacije izven brskalnika

---

## Povezave

- [[OPSEC - digitalna anonimnost]] — Tor kot del de-Googlanja in anonimnega brskanja
- [[OSINT - odprtokodna inteligenca]] — dark web OSINT monitoring
- [[Qubes OS]] — idealno okolje za Tor (Whonix integracija)

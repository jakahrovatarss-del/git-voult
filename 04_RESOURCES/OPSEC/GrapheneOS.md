---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - privacy
  - OPSEC
---

# GrapheneOS

GrapheneOS je hardened Android OS za Google Pixel naprave — brez Google bloatware, z okrepljeno varnostjo in sandbox arhitekturo. Mobilni ekvivalent [[Qubes OS]]-a za Android.

---

## Zakaj GrapheneOS

Standardni Android (še posebej z Google Play Services) konstantno:
- pošilja lokacijo Googlu
- logira glasovne ukaze
- zbira podatke o nameščenih aplikacijah
- oddaja edinstvene identifikatorje

GrapheneOS ta strežnik odstrani — obdržiš kompatibilnost z Android aplikacijami brez telemetrije.

---

## Ključne Funkcije

| Funkcija | Opis |
|----------|------|
| **Sandboxed Google Play** | Google Play Services tečejo v izoliranem sandboxu — ne dobijo sistemskih privilegijev |
| **Network permission toggle** | Vsaki aplikaciji omeji dostop do interneta |
| **Sensors permission toggle** | Omeji dostop do kamere, mikrofona, GPS na app-level |
| **Duress password** | Alternativno geslo, ki zbriše napravo |
| **Auto-reboot** | Nastavi avtomatski reboot po X urah neaktivnosti |
| **PIN scramble** | Naključna razporeditev tipkovnice → zaščita pred shoulder surfing |
| **Storage scopes** | Aplikacija vidi samo datoteke, ki ji dovoliš |

---

## Podprte Naprave

Samo **Google Pixel** naprave (Pixel 6, 7, 8, 9 serija). Razlog: Titan M security chip + verified boot garancija.

Pixel je paradoks: zasebnostna rešitev za napravo, ki jo je naredil Google.

---

## Namestitev

1. **web.grapheneos.org** → spletni installer (Chrome/Chromium)
2. Odkleni bootloader na Pixelu
3. Flashaj skozi WebUSB
4. Po namestitvi: znova zakleni bootloader

---

## Primerjava z Alternativami

| OS | Varnost | Kompatibilnost | HW |
|----|---------|---------------|-----|
| **GrapheneOS** | ✅✅✅ | ✅✅ (sandbox Play) | Samo Pixel |
| **LineageOS** | ✅✅ | ✅✅✅ | Širok HW |
| **CalyxOS** | ✅✅ | ✅✅ | Pixel + nekaj |
| **Stock Android** | ✅ | ✅✅✅ | Vse |

---

## Povezave

- [[OPSEC - digitalna anonimnost]] — GrapheneOS kot del de-Googlanja
- [[Qubes OS]] — desktop ekvivalent
- [[Tor Browser]] — kombiniraj z Orbot za Tor na mobilnem

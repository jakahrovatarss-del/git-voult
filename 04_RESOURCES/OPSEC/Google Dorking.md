---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - OSINT
---

# Google Dorking

Google Dorking (Google hacking) je tehnika naprednih iskalnih operatorjev za odkrivanje javno dostopnih, a skritih informacij — dostopnih datotek, ranljivih strežnikov, prijav, kamer...

> Google indeksira vse kar je javno — vključno s stvarmi, ki ne bi smele biti javne.

---

## Ključni Operatorji

| Operator | Opis | Primer |
|----------|------|--------|
| `site:` | Išči samo na domeni | `site:vlada.si filetype:pdf` |
| `filetype:` | Specifičen tip datoteke | `filetype:xls "geslo"` |
| `inurl:` | Beseda v URL-ju | `inurl:admin inurl:login` |
| `intitle:` | Beseda v naslovu strani | `intitle:"Index of" /backup` |
| `intext:` | Beseda v vsebini | `intext:"confidential" filetype:doc` |
| `cache:` | Google-ova predpomnjena verzija | `cache:primer.si` |
| `"..."` | Točna fraza | `"internal use only" filetype:pdf` |
| `-` | Izključi besedo | `site:gov.si -www` |

---

## Praktični Primeri

```
# Odprte kamere (ki ne bi smele biti odprte)
intitle:"webcamXP" inurl:8080

# Exposed admin paneli
inurl:/admin/login.php

# Excel datoteke z gesli
filetype:xls "username" "password"

# Odprte direktorije z backupi
intitle:"Index of" inurl:backup

# PDF dokumenti z "zaupno"
filetype:pdf "zaupno" site:.si

# Ranljivi login portali
inurl:":8080/manager/html" intitle:"Apache Tomcat"
```

---

## OSINT Uporaba

- Najdi vse PDF dokumente podjetja s specifičnimi ključnimi besedami
- Poišči starejše verzije strani (v kombinaciji z [[Wayback Machine]])
- Odkrij subdomene: `site:podjetje.si -www`
- Najdi email naslove: `site:podjetje.si "@podjetje.si"`
- Preveri kaj Google ve o tebi: `"tvoje ime" site:linkedin.com OR site:facebook.com`

---

## Google Dork Database

**GHDB** (Google Hacking Database) na exploit-db.com — zbirka tisoč preverjenih dorkov, kategoriziranih po tipu (files containing passwords, vulnerable servers, sensitive directories...).

---

## Etika in Zakonitost

Google Dorking **sam po sebi je legalen** — iščeš javno dostopne podatke. Nezakonito postane, ko dostopneš do sistemov brez pooblastila ali zlorabljaš najdene podatke.

---

## Povezave

- [[OSINT - odprtokodna inteligenca]] — Google Dorking kot OSINT tehnika
- [[Wayback Machine]] — kombiniraj za historično iskanje
- [[OPSEC - digitalna anonimnost]] — razumej, kaj Google ve o tebi

---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - OSINT
---

# Wayback Machine

Wayback Machine (archive.org/web) je digitalni arhiv interneta — avtomatično shranjuje snapshote spletnih strani skozi čas. Deluje od leta 1996.

> Izbrisana objava ni izbrisana. Je v Wayback Machine.

---

## Kaj Arhivira

- Spletne strani (HTML, slike, JS) — snapshoti skozi čas
- Video in avdio (novice, YouTube videi pred brisanjem)
- Stari software, aplikacije, igre
- Digitalne knjige in dokumenti

Trenutno: **800+ milijard spletnih strani**, raste vsak dan.

---

## OSINT Uporaba

| Primer | Opis |
|--------|------|
| **Izbrisane objave** | Podjetje zbriše inkriminirajočo izjavo — Wayback jo ima |
| **Spremembe na strani** | Primerjaš verzije skozi čas — ko je bilo kaj dodano/odstranjeno |
| **Ugasnjena spletišča** | Domena ni več aktivna, vsebina pa obstaja |
| **Stari "about" / team strani** | Kdaj je bil kdo zaposlen, kakšna je bila organizacijska struktura |
| **Preiskovanje incident timeline** | Kdaj je podjetje spremenilo varnostno politiko po breachin |

---

## Kako Poiskati

```
https://web.archive.org/web/*/https://primer.si
```

Ali direktno: web.archive.org → vnesi URL → izberi datum na časovnici.

**API** za programatski dostop:
```
https://archive.org/wayback/available?url=primer.si&timestamp=20230101
```

---

## OPSEC Implikacija

Wayback Machine je avtomatiziran — ne moreš preprečiti arhiviranja. Preden karkoli objaviš online, predpostavi, da bo trajno.

Spletna stran ponuja obrazec za **odstranitev vsebine** — ampak to ni garancija in zahteva čas.

---

## Povezave

- [[OSINT - odprtokodna inteligenca]] — Wayback kot OSINT orodje za sledenje sprememb
- [[OPSEC - digitalna anonimnost]] — internet je trajen zapis

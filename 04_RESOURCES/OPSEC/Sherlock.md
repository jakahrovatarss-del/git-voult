---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - OSINT
---

# Sherlock

Sherlock je odprtokodno orodje za **username OSINT** — ob enem ukazu preveri, ali obstaja račun z danim uporabniškim imenom na 300+ platformah.

---

## Kaj Dela

Vnesi en username → Sherlock preveri: Twitter/X, Instagram, Reddit, GitHub, TikTok, LinkedIn, Steam, Twitch, Pinterest... in 300+ ostalih.

Izpis: URL do profila za vsako platformo, kjer račun obstaja.

---

## Namestitev in Uporaba

```bash
# Namestitev
pip3 install sherlock-project

# Osnovna uporaba
sherlock uporabnisko_ime

# Več imen hkrati
sherlock ime1 ime2 ime3

# Shrani rezultate
sherlock ime --output rezultati.txt

# Samo najdene (brez "not found")
sherlock ime --print-found
```

Alternativa brez namestitve: **sherlock-project.github.io** (spletna verzija).

---

## OSINT Scenariji

| Scenarij | Pristop |
|----------|---------|
| Preiskovati osebo z znano vzdevkom | Direkten username lookup |
| Ugotoviti ali oseba reuse-a username | Primerjaj profile — isti stil, slika, vsebina |
| Najti "izginulo" identiteto | Stare platforme morda ohranjajo profil |
| Povezati ločene online identitete | Isti username na različnih platformah = ista oseba |

---

## Omejitve

- Ne more dostopati do zasebnih profilov
- Nekatere platforme blokirajo avtomatizirane zahteve (rate limiting)
- False positives — username obstaja, ampak ni ista oseba
- Ne preverja vsebin, samo prisotnosti

---

## OPSEC Implikacija

Nikoli ne reuse-aj usernamea. En alias = ena platforma = ena operacija. Sherlock je dostopen vsakomur — kar ti poišče, poišče tudi nasprotnik.

Primer: **Ross Ulbricht (Silk Road)** — username "altoid" reused iz Bitcoinskih forumov → FBI Google → aretacija.

---

## Povezave

- [[OSINT - odprtokodna inteligenca]] — Sherlock kot social media OSINT orodje
- [[OPSEC - digitalna anonimnost]] — higiena identitet, zakaj ne reusaš usernamov

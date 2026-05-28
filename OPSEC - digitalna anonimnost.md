---
created: 2026-05-26
tags:
  - note
  - journal
  - cybersecurity
  - privacy
source: YouTube (Zuma channel) — OPSEC video
---

```table-of-contents
title: 
style: nestedList
minLevel: 0
maxLevel: 0
includeLinks: true
hideWhenEmpty: false
debugInConsole: false
```

# OPSEC — Digitalna Anonimnost

OPSEC (Operational Security) je sistematičen pristop k zaščiti lastne digitalne zasebnosti. Cilj: minimizirati sledljive sledi in preprečiti, da korporacije in tretje osebe gradijo profil o tebi.

> "Treat your entire life like a black ops mission."

---

# Zakaj Sploh

Celotna industrija obstaja samo za to, da te sledi, gradi tvoj profil in ga prodaja oglaševalcem, vladnim agencijam ali komerkoli, ki plača. Tvoji podatki so eden najvrednejših surovin 21. stoletja.

Odgovor ni paranoja — je **disciplina**. Enako kot [[Solo Ucenje|solo učenje]] zahteva sistem, zahteva OPSEC sistem navad.

---

# 1. Kompartmentalizacija

Eno napravo, en brskalnik za vse = ena luknja poruši vse. Kompartmentalizacija pomeni, da vsaka aktivnost živi v **ločenem, izoliranem silosu**.

## Digitalna Kompartmentalizacija

- **[[Qubes OS]]** — najboljša rešitev: vsak opravek teče v svoji virtualni mašini (VM), vsaka VM je ognjena pregrada. Avtomatsko menja MAC naslove.
- **Alternativa**: Linux + Docker kontejnerji (manj varno — deli jedro OS, ampak bolje kot nič)
- Vsak opravek = svoja VM, svoja identiteta, svoja email, svoja pot skozi omrežje
- **MAC address spoofing**: orodje `macchanger` randomizira hardware identifikator ob vsakem zagonu (v Qubes OS samodejno)

## Fizična Kompartmentalizacija

- En laptop za vsakdanje življenje, drug za občutljive operacije
- Nikoli ne mešaj online identitet z realnim življenjem
- Informacije na "need-to-know" osnovi — ena kompromitirana oseba ne poruši celotne mreže

---

# 2. Čiščenje Metapodatkov

Vsaka datoteka (slika, dokument, video) vsebuje **skriti metapodatki** — GPS koordinate, timestamp, model naprave, verzija softwara. To je digitalni prstni odtis.

## Orodja

| Orodje | Namenjeno za | Uporaba |
|--------|-------------|---------|
| **ExifTool** | Slike, splošno | `exiftool -all= datoteka.jpg` |
| **MAT2** | Večina formatov | GUI ali CLI |
| **FFmpeg** | Video | `ffmpeg -i input.mp4 -map_metadata -1 output.mp4` |

**Pravilo**: preden karkoli pošlješ ali objaviš → očisti metapodatke. Vedno. Brez izjeme.

Avtomatiziraj z Python skriptom ali Image Magick v batch načinu. Ne zanašaj se samo na storitve, ki to delajo za tebe — naredi to sam najprej.

Podrobneje: [[EXIF Metadata]]

---

# 3. De-Googlanje

Google zbira: vsako iskanje, lokacijo, glasovne ukaze, email vsebino, history. "Brezplačen" Gmail stane tvoje podatke.

## Koraki

1. **Revizija**: Prenesi Google arhiv podatkov — vidiš točno, koliko so nabrali
2. **Izvozi** kontakte, kalendarje → potem zbriši račun
3. **Iskanje**: Zamenjaj z [SearX](https://searx.be) (self-hosted) ali StartPage — self-hosted ne logira poizvedb
4. **Email**: Self-hosting z `Mail-in-a-Box` ali šifrirani ponudniki (ProtonMail, Tutanota)
5. **Android**: Flash **[[GrapheneOS]]** — brez Google bloatware, sandbox apps. Alternativa: LineageOS brez Google Play Services
6. **Brskalnik**: Utrdi Firefox z uBlock Origin, uMatrix. Za občutljive zadeve: [[Tor Browser]]
7. **Alternative naprave**: PinePhone ali Fairphone (čisti Linux Mobile)

---

# 4. Higiena Identitet

Vsaka online identiteta je **začasna**. Ko jo uporabiš, jo zavrzi. Ni "blagovnih znamk" v anonimnosti.

## Zakaj

Preiskovalci iščejo **vzorce**: iste uporabniško ime, enake tipkarske napake, enaki frazeji, enaki časovni vzorci aktivnosti — čez clearnet in darknet.

**Ross Ulbricht (Silk Road)**: milijardarski imperij, ki je propadel ker je reused username "altoid" iz Bitcoinskih forumov pri rekrutiranju za Silk Road. FBI je Googlan → poveže → aretacija.

**Pravilo**: en alias = ena operacija. Nato brisanje.

---

# 5. Generiranje Šuma

Prava anonimnost ni popolna nevidnost — je **nerazločnost v masi**. Kot v snegu: ne moreš hoditi brez sledi, ampak narediš toliko lažnih sledi, da prave nihče ne najde.

## Metode

- **Dummy računi** na socialnih omrežjih — objavljaj naključni šum z automated Selenium skripti
- **Lažna GPS spoofing** na mobilnih napravah — zmede profiling algoritmov
- Brskalniški extension **TrackMeNot** — periodično pošilja naključne poizvedbe v zgodovino iskanj
- Iščeš "pizzerija Tokio" medtem ko si v Teksasu → profil postane neuporabен

---

# 6. Fizični OPSEC

Digitalna zaščita je brez vrednosti, če je fizično okolje kompromitiran.

- **Molčanje** — nihče v tvojem vsakdanjem življenju ne sme vedeti obsega tvojega digitalnega znanja
- Urij odpornost na **social engineering** — napadalci pogosto ne vlomijo v sistem, ampak v osebo
- Mentaliteta: "nekdo me opazuje" — ne ker si paranoičen, ampak ker te disciplinira

---

# Poučni Primeri (Kaj Ne Delati)

| Primer | Napaka | Posledica |
|--------|--------|-----------|
| Ross Ulbricht (Silk Road) | Reused username "altoid" čez clearnet | Dosmrtna ječa |
| Eldo Kim (Harvard bombna grožnja) | Tor + hkrati prijavljen na šolski Wi-Fi | Edini Tor user na kampusu → aretacija |
| Hector Monsegur (LulzSec) | Pozabljeni VPN v IRC chatu | Realni IP → aretacija + ovajanje |

**Skupni imenovalec**: ena majhna napaka poruši vse.

---

# OPSEC Checklist

- [ ] Različne naprave / VM za različne aktivnosti
- [ ] Metapodatki očiščeni pred vsako objavo
- [ ] Google accounts zamenjani z zasebnimi alternativami
- [ ] Android → GrapheneOS ali LineageOS
- [ ] Vsak alias je enkraten in začasen
- [ ] Dummy aktivnost za zakrivanje realnih vzorcev

---

# Povezave

- [[OSINT - odprtokodna inteligenca]] — kako te drugi iščejo (razumej napad za boljšo obrambo)
- [[Qubes OS]] — najboljši OS za OPSEC
- [[Tor Browser]] — anonimno brskanje
- [[GrapheneOS]] — hardened Android
- [[EXIF Metadata]] — metapodatki in čiščenje
- [[Google Dorking]] — kako te Google indeksira

---

## Viri

- Zuma (YouTube) — OPSEC video

---
created: 2026-06-25
tags:
  - projekt/arss
  - tip/projekt
  - status/lead
  - drzava/nz
  - produkt/lobaro
type: projekt
---

# Wireless M-Bus Gateway V4 — NZ (Tether)

## Pregled

**Lead iz NZ** — Julian Cole (Tether Limited) išče Gateway V4 za testiranje na B-Meters retrofit instalaciji v komercialnih objektih na Novi Zelandiji.

**Status:** Čaka na dogovor. Klara je predlagala, da skupaj pogledata.

## Email nit

### Klara → Jaka (25. jun. 2026)

> "Bova malo skupaj pogledala enkrat."

Forwardala je celotno korespondenco z Julianom. Priložena slika (image.png).

### Klara → Julian (23. jun. 2026)

Uraden odgovor kot Lobaro distributer:

- Potrdila 868MHz kompatibilnost
- MQTT direct-to-cloud podprt
- AES-128 se ne dekriptira na napravi — forwardira 1:1, dekripcija na platformi
- LTE-M/NB-IoT deluje na NZ omrežjih (Spark, One NZ)
- V4 Edge za Ethernet
- LoRaWAN samo EU-868 (ni AS923)
- En gateway: do ~64.000 telegramov ali ~2.000 unikatnih merilnikov
- Enkraten nakup, brez licenčnin na merilnik
- Priporoča Lobaro platformo za remote management (plačljiv letni dostop)
- Julian-a preusmerila na [[#Osebe|Bobbyja in Johna]] (Strongcast, NZ partner)

### Julian → Klara (23. jun. 2026)

> "We would like to test one of these devices. Who can help us get our hands on one?"

### Julian → Klara (original)

Podrobna tehnična vprašanja o Gateway V4:

- EN13757-4, 868MHz, T1/C1 mode
- AES-128 encrypted telegrams
- MQTT (JSON) do lastnega clouda
- LTE-M/NB-IoT za NZ
- V4 Edge za Ethernet
- Kapaciteta in licenciranje

## Tehnični zaključki

| Vprašanje | Odgovor |
|---|---|
| Frekvenca | 868 MHz (standard), 433 MHz ni na voljo |
| Dekripcija | Na platformi, ne na napravi |
| MQTT direct | Da, JSON v lastni MQTT broker |
| LTE-M/NB-IoT | Deluje, APN priporočljiv |
| V4 Edge | Da, Ethernet + edge processing |
| LoRaWAN | Samo EU-868 (ni AS923 za NZ) |
| Kapaciteta | 64k telegramov ali ~2000 merilnikov |
| Cena | Enkraten nakup + opcijsko platforma (letno) |

## Osebe

| Ime | Vloga | Kontakt |
|---|---|---|
| **Klara Rennesson** | ARSS / Lobaro distributer | klara@arss.si, T: +386 40 276 101 |
| **Julian Cole** | Head of Sales, Tether (NZ) | Julian@tetherhq.com, M: +64 27 279 5359 |
| **Bobby Herbohn** | Strongcast (NZ partner) | bobby.herbohn@datadrop.com.au |
| **John Comino** | Strongcast (NZ partner) | john@strongcast.com.au |

## Akcije

- [ ] Dogovor s Klaro — "pogledat skupaj" (sestanek?)
- [ ] Pregledati attachment (image.png)
- [ ] Preveriti ali imamo Gateway V4 na zalogi za test
- [ ] Kontaktirati Bobbyja/John (Strongcast) za NZ support
- [ ] Pripraviti ponudbo za Tether

## Analiza priložnosti

### Ocena

Tether je resen lead — smart metering platforma, prevzem obstoječe infrastrukture na komercialnih nepremičninah. Če test uspe, sledijo večje količine. Julian je Head of Sales — odločevalec, ne samo tehnični kontakt.

**ARSS vloga:** ARSS je uradni Lobaro distributer. Strongcast (Avstralija/NZ) je naš partner za lokalno podporo. To pomeni, da ARSS dobi distributorski delež, Strongcast pa operativo na terenu — fer delitev.

### Tveganja in odprta vprašanja

| Tveganje | Ocena | Opomba |
|----------|-------|--------|
| **868 MHz frekvenca v NZ** | ⚠️ Srednje | Klara je napisala "usually available" — ni potrjeno. M-Bus kratkega dometa v buildingih ponavadi ni problem, ampak treba preveriti pri Strongcast ali NZ regulatorju (RSM). |
| **LTE-M bandi** | ⚠️ Srednje | "If network exists, device connects" je pavšalno. EU modemi ponavadi podpirajo Band 28 (700 MHz), ki ga NZ uporablja za LTE-M. Treba potrditi spec modema. |
| **LoRaWAN samo EU-868** | ✅ Jasno | NZ uporablja AS923 — za ta projekt ni relevantno, ker Julian hoče LTE-M. |
| **Kdo plača testno enoto?** | ❓ Odprto | Julian vpraša "who can help us get our hands on one" — verjetno pričakuje sample. Strongcast to reši. |
| **Lobaro platform fee** | ✅ Jasno | Julian noče platforme. HW je one-off purchase — to mu ustreza. |

### Marketinški potencial

Če gre skozi:
- **Referenca:** NZ pilot na komercialnih stavbah za ARSS kot Lobaro distributer
- **Pričevanje:** Tether kot customer story
- **Večja količina:** commercial property portfolio → lahko 20+ gatewayev
- **Širitev:** Strongcast kot regionalni partner v Avstralaziji

### Ključna ugotovitev iz korespondence

Klara je odgovorila zelo profesionalno — vsa tehnična vprašanja naslovila, Julianu dala jasno pot (Strongcast). Edina šibka točka je 868 MHz frekvenca v NZ — "usually available" ni dovolj trden odgovor za customerja, ki se odloča o rollout-u.

## Priporočilo

1. Strongcast naj potrdi 868 MHz M-Bus spekter v NZ (Bobby/John)
2. Strongcast naj Julianu da testno enoto (sample ali posojilo)
3. ARSS ostane v CC in spremlja — če gre v količino, se aktivira
4. Po testu: case study / referenca za ARSS spletno stran

## Naslednji koraki

- [x] Analiza narejena v Obsidian
- [ ] Pokazati Klari in uskladiti naslednje korake
- [ ] Počakati na odgovor Strongcast / Julian

## Povezave

- [[Arss.md|ARSS]]
- [[Klara pejt k njej pa zrihtej stvari|Task: Klara]]
- [[ARSS- ZAČETEK PRODAJE POSAMEZNIKOM.md]]
- [[AURA price list 2026.md]]

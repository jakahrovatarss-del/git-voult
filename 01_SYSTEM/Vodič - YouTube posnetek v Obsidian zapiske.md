---
created: 2026-06-07
tags:
  - vodič
  - sistem
---

# Kaj je ta vodič

Korak za korakom postopek za pretvorbo YouTube posnetka v hub poročilo + konceptne opombe po uveljavljenem sistemu. Cilj je da vsak posnetek ki ti da kaj vrednega postane del mreže - ne le enkratna opomba ki jo pozabiš.

---

# Faza 1 - Priprava pred gledanjem

Preden pritisneš play:

1. Odpri nov `.md` dokument v Obsidianu z naslovom formata:
   `Tema - podnaslov.md` (enako kot ostala hub poročila)

2. Pripravi frontmatter takoj:
```
---
created: YYYY-MM-DD
tags:
  - note
  - journal
source: [URL posnetka]
---
```

3. Zapiši si vprašanje: **kaj točno hočem iz tega posnetka?**
   Brez tega boš zapisoval vse in nič.

---

# Faza 2 - Med gledanjem

## Kaj opazuješ

Med gledanjem ne pišeš dobesedno - loviš strukturo in bistvo.

Vprašanja ki si jih postavljaš sproti:
- Kateri so glavni koncepti ki se pojavljajo?
- Kaj je tukaj novo kar še nimam v mreži?
- Kateri koncepti že obstajajo v moji mreži? → `[[WikiLink]]`
- Kaj je teza tega posnetka v eni povedi?

## Tehnika hitrega beleženja

Med gledanjem pišeš surove opombe v isti dokument pod začasno sekcijo `# Surove opombe`. Ne oblikuješ, ne urejuješ. Samo loviš ideje z lastnimi besedami.

**Ključno:** Nikoli ne kopiraš dobesedno. Zapišeš z lastnimi besedami takoj - to prisili možgane da razumejo, ne samo prenesejo.

Kadar naleteš na koncepte ki zaslužijo svojo opombo si označi z `*` da ga ne pozabiš:
```
* KONCEPT: ime koncepta - kratek opis zakaj je pomemben
```

## Marker za čas

Ko je kaj posebej dobrega zapiši timestamp:
```
[14:32] - tukaj razloži zakaj je X boljši od Y → dobra tabela za primerjavo
```

---

# Faza 3 - Takoj po gledanju (najpomembnejša faza)

## Korak 1 - Določi strukturo

Preden začneš pisati hub poročilo si odgovori:
- Koliko glavnih sekcij ima vsebina? (cilj: 4-7)
- Kateri koncept je osrednji? → to bo `# Uvod`
- Kaj je zaključna misel? → to bo `# Zaključek`

## Korak 2 - Napiši hub poročilo

Struktura hub poročila je vedno enaka:

```markdown
# Uvod
[2-4 stavki: kaj je tema, zakaj je pomembna, kakšna je teza posnetka]
[[WikiLink na obstoječe koncepte če obstajajo]]

# Struktura teme
[seznam vej/sekcij z [[WikiLinki]] na koncepte ki bodo dobili svoje opombe]
- **Veja 1** - [[Koncept1]]
- **Veja 2** - [[Koncept2]]
...

# [Sekcija 1]
[vsebina - direktno, brez floskulov]

# [Sekcija 2]
...

# Zaključek
[sinteza - kaj vzameš iz tega, kaj se poveže z obstoječim znanjem]

# Viri
- [Naslov posnetka](URL)
[[Obstoječe hub poročilo če se tematsko navezuje]]
```

## Korak 3 - Identificiraj koncepte

Pregledaj svoje `* KONCEPT:` markerje iz faze 2. Za vsakega si odgovori:

> Ali ta koncept obstaja v moji mreži?

- **Da** → samo dodaj `[[WikiLink]]` v hub poročilu, ne ustvarjaš nove opombe
- **Ne** → ustvari novo konceptno opombo

---

# Faza 4 - Pisanje konceptnih opomb

Za vsak nov koncept ustvari ločeno datoteko: `ImKoncepta.md`

Struktura konceptne opombe:

```markdown
---
categories:
  - "[[Koncepti]]"
created: YYYY-MM-DD
---

# Kaj je
[1-3 stavki: definicija koncepta v lastnih besedah]

# [Funkcionalna sekcija - odvisno od tipa koncepta]
Možne sekcije:
- # Zakaj deluje
- # Kako se gradi
- # Kako to uporabiti
- # Dimenzije
- # Zakaj je boljši od...
- # Neverbalni prikaz
- # Omejitve

# Viri
[[Hub poročilo iz katerega izhaja]]
[[Morebitno obstoječe hub poročilo ki pokriva isto temo]]
```

**Pravilo:** Konceptna opomba je kratka. Če postane dolga, razbiješ na dva koncepta.

---

# Faza 5 - Vzpostavi povezave

Ko imaš hub poročilo in konceptne opombe narejene:

1. **Hub → koncepti:** preveri da ima hub poročilo `[[WikiLink]]` za vsak koncept ki si mu naredil opombo

2. **Koncepti → hub:** preveri da ima vsaka konceptna opomba v `# Viri` link nazaj na hub poročilo

3. **Koncepti → koncepti:** poglej katere koncepte iz novih opomb že poznaš iz starih. Dodaj `# Povezano` sekcijo:
```markdown
# Povezano
[[ObstoječiKoncept1]]
[[ObstoječiKoncept2]]
```

4. **Stari hub → novi hub:** če se nova tema navezuje na obstoječe hub poročilo, pojdi v staro hub poročilo in dodaj link v `# Viri`:
```markdown
# Viri
- [originalni vir]
[[NovoHubPoročilo]]
```

---

# Faza 6 - Preveri mrežo

Odpri Obsidian Graph View in preveri:
- So novi nodi vidni?
- So povezani z obstoječimi?
- Ali kateri koncept "visi" brez povezave? → dodaj link

**Opomba:** Novo vozlišče ki je izolirano od mreže je izgubljen čas. Vsak nov zapis mora imeti vsaj eno zvezo z obstoječim.

---

# Hiter povzetek - celoten proces

```
PRED gledanjem
└── Odpri nov .md, frontmatter, zapiši vprašanje

MED gledanjem
└── Surove opombe z lastnimi besedami
└── Označi koncepte z *
└── Timestampaj kar je dobro

PO gledanju
└── Določi strukturo (4-7 sekcij)
└── Napiši hub poročilo
└── Identificiraj nove koncepte
└── Napiši konceptne opombe
└── Vzpostavi vse WikiLinke (hub↔koncepti, koncepti↔koncepti)
└── Preveri graph view
```

---

# Tipične napake

**Pišeš med gledanjem in oblikuješ hkrati.**
Ne. Med gledanjem loviš ideje, po gledanju oblikuješ.

**Konceptna opomba postane dolga.**
Razbiješ na dva koncepta. Konceptna opomba je fokusirana na eno stvar.

**Pozabiš na povratne linke.**
Koncepti brez `# Viri` so slepe ulice v mreži.

**Kopiraš dobesedno namesto z lastnimi besedami.**
Kopiraj idejo, ne besedilo. Lastne besede = razumevanje. Kopiran tekst = shramba ki je ne boš bral.

**Ustvariš hub poročilo brez konceptnih opomb.**
Hub poročilo brez konceptnih opomb je samo dolg zapis. Vrednost sistema je v mreži.

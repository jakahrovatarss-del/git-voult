---
tags: [mehanika, tehnično-risanje, GDT, tolerancing, načrti, vir]
predmet: Mehanika
datum: 2026-06-17
vir: "Understanding Engineering Drawings — The Efficient Engineer (YouTube)"
url: "https://youtu.be/ht9GwXQMgpo"
kanal: "The Efficient Engineer"
---

# Vir — Tehnično Risanje in GD&T

> Povzetek videa "Understanding Engineering Drawings" s kanala The Efficient Engineer.  
> Tehnično risanje je osnoven jezik inženirja — brez tega ne moreš komunicirati z delavnico.

---

## Zakaj tehnično risanje?

Tehnična risba je **edinstven jezik**, ki natančno opisuje obliko, dimenzije in toleranco dela. Napaka v branju risbe = napaka v proizvodnji.

---

## 1. Vrste pogledov (Views)

### Ortogonalni pogledi
Standardni pogledi na 3D objekt projicirani na 2D ravnino:

| Pogled | Opis |
|--------|------|
| Tloris (Top view) | Pogled od zgoraj |
| Naris (Front view) | Pogled spredaj |
| Stranski ris (Side view) | Pogled z desne ali leve |
| Zadnji pogled (Rear view) | Pogled od zadaj |
| Pogled od spodaj (Bottom view) | Pogled od spodaj |

> ⚠️ **Pozor (popravek iz videa @4:00):** Desni in zadnji pogled sta horizontalno zrcaljena, spodnji pogled je vertikalno zrcaljen!

### Prerezni pogledi (Section views)
Namišljeni prerez skozi del, da pokažemo notranjo geometrijo:
- **Polni prerez** (Full section) — celoten prerez
- **Polovični prerez** (Half section) — za simetrične dele
- **Lokalni prerez** (Detail section) — samo del prereza

---

## 2. Metode projekcije

### 1. kotna projekcija (First Angle — Evropa 🇪🇺)
- Objekt projiciramo na ravnino ZA njim
- Standard: **ISO** — simbol: ○ z levo stožčasto obliko

### 3. kotna projekcija (Third Angle — ZDA/UK 🇺🇸)
- Objekt projiciramo na ravnino PRED njim
- Standard: **ANSI** — simbol: ○ z desno stožčasto obliko

> **Slovenija:** Večinoma 1. kotna projekcija (ISO standard).

---

## 3. Kotiranje (Dimensioning)

### Osnovna pravila:
1. Vsaka dimenzija se pojavi **enkrat** — ne ponavljaj
2. Kotiraj direktno na pogled, kjer je oblika najjasnejša
3. Kotirne črte ne smejo se križati
4. Enote: privzeto **mm** (zapisano v glavi risbe)

### Tipi kotiranja:
| Tip | Opis |
|-----|------|
| Linearna kota | Razdalja med dvema točkama |
| Kotna kota | Kot med dvema ploskvama |
| Premer (⌀) | Valjaste oblike |
| Polmer (R) | Zaokrožitve |
| Globina (↧) | Luknje in utori |

### Referenčna točka (Datum):
Izhodiščna točka/ravnina za kotiranje. Vse ostale dimenzije so relativne glede nanjo.

---

## 4. Toleriranje (Tolerancing)

### Zakaj tolerance?
Vsak del ima **dovoljeno odstopanje** od nominalne mere. Brez toleranc bi bili deli nezmontirljivi ali predragi.

### Zapis tolerance:
$$\text{nominalna mera} ^{+\text{zgornje odstopanje}}_{-\text{spodnje odstopanje}}$$

Primer: $25 ^{+0.1}_{-0.0}$ → del je sprejemljiv med 25.0 in 25.1 mm

### Sistem ujemov (Fits):
| Tip | Opis | Primer |
|-----|------|--------|
| Tesno ujemanje (Interference fit) | Gred > Luknjo | Vpresovanje osi |
| Prehodno ujemanje (Transition fit) | Gred ≈ Luknja | Srednja ohlapnost |
| Prosto ujemanje (Clearance fit) | Gred < Luknja | Drsni ležaj |

---

## 5. GD&T — Geometrijsko Kotiranje in Toleriranje

GD&T (Geometric Dimensioning and Tolerancing) je napredni sistem, ki tolerira **obliko**, ne samo **mere**.

### Simboli GD&T:

| Simbol | Ime | Opis |
|--------|-----|------|
| ⏤ | Ravnost (Flatness) | Površina mora biti v tolerančnem pasu |
| ○ | Okroglost (Circularity) | Profil kroži znotraj dveh koncentričnih krogov |
| ⌭ | Valjičnost (Cylindricity) | Površina valja znotraj dveh coaksialnih valjev |
| ⊥ | Pravokotnost (Perpendicularity) | Površina ali os ⊥ na datum |
| ∥ | Vzporednost (Parallelism) | Površina ∥ na datum |
| ◎ | Koncentričnost (Concentricity) | Osi so koaxialne |
| ⌖ | Pozicija (True Position) | Točna lega luknje/elementa |
| ⌒ | Profilna toleranca (Profile) | Prostorska oblika površine |

### Feature Control Frame (Okvir kontrole):
```
[ Simbol | Toleranca | Datum ]
```
Primer: `[ ⊥ | 0.05 | A ]` → površina je pravokotna na datum A z toleranco 0.05 mm

---

## 6. Glava risbe (Title Block)

Vsaka tehnična risba vsebuje:
- Ime dela / številka dela
- Material
- Merilo (Scale)
- Enote
- Metoda projekcije (1. ali 3. kotna)
- Datum in podpis
- Revizije (spremembe)

---

## Najboljše prakse

- **Minimum pogledov** — samo toliko, kot je potrebno za enoznačen opis
- **Jasnost > Popolnost** — raje manj, a jasno
- **Funk. površine** — kotiraj tiste površine, ki so funkcionalno pomembne
- **Izogibaj se redundantnim kotam** — računalnik ne ve, katera je "prava"

---

## Samotest

- [ ] Znaš narisati 3 standardne ortogonalne poglede enostavnega dela?
- [ ] Veš, kakšna je razlika med 1. in 3. kotno projekcijo?
- [ ] Znaš prebrati toleranco $30 ^{+0.2}_{-0.1}$?
- [ ] Veš, kaj pomeni simbol ⊥ v GD&T okvirju?
- [ ] Znaš povedati razliko med Interference in Clearance fit?

---

## Flashcards

> Q: Kateri standard tehniškega risanja se uporablja v Evropi?
> A: ISO standard, 1. kotna projekcija (First Angle)

> Q: Kaj pomeni toleranca $50 ^{+0.0}_{-0.5}$?
> A: Del je sprejemljiv med 49.5 mm in 50.0 mm

> Q: Kaj je GD&T?
> A: Geometric Dimensioning and Tolerancing — sistem, ki tolerira obliko, orientacijo in pozicijo (ne samo mere)

> Q: Kaj pomeni simbol ⌖ v GD&T?
> A: True Position — tolerira točno lego elementa (npr. luknje) glede na datum

---

## Povezave

- [[Mehanika Hub]]
- [[Koncept - Upogib]]
- [[Koncept - Euler Uklon]]
- [[Vir - The Efficient Engineer Kanal]]
- [[05_SCHOOL/School Hub]]

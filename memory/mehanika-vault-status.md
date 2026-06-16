---
name: mehanika-vault-status
description: "Popoln pregled mehanika vault-a — note, PDF viri, povezave, stanje junij 2026"
metadata:
  node_type: memory
  type: project
---

## Vault struktura (lokalna pot)

**Vault root:** `/home/jaka/Zdaj Pa Zares Obsidian/`  
**Mehanika note (root):** `STATIKA.md` (v 05_SCHOOL/), `ravnovesje delca.md`, `Mehanika Hub.md`  
**Šolske note:** `05_SCHOOL/`  
**PDF-ji:** `Attachments/mehanika/` in `Attachments/fizika/`

> ⚠️ **Stanje po reorganizaciji (2026-06-16):** 6 starih not je bilo izbrisanih ali integriranih — glej opombe spodaj.

---

## PDF viri — Attachments/mehanika/

| Datoteka | Opis | Strani |
|----------|------|--------|
| `IMG_1241.pdf` | **Glavni vir za naloge** — upogib, uklon, prerezi | 56 |
| `IMG_1183.pdf` | Naloge — statika, notranje sile | 56 |
| `arne mehanika strojništvo.pdf` | Arne-ov učbenik mehanika (BF/strojništvo) | 161 (40 scaniranih) |
| `Celovit pregled izpitnih nalog iz Mehanike I in Statike.pdf` | Pregled izpitnih nalog | 4 |
| `engineering-mechanics-statics-r-c-hibbeler-12th-edition.pdf` | Hibbeler Statics 12th ed. | 706 (40 scaniranih) |
| `statikaNalogeJesenko.pdf` | Jesenko statika naloge | 14 |
| `NotrSileVaje (1).pdf` | Notranje sile — vaje | 18 |
| `podporeVeziLes.pdf` | Podpore in vezi — les | 19 |
| `LinKonstr1.pdf` | Linijske konstrukcije 1 | 10 |
| `mehLastnLes.pdf` | Mehanske lastnosti lesa | 9 |
| `vrsteKonstrukcijLes.pdf` | Vrste konstrukcij les | 19 |
| `SileBrezSkupnPrijem.pdf` | Sile brez skupnega prijemališča | 15 |
| `SileSskupnnimPrijem.pdf` | Sile s skupnim prijemališčem | 18 |
| `sSkupPrij.pdf` | Skupno prijemališče | 4 |
| `ZapiskiUvod.pdf` | Zapiski uvod | 7 |
| `Wood_As_An_Engineering_Material.pdf` | Les kot inženirski material | 186 |
| `DN1_diagrami.py` + `.ipynb` | Python koda za DN1 diagrame | — |

**Vsak PDF ima vzporedno `.md` datoteko** v isti mapi (povzetek / OCR vsebine).

---

## Obstoječe note — 05_SCHOOL/

### Koncept note (`05_SCHOOL/Zapiski/`)
- `Koncept - Upogib.md` ✅ — 7 korakov, M-diagram, Steiner, dimenzioniranje, SVG-ji, primeri, flashcards
- `Koncept - Euler Uklon.md` ✅ — 6 korakov, 4 Eulerovi primeri, ω tabela, SVG, flashcards
- `Koncept - Vztrajnostni moment.md` ✅ — enostavni prerezi, Steiner, sestavljeni prerezi (U, T, I, box), primer U-prerez
- `Koncept - Napetostno stanje.md` ✅ — 2D/3D Mohr, Tresca/Von Mises (canonical!), Hookov zakon 3D, lastne vrednosti
- `Koncept - NTM Diagrami.md` ✅ — N, T, M diagrami
- `Koncept - Torzija.md` ✅ — τ, zasuk φ, Bredt, kombinirano M+Mt
- `Koncept - Kinematika Mehanizmi.md` ✅ — pol hitrosti, kotalna kinematika
- `Koncept - Krožni žagalni stroj.md` ✅ — aplikacija mehanike
- `Koncept - Premo Gibanje.md` — fizika poglavje 2
- `Koncept - Zakoni Gibanja.md` — fizika poglavje 4
- `Koncept - Toplota.md` — fizika poglavje 11
- ~~`Koncept - Hipoteze Porusitve.md`~~ ❌ IZBRISANA — vsebina integrirana v `Koncept - Napetostno stanje.md#Hipotezi porušitve`

### Vaje note (`05_SCHOOL/Zapiski/`)
- `Vaje - Napetostni tenzor in Mohrova kroznica.md`
- `Vaje - NTM diagrami - Vse vrste.md`
- `Vaje - Trdnost in dimenzioniranje.md`

### Naloga note (`05_SCHOOL/Naloge/`)
- `Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib.md` — pravokotnik 13×22 cm
- `Naloga - Mehanika - Dimenzioniranje krozni prerez upogib.md` — d ≥ 17,44 cm
- `Naloga - Mehanika - Upogibne napetosti U-prerez.md` — σ_max = 1,50 kN/cm²
- `Naloga - Mehanika - Upogibne napetosti C-prerez.md`
- `Naloga - Mehanika - Napetosti skatlaski profil.md`
- `Naloga - Mehanika - Uklon lesene deske.md` — F_k = 0,524 kN, β=2
- `Naloga - Mehanika - Uklon leseni steber F_max.md` — F_max = 11,84 kN
- `Naloga - Mehanika - Uklon palica S_dop.md` — S_dop = 23,4 kN, jeklo
- `Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor.md`
- `Naloga - Mehanika - Tenzorska analiza - aluminijast kvader.md`
- `Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine.md`
- `Naloga - Mehanika - Izpit Feb2019 - Torzija Bredt skatlast.md`
- `Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises.md`
- `Naloga - Mehanika - Izpit Jul2018 - Cisto strizno stanje.md`

### Izpit note (`05_SCHOOL/Izpiti/`)
- `Izpit - Mehanika - Upogib.md` ✅ — 7 tipov nalog, algoritmi, formule, primer za vsak tip
- `Izpit - Mehanika - Celoletni 2026.md` ✅ — **PREP NOTA** (podrobni algoritmi, wiki-referenčna tabela, izpit 2026-06-19)
- `Izpit - Mehanika - Junij 2026.md` ✅ — **CHEAT SHEET** (kompaktne formule, hitra referenca za dan izpita)

### Ostalo v 05_SCHOOL/
- `STATIKA.md` ✅ — **PRENOVLJENA** (2026-06-16): SL↔EN terminologija, ravnotežne enačbe, podpore, redukcija sil, FBD postopek, Hibbeler ref.
- `School Hub.md` — centralni hub

---

## Root vault — note relevantne za mehaniko

- `Mehanika Hub.md` ✅ — hub s koncepti, nalogami, algoritmi, SVG listi
- `ravnovesje delca.md` — kratka nota ravnovesja točke, slika
- ~~`mehanika.md`~~ ❌ IZBRISANA — superseded by Mehanika Hub
- ~~`naloge statika.md`~~ ❌ IZBRISANA — integrirana v STATIKA.md
- ~~`Statika-enačbe statičnega ravnovesja...md`~~ ❌ IZBRISANA — integrirana v STATIKA.md
- ~~`Statika – enačbe ravnovesja, principi...md`~~ ❌ IZBRISANA — integrirana v STATIKA.md
- ~~`Sklop 1 Statika – enačbe statičnega ravnovesja...md`~~ ❌ IZBRISANA — integrirana v STATIKA.md

---

## Kako so note povezane

```
Mehanika Hub
├── Koncept - Upogib ←→ Koncept - Vztrajnostni moment ←→ Koncept - Euler Uklon
│       ↓                          ↓
│   Naloge upogib              Naloge uklon
│       ↓
│   Izpit - Mehanika - Upogib
│
├── mehanika (root) ← STATIKA ← ravnovesje delca
│
└── School Hub → 05_SCHOOL/
```

Vsaka Koncept nota → linki na naloge z `[[Naloga - Mehanika - ...]]`  
Vsaka Naloga nota → linki na Koncept s `[[Koncept - ...#Korak N]]` (sekcijski linki!)  
Izpit nota → zbira vse tipe nalog z linki na posamezne naloge

---

## Templates (08_TEMPLATES/Templates/)

Relevantne predloge:
- `Koncept - Template.md` — tip/definicija/razlaga/primer/zakaj/napake/povezave
- `Naloga - Template.md` — tip/predmet/rok/status/namen/zahteve/pristop/rešitev/refleksija
- `Izpit - Template.md`
- `School Note Template.md`

**Opomba:** Dejanske note v 05_SCHOOL so bogatejše od template — imajo enačbe, tabele, SVG-je, flashcards, ki v template niso.

---

## SVG diagrami (Attachments/mehanika/)

- `m_diagram_predznak.svg` — sagging/hogging, napetosti
- `m_diagram_tipi.svg` — 4 tipični M diagrami
- `upogib_lesen_nosilec.svg` — previsni nosilci
- `upogib_U_prerez_napetosti.svg` — U-prerez
- `uklon_lesena_deska.svg` — 4 Eulerovi primeri
- `vztrajnostni_moment_prerezi.svg` — prerezi z enačbami
- `DN1_diagrami.png`, `DN1_Mup.png`, `DN1_NTM_diagrami_celotna.png` — DN1 rešitve

---

## Manjkajoče (za ustvariti)

**Visoka prioriteta:**
- `Koncept - Nateg in tlak.md` — σ = N/A, Hookov zakon, raztezek
- `Koncept - Strižne napetosti.md` — τ = Q·S/(I·b)
- `Izpit - Mehanika - Uklon.md` — po vzoru Izpit - Upogib

**Why:** Pred vsako novo noto preveri ta seznam — prepreči duplikate.
**How to apply:** Ko ustvarjaš mehanika noto, najprej poglej ali že obstaja.

**Linked memories:** [[mehanika-workflow]], [[obsidian-note-style]]

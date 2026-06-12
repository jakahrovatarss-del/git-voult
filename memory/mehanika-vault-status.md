---
name: mehanika-vault-status
description: "Popoln pregled mehanika vault-a — note, PDF viri, povezave, stanje junij 2026"
metadata:
  node_type: memory
  type: project
---

## Vault struktura (lokalna pot)

**Vault root:** `/home/jaka/Zdaj Pa Zares Obsidian/`  
**Mehanika note (root):** direktno v root — `mehanika.md`, `STATIKA.md`, `ravnovesje delca.md`, `Mehanika Hub.md`, `naloge statika.md`  
**Šolske note:** `05_SCHOOL/`  
**PDF-ji:** `Attachments/mehanika/` in `Attachments/fizika/`

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
- `Koncept - Premo Gibanje.md` ✅ — fizika poglavje 2
- `Koncept - Zakoni Gibanja.md` ✅ — fizika poglavje 4
- `Koncept - Toplota.md` ✅ — fizika poglavje 11
- `Koncept - Krožni žagalni stroj.md` ✅ — aplikacija mehanike

### Naloga note (`05_SCHOOL/Naloge/`)
- `Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib.md` — pravokotnik 13×22 cm
- `Naloga - Mehanika - Dimenzioniranje krozni prerez upogib.md` — d ≥ 17,44 cm
- `Naloga - Mehanika - Upogibne napetosti U-prerez.md` — σ_max = 1,50 kN/cm²
- `Naloga - Mehanika - Uklon lesene deske.md` — F_k = 0,524 kN, β=2
- `Naloga - Mehanika - Uklon leseni steber F_max.md` — F_max = 11,84 kN
- `Naloga - Mehanika - Uklon palica S_dop.md` — S_dop = 23,4 kN, jeklo

### Izpit note (`05_SCHOOL/Izpiti/`)
- `Izpit - Mehanika - Upogib.md` ✅ — 7 tipov nalog, algoritmi, formule, primer za vsak tip

### Ostalo v 05_SCHOOL/
- `School Hub.md` — centralni hub, linki na STATIKA, mehanika
- `Zapiski/Govorniške Veščine - Nastop in Predstavitev.md`
- `Zapiski/Trening - ZMOREM Mars Venus.md`

---

## Root vault — note relevantne za mehaniko

- `Mehanika Hub.md` ✅ — hub s koncepti, nalogami, algoritmi, SVG listi
- `mehanika.md` — stara nota (daily format), vsebuje fizika dopolnilo (kinematika, Newton)
- `STATIKA.md` — statika: ravnovesje, FBD, reakcije podpor (pin, roller, vpetje), Hibbeler ref.
- `ravnovesje delca.md` — kratka nota ravnovesja točke, slika
- `naloge statika.md` — kratke statika naloge (napetost TAC, cos/sin)
- `Statika-enačbe statičnega ravnovesja, osnovni principi statike,redukcija sistema sil..md` — daljša statika nota (7677 B)
- `Sklop 1 Statika – enačbe statičnega ravnovesja...md` — sklop zapiskov

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
- `Koncept - Torzija.md` — zasuk, momentni diagram
- `Izpit - Mehanika - Uklon.md` — po vzoru Izpit - Upogib

**Why:** Pred vsako novo noto preveri ta seznam — prepreči duplikate.
**How to apply:** Ko ustvarjaš mehanika noto, najprej poglej ali že obstaja.

**Linked memories:** [[mehanika-workflow]], [[obsidian-note-style]]

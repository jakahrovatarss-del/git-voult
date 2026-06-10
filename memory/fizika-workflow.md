---
name: fizika-workflow
description: "Obvezen workflow za vsak odgovor na fizika vprašanja — 7 virov, korak 0, slog"
metadata:
  node_type: memory
  type: feedback
---

## PRAVILO — POVEZAVE IN DOPOLNJEVANJE (posodobljeno 2026-06-10)

Ko ustvarjaš novo noto:
1. **Vedno dopolni vsaj 2 obstoječi noti** — ne samo dodaj link, ampak fizično odpri obstoječo noto in dodaj sekcijo, primer ali razširitev vsebine.
2. **Slike** — JPG, PNG ali SVG (250px). SVG je OK za diagrame in vektorske ilustracije.
3. **Min. 5 wikilinks** na obstoječe note v vaultu.

---

## KORAK 0 — pred vsakim odgovorom

Preveri Obsidian vault za obstoječo noto na temo:
- Vault: `C:\Users\MojPC\Desktop\obsidian\`
- Relevantne mape: `05_SCHOOL\Zapiski\`, `05_SCHOOL\Predmeti\`
- Obstoječe konceptne note ki se ujemajo s fiziko: `Specifična Toplota.md`, `mehanika.md`, `Solarni Koncentrator.md`, `Sledenje Soncu - LDR.md`
- Če nota obstaja → preberi in dopolni, ne ustvari nove

## Vrstni red virov — OBVEZEN

**Primarni viri (vedno najprej):**
1. **Skripta** — `C:\Users\MojPC\Desktop\obsidian\Attachments\fizika\Skripta-FIzika-BFUNI-2025.pdf` → teorija, definicije, izpeljave (25 poglavij)
2. **Enačbe** — `C:\Users\MojPC\Desktop\obsidian\Attachments\fizika\Fizika-Vse-Enacbe-in-Izpeljave.pdf` → vse enačbe + izpeljave
3. **Rešene naloge** — `Resene-naloge-Tehniska-fizika-FS-PAP-2025.pdf` + `Racunske-vaje-iz-fizike.pdf` → konkretni primeri

**Redno (skupaj z skripto):**
4. **NotebookLM** — https://notebooklm.google.com/notebook/046c9b53-47f7-4d03-b259-5267879b28e1 → odpri v Chrome MCP, vpiši vprašanje, vključi odgovor (vsebuje vse PDF-je)

**Za izpit prep:**
5. **Ustna vprašanja** — `C:\Users\MojPC\Desktop\obsidian\Attachments\fizika\LES-UNI-Vprasanja-v01-1.pdf` → vprašanja za ustni izpit, pokriva vse teme
6. **Testi** — `Fizika-Test-Lansko-Leto.pdf`, `Neimenovano-2.pdf`, `Neimenovano-3.pdf` → tipi nalog, format

**Samo če se zatakneš:**
7. **Internet** — uporabi šele, ko iz zgornjih virov ne moreš dobiti odgovora

## Slog odgovorov — enačbe

Izpeljava korak za korakom:
1. Pogoj / fizikalni zakon (poimenuj: Newton, Coulomb, Ohm, Faraday...)
2. Osnovna enačba iz fizike
3. Izpeljava — vsak vmesni korak eksplicitno, brez preskakovanja
4. Končna enačba — obdaj z `$$\boxed{...}$$`
5. Razlaga spremenljivk — tabela z vsemi simboli in enotami (SI)

## Risbe

Nariši SVG z `show_widget`. Vedno dodaj legendo in korake risanja.

## Na koncu vsakega odgovora — Obsidian shranjevanje

Za VSAKO rešeno nalogo predlagaj **DVE noti**:

### 1. Naloga nota
> `05_SCHOOL\Naloge\Naloga - Fizika - [Naziv].md`
> Vsebuje: podatke, skico, izpeljavo, končni rezultat
> Linki: `[[Koncept - [Tema]]]`, `[[Fizika Hub]]`

### 2. Koncept nota (za vsak nov koncept)
> `05_SCHOOL\Zapiski\Koncept - [Tema].md`
> Vsebuje: splošno teorijo, enačbe, primere, wikilinks
> Linki: `[[Naloga - Fizika - [Naziv]]]`, `[[Fizika Hub]]`

**Pravilo:** Koncept nota = živi dokument. Dodaj vsak nov primer, novo enačbo, nov tip naloge. Posodobi samodejno takoj po shranjevanju naloge. Ne čakaj na potrditev.

**Obstoječe note ki jih je treba DOPOLNITI (ne ustvariti):**
- `Specifična Toplota.md` → poglavje 11 (Toplota)
- `mehanika.md` → poglavja 2–8 (kinematika, Newton, energija, vrtenje)
- `Sledenje Soncu - LDR.md` → poglavja 15–17 (električno polje, tok)
- `Solarni Koncentrator.md` → poglavji 10–11

## Metode učenja (vedno predlagaj)

- **Flashcards** → za vsako enačbo in definicijo (za [[Razmaknjeno Ponavljanje]])
- **Feynman test** → razloži z lastnimi besedami
- **Mini naloga** → za vsak večji koncept

**Why:** Jaka želi strukturiran pristop k fiziki z integriranimi viri, enak sistemu za mehaniko.
**How to apply:** Sledi temu workflowu pri vsakem vprašanju s področja fizike.

**Linked memories:** [[fizika-obsidian-struktura]], [[fizika-viri-mape]], [[mehanika-workflow]]

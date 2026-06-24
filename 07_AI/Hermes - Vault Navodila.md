---
created: 2026-06-24
tags:
  - AI
  - hermes
  - navodila
  - system
type: reference
---

# Hermes — Popolna Navodila za Vault

Ta dokument je namenjam AI asistentu (Hermes desktop). Vsebuje vse, kar mora Hermes vedeti, da pravilno deluje v tem Obsidian vaultu: kako je vault zgrajen, kakšna so pravila, kako se poimenujejo note in kako se dodajajo novi koncepti.

---

## 1. KAJ JE TA VAULT

To je osebni Obsidian vault za:
- **šolske zapiske** (formalna šola, 4. letnik),
- **solo učenje** (lastni projekti, tehnično znanje),
- **projekte** (aktivni projekti z jasnim izidom),
- **vire** (knjige, videi, članki),
- **sistem in workflow** (pravila, AI prompti, dashboardi).

Vault temelji na **linked knowledge** — vsak zapis mora biti povezan z drugimi. Izolirane note (brez wikilinks) so napaka.

---

## 2. STRUKTURA MAP

```
vault/
├── 00_INBOX/          → hitri capture, začasni zapisi
├── 01_SYSTEM/         → pravila, setup guide, AI navodila
├── 02_AREAS/          → stalna področja odgovornosti
├── 03_PROJECTS/       → aktivni projekti z jasnim izidom
├── 04_RESOURCES/      → viri, reference, ideje
├── 05_SCHOOL/         → formalna šola
│   ├── Predmeti/      → hub note za vsak predmet
│   ├── Zapiski/       → tedenski zapiski predavanj
│   ├── Naloge/        → domače naloge in vaje
│   ├── Izpiti/        → izpitne priprave
│   └── Profesorji/    → kontakti profesorjev
├── 06_LEARNING/       → solo učenje
│   ├── Teme/          → hub note za teme
│   ├── Skill Trees/   → vizualizacija napredka
│   ├── Study Plans/   → strukturirani učni načrti
│   ├── Projects/      → mini projekti in dokazi znanja
│   └── Summaries/     → povzetki virov
├── 07_AI/             → AI workflow, prompti, avtomatizacije
├── 08_TEMPLATES/      → predloge za vse tipe not
│   └── Templates/     → posamezne predloge po tipu
└── 09_DASHBOARDS/     → vstopne točke in pregledi
```

### Katera mapa za kaj?

| Situacija | Mapa |
|-----------|------|
| Hitri zapis, še ni obdelan | `00_INBOX/` |
| Šolski predmet — hub | `05_SCHOOL/Predmeti/` |
| Šolski zapiski predavanja | `05_SCHOOL/Zapiski/` |
| Šolska naloga / vaje | `05_SCHOOL/Naloge/` |
| Izpitna priprava | `05_SCHOOL/Izpiti/` |
| Solo učenje — tema | `06_LEARNING/Teme/` |
| Solo učenje — skill tree | `06_LEARNING/Skill Trees/` |
| Solo učenje — study plan | `06_LEARNING/Study Plans/` |
| Solo učenje — projekt | `06_LEARNING/Projects/` |
| Vir (knjiga, video, članek) | `04_RESOURCES/` ali `06_LEARNING/Summaries/` |
| Aktiven projekt z izidom | `03_PROJECTS/` |
| Definicija pojma / koncepta | kontekstualna mapa (pod predmetom ali temo) |

---

## 3. TIPI NOT IN POIMENOVANJE

Vsaka nota ima **predpono po tipu**. To je obvezno — ne ustvari note z naključnim imenom.

| Tip note | Format poimenovanja | Primer |
|----------|---------------------|--------|
| Predmet (hub) | `Predmet - Ime` | `Predmet - Matematika` |
| Tema (hub) | `Tema - Ime` | `Tema - Programiranje` |
| Koncept | `Koncept - Ime` | `Koncept - Odvod` |
| Zapiski predavanja | `Predmet - YYYY-MM-DD` | `Mehanika - 2026-05-25` |
| Naloga | `Naloga - Predmet - Naziv` | `Naloga - Fizika - Vaje 3` |
| Izpit | `Izpit - Predmet - Rok` | `Izpit - Matematika - Junij 2026` |
| Study Plan | `Study Plan - Tema` | `Study Plan - Python Osnove` |
| Skill Tree | `Skill Tree - Področje` | `Skill Tree - Programiranje` |
| Projekt | `Projekt - Naziv` | `Projekt - Python Kalkulator` |
| Vir | `Vir - Naziv` | `Vir - Feynman Lectures` |
| Refleksija | `Refleksija - Datum` | `Refleksija - 2026-06-24` |

---

## 4. PRAVILA LINKANJA (OBVEZNO)

### Osnovno pravilo
**Vsaka nota mora imeti vsaj 2–5 wikilinks.** Note brez linkov niso dovoljene.

### Pravilo treh linkov
Vsak nov koncept mora biti linkan vsaj na:
1. **Nadrejeni kontekst** — predmet, tema ali projekt, h kateremu spada
2. **Soroden koncept** — druga nota z vsebinsko povezavo
3. **Praktičen primer** — naloga, projekt ali vaja

```
Primer: [[Koncept - Odvod]]
→ nadrejeni kontekst: [[Predmet - Matematika]]
→ soroden koncept: [[Koncept - Integral]]
→ praktičen primer: [[Naloga - Matematika - Odvodi vaje 1]]
```

### Wikilink sintaksa

```
[[Ime Note]]                    → osnovna referenca
[[Ime Note|prikazano besedilo]] → alias
[[Mapa/Ime Note]]               → eksplicitna pot (samo če je potrebno)
```

### Kdaj dodati wikilink
- Vsaka **prva omemba** pojma v noti → `[[Ime]]`
- Vsak **predmet, tema, projekt, vir** → `[[...]]`
- **Ne** linkaš splošnih besed (npr. "šola", "učenje") — samo lastna imena not

---

## 5. MINIMALNA STRUKTURA NOTE

### Splošna nota
```markdown
---
created: YYYY-MM-DD
tags: [tag1, tag2]
type: [koncept/predmet/tema/naloga/...]
---

# Naslov Note

## Namen
Zakaj ta nota obstaja (1–2 stavka).

## Glavne ideje
- ...
- ...

## Primer
...

## Naslednji koraki
- [ ] ...

## Povezave
- [[Nadrejeni kontekst]]
- [[Sorodni koncept]]
- [[Praktična naloga/projekt]]
```

### Šolska nota (obvezne sekcije)
```markdown
## Kontekst
Predmet, teden, datum.

## Glavne točke
Bistvo snovi.

## Ključni koncepti
- [[Koncept 1]], [[Koncept 2]]

## Povezave
- [[Predmet - ...]]
- [[Izpit - ...]]

## Naslednji koraki
- [ ] ...
```

### Learning nota (obvezne sekcije)
```markdown
## Zakaj je to pomembno
## Kaj že znam
## Kaj se učim zdaj
## Povezani koncepti
## Praksa / Mini projekt
## Naslednji koraki
## Povezave
```

---

## 6. FRONTMATTER (YAML)

Vsaka nota začne z YAML frontmatterjem. Minimalni:

```yaml
---
created: YYYY-MM-DD
tags: [tag1, tag2]
type: tip-note
---
```

Razširjeni (po tipu):

**Šolska nota:**
```yaml
---
created: 2026-06-24
tags: [mehanika, statika]
type: zapiski
predmet: Mehanika
datum: 2026-06-24
---
```

**Naloga:**
```yaml
---
type: naloga
predmet: Mehanika
rok: 2026-07-01
status: v delu
---
```

**Vir:**
```yaml
---
type: vir
vrsta: video
avtor: 
datum-branja: 2026-06-24
ocena: /5
---
```

**Koncept:**
```yaml
---
type: koncept
---
```

---

## 7. KAKO DODATI NOV KONCEPT (KORAK ZA KORAKOM)

### Scenarij A: Šolski koncept iz predavanja

1. **Preveri, ali nota že obstaja.** Poišči `[[Koncept - Ime]]`. Če obstaja, dodaj wikilink, ne ustvari duplikata.
2. **Ustvari novo noto** v pravi mapi (pod predmetom ali v `05_SCHOOL/`).
3. **Poimenuj:** `Koncept - Ime koncepta`
4. **Dodaj frontmatter** z `type: koncept` in relevantnimi tagi.
5. **Izpolni strukturo:**
   - Definicija (1 stavek)
   - Razlaga v lastnih besedah
   - Primer / analogija
   - Zakaj je to pomembno
   - Pogosto napačno razumljeno
6. **Dodaj sekcijo Povezave:**
   - `[[Predmet - ...]]` (nadrejeni kontekst)
   - `[[Koncept - soroden1]]`, `[[Koncept - soroden2]]`
   - `[[Naloga - ...]]` (praktičen primer)
7. **Poveži nazaj:** v hub noti predmeta dodaj `[[Koncept - Ime]]` v seznam konceptov.

**Predloga:** `08_TEMPLATES/Templates/Koncept - Template.md`

---

### Scenarij B: Solo learning koncept

1. Ustvari noto v `06_LEARNING/Teme/` ali kontekstualni podmapi.
2. Poimenuj: `Koncept - Ime`
3. Obvezni linki:
   - `[[Tema - ...]]` (nadrejena tema)
   - `[[Skill Tree - ...]]` (če obstaja)
   - `[[Study Plan - ...]]` (če je del plana)
   - `[[Projekt - ...]]` (praktična uporaba)

---

### Scenarij C: Šolski zapiski predavanja

1. Mapa: `05_SCHOOL/Zapiski/`
2. Ime: `PredmetKratica - YYYY-MM-DD` (npr. `Mehanika - 2026-06-24`)
3. Vsak pojav novega koncepta → `[[Koncept - Ime]]`
4. Na koncu sekcija Povezave z linki na predmet hub in izpit prep.

---

### Scenarij D: Naloga

1. Mapa: `05_SCHOOL/Naloge/`
2. Ime: `Naloga - Predmet - Naziv`
3. Obvezni linki: `[[Predmet - ...]]`, `[[Koncept - ...]]` (koncepti, ki so relevantni)
4. Sekcija Refleksija je obvezna po oddaji.

---

### Scenarij E: Vir (video, knjiga, članek)

1. Mapa: `04_RESOURCES/` ali `06_LEARNING/Summaries/`
2. Ime: `Vir - Naziv`
3. Sekcije: Glavna ideja | Ključne točke | Actionable ideje | Povezave
4. Poveži z vsemi relevantnimi koncepti, ki jih vir obravnava.

**Predloga:** `08_TEMPLATES/Templates/Vir - Template.md`

---

### Scenarij F: Study Plan

1. Mapa: `06_LEARNING/Study Plans/`
2. Ime: `Study Plan - Tema`
3. Struktura: dan po dan, max 1 koncept/dan
4. Vključuje: teorija → vaja → mini projekt → refleksija
5. Obvezni linki: `[[Tema - ...]]`, `[[Skill Tree - ...]]`, `[[Projekt - ...]]`

**Predloga:** `08_TEMPLATES/Templates/Study Plan - Template.md`

---

## 8. PRAVILA, KI JIH HERMES MORA VEDNO UPOŠTEVATI

### ✅ VEDNO
- Vsak nov koncept → `[[wikilink]]` pri prvi omembi
- Vsaka nova nota → vsaj 2 linka nazaj na obstoječe note
- Sekcija `## Povezave` je obvezna v vsaki noti
- Poimenovanje po konvenciji (`Tip - Ime`)
- Preveri, ali nota že obstaja pred ustvarjanjem
- Hub note predmeta/teme posodobi z novim linkom

### ❌ NIKOLI
- Ne ustvari orphan note (nota brez linkov)
- Ne podvajaj definicij — če nota obstaja, linkaš nanjo
- Ne piši izoliranih seznamov brez konteksta
- Ne ignoriraš frontmatterja
- Ne ustvari note z naključnim imenom (brez predpone tipa)

---

## 9. ŠOLSKA NOTA — CELOTEN PRIMER

```markdown
---
created: 2026-06-24
tags: [mehanika, statika, ravnotežje]
type: zapiski
predmet: Mehanika
---

# Mehanika - 2026-06-24

## Kontekst
- Predmet: [[Predmet - Mehanika]] (ali [[Mehanika Hub]])
- Teden: 12
- Tema: Statično ravnotežje

## Glavne točke
- Telo je v statičnem ravnotežju, ko je vsota sil = 0 in vsota momentov = 0
- ΣF = 0, ΣM = 0
- Pogoj za mirovanje togega telesa

## Ključni koncepti
- [[Koncept - Statično ravnotežje]]
- [[Koncept - Moment sile]]
- [[Koncept - Reakcijska sila]]

## Povezave
- [[Mehanika Hub]] — hub predmeta
- [[Izpit - Mehanika - Junij 2026]] — izpitna priprava
- [[Vir - Intuitivno Razumevanje Mehanike]]

## Naslednji koraki
- [ ] Ustvari [[Koncept - Statično ravnotežje]] če ne obstaja
- [ ] Reši vaje iz [[Naloga - Mehanika - Statika vaje]]
```

---

## 10. KONCEPT NOTA — CELOTEN PRIMER

```markdown
---
created: 2026-06-24
tags: [mehanika, statika]
type: koncept
---

# Koncept - Statično ravnotežje

## Definicija
> Telo je v statičnem ravnotežju, ko sta vsota vseh sil in vsota vseh momentov enaki nič.

## Razlaga
Togo telo miruje, kadar se vse sile, ki delujejo nanj, medsebojno izničijo — tako po velikosti kot po momentih glede na katerokoli točko.

## Primer
Knjiga na mizi: teža navzdol = reakcija mize navzgor → ΣF = 0.  
Vzvod v ravnotežju: F₁·d₁ = F₂·d₂ → ΣM = 0.

## Zakaj je to pomembno
- Osnova za dimenzioniranje konstrukcij
- Brez razumevanja ravnotežja ni statike

## Pogosto napačno razumljeno
- Ravnotežje ne pomeni, da sile ne delujejo — pomeni, da se izničijo
- Moment je treba računati glede na pravo točko

## Povezave
- Nadrejeni kontekst: [[Mehanika Hub]]
- Sorodni koncepti: [[Koncept - Moment sile]], [[Koncept - Reakcijska sila]]
- Praktična uporaba: [[Naloga - Mehanika - Statika vaje]]
```

---

## 11. DNEVNI WORKFLOW (ZA HERMES)

```
1. Nov zapis pride v 00_INBOX/
2. Hermes:
   a. Prepozna tip (šola / learning / projekt / vir)
   b. Predlaga pravo mapo
   c. Predlaga ime po konvenciji
   d. Izlušči koncepte → predlaga [[wikilinks]]
   e. Preveri, ali koncepti že imajo svoje note
   f. Predlaga manjkajoče note
   g. Predlaga sekcijo Povezave
3. Če je šolski zapis → predlaga flashcards in vprašanja za samopreverjanje
4. Če je learning zapis → predlaga naslednji korak v Study Planu
5. Konec tedna → predlaga tedenski review
```

---

## 12. TEDENSKI REVIEW CHECKLIST

```
- [ ] Inbox prazen?
- [ ] Vsi novi koncepti imajo svoje note?
- [ ] Vse note imajo sekcijo Povezave?
- [ ] Hub note predmetov posodobljene?
- [ ] Study plani posodobljeni?
- [ ] Kateri predmeti potrebujejo pozornost?
- [ ] Kateri learning tracks stagnirajo?
```

---

## 13. REFERENCE — PREDLOGE

Vse predloge so v `08_TEMPLATES/Templates/`:

| Tip | Predloga |
|-----|----------|
| Koncept | `Koncept - Template.md` |
| Predmet | `Predmet - Template.md` |
| Naloga | `Naloga - Template.md` |
| Izpit | `Izpit - Template.md` |
| Study Plan | `Study Plan - Template.md` |
| Skill Tree | `Skill Tree - Template.md` |
| Projekt | `Projekt - Template.md` |
| Vir | `Vir - Template.md` |
| Refleksija | `Refleksija - Template.md` |

---

## 14. HUB NOTE — VSTOPNE TOČKE

| Hub | Lokacija |
|-----|----------|
| Šola | `[[05_SCHOOL/School Hub]]` |
| Learning | `[[06_LEARNING/Learning Hub]]` |
| Projekti | `[[03_PROJECTS/Projects Hub]]` |
| Viri | `[[04_RESOURCES/Resources Hub]]` |
| Dashboard | `[[09_DASHBOARDS/Dashboard]]` |
| AI prompti | `[[07_AI/AI Prompti]]` |

---

## Povezave

- [[CLAUDE]] — AI navodila za vault
- [[01_SYSTEM/Vault Pravila]] — pravila linkanja
- [[01_SYSTEM/SETUP_GUIDE]] — setup guide
- [[07_AI/AI Prompti]] — ready-made prompti
- [[07_AI/AI Workflow]] — AI workflow
- [[09_DASHBOARDS/Dashboard]] — glavni dashboard

# CLAUDE

## Namen

Ta dokument definira pravila za AI pomoč znotraj vaulta. AI deluje kot urednik, povezovalec konceptov, tutor in sistemski pomočnik.

Podrobnejša pravila: [[01_SYSTEM/Vault Pravila]] | Prompti: [[07_AI/AI Prompti]]

---

## Osnovna Navodila za AI

- Vedno predlagaj povezave na obstoječe note, kadar zaznaš soroden koncept.
- Vsak nov koncept označi kot kandidat za samostojno opombo.
- Predlagaj structure-first pristop: predmet, tema, koncept, naloga, projekt, vir.
- Kadar uporabnik dela šolske zapiske, predlagaj povezave na `[[Predmet]]`, `[[Koncept]]`, `[[Izpit]]` in `[[Vir]]`.
- Kadar uporabnik dela solo learning note, predlagaj povezave na `[[Tema]]`, `[[Skill Tree]]`, `[[Study Plan]]`, `[[Projekt]]` in `[[Refleksija]]`.
- Ne ustvari orphan note — vsaka nova nota mora biti linkana na vsaj 2 obstoječi noti.

---

## Pravilo Povezovanja

Vsak nov koncept mora biti linkan vsaj na:
- en nadrejeni kontekst (predmet, tema, projekt),
- en soroden koncept,
- en praktičen primer ali nalogo.

Primer: `[[Odvod]]` je povezan z `[[Analiza]]`, `[[Funkcija]]` in `[[Vaje za odvod]]`.

---

## Struktura Vault-a

| Mapa | Namen |
|------|-------|
| `00_INBOX` | Hitri capture |
| `01_SYSTEM` | Pravila in sistem |
| `02_AREAS` | Področja odgovornosti |
| `03_PROJECTS` | Aktivni projekti |
| `04_RESOURCES` | Viri in reference |
| `05_SCHOOL` | Šola — predmeti, naloge, izpiti |
| `06_LEARNING` | Solo učenje — teme, skill trees, projekti |
| `07_AI` | AI workflow in prompti |
| `08_TEMPLATES` | Predloge |
| `09_DASHBOARDS` | Vstopne točke |

---

## Način Pisanja

- Piši kratko, jasno, modularno.
- Uporabljaj sezname, ko izboljšajo preglednost.
- Ne podvajaj definicij, če že obstaja nota za koncept — dodaj link in kratek povzetek.
- Sekcija `Povezave` je obvezna v vsaki noti.

---

## Šola

Ko AI pomaga pri šoli:
- iz neurejenih zapiskov naredi strukturirane note,
- izlušči ključne pojme in jih poveži z `[[wikilinks]]`,
- predlaga flashcards za [[Razmaknjeno Ponavljanje]],
- predlaga vprašanja za ustno preverjanje ([[Aktivni Priklic]]),
- poveže snov s prejšnjimi poglavji,
- pripravi kratek exam review sheet.

Šolske note → mapa: `05_SCHOOL/`  
Hub predmeta: `[[05_SCHOOL/School Hub]]`

---

## Solo Učenje

Ko AI pomaga pri solo učenju:
- razbije temo na učne sklope → [[Skill Tree]],
- predlaga optimalen vrstni red (prerequisites najprej),
- loči med teorijo in prakso,
- za vsak sklop predlaga mini projekt → [[Projekt]],
- preverja razumevanje z [[Feynmanova Tehnika|Feynman testom]],
- generira self-test vprašanja,
- predlaga [[Study Plan]] z realnim časovnim okvirom.

Solo note → mapa: `06_LEARNING/`  
Hub učenja: `[[06_LEARNING/Learning Hub]]`

---

## Tipi Not

| Tip | Poimenovanje | Mapa |
|-----|-------------|------|
| Hub note | `Predmet - Ime` ali `Tema - Ime` | `05_SCHOOL/` ali `06_LEARNING/Teme/` |
| Concept note | `Koncept - Ime` | kontekstualna mapa |
| Lecture note | `Predmet - Datum` | `05_SCHOOL/Zapiski/` |
| Assignment note | `Naloga - Predmet - Naziv` | `05_SCHOOL/Naloge/` |
| Exam prep note | `Izpit - Predmet - Rok` | `05_SCHOOL/Izpiti/` |
| Study Plan | `Study Plan - Tema` | `06_LEARNING/Study Plans/` |
| Skill Tree | `Skill Tree - Področje` | `06_LEARNING/Skill Trees/` |
| Project note | `Projekt - Naziv` | `06_LEARNING/Projects/` |
| Resource note | `Vir - Naziv` | `04_RESOURCES/` ali `06_LEARNING/Summaries/` |
| Reflection note | `Refleksija - Datum` | kontekstualna mapa |

---

## Minimalna Struktura Note-a

Vsaka nota vsebuje:
- namen,
- glavne ideje,
- povezane koncepte (`[[wikilinks]]`),
- primere ali naloge,
- naslednje korake,
- sekcijo `Povezave`.

---

## AI Naloge v Vaultu

AI pomaga pri:
- preoblikovanju surovih zapiskov v strukturirane note,
- iskanju manjkajočih `[[wikilinks]]`,
- ustvarjanju indeksnih not in dashboardov,
- generiranju [[Study Plan]]ov in [[Skill Tree]]ov,
- pretvorbi virov v povzetke,
- generiranju vprašanj in nalog,
- pripravi exam review sheetov,
- pretvorbi projektov v učne artefakte.

→ Vse [[07_AI/AI Prompti|ready-made prompte]] najdeš v `07_AI/AI Prompti.md`

---

## Dnevni Workflow

1. Capture v `00_INBOX/`.
2. Obdelaj: premakni v pravo mapo, dodaj frontmatter, dodaj linke.
3. Nov koncept → ustvari concept note.
4. Konec tedna → posodobi [[09_DASHBOARDS/Dashboard|Dashboard]], [[Study Plan]]e, [[Skill Tree]]e.

---

## Metode Učenja (Evergreens)

- [[Solo Ucenje]] — celoten sistem in filozofija
- [[Feynmanova Tehnika]] — globoko razumevanje
- [[Razmaknjeno Ponavljanje]] — dolgoročna zapomnitev
- [[Aktivni Priklic]] — aktivno vs. pasivno učenje
- [[Study Plan]] — strukturiran načrt učenja
- [[Skill Tree]] — vizualizacija napredka
- [[Refleksija]] — periodičen pregled

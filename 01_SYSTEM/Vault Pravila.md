---
created: 2026-05-25
tags:
  - system
  - rules
---

# 📐 Vault Pravila

Operativna pravila za ta vault. To je živi dokument — posodobi ga kadar se pravila spremenijo.

---

## Struktura Map

| Mapa | Namen |
|------|-------|
| `00_INBOX` | Hitri capture, obdelaj čim prej |
| `01_SYSTEM` | Pravila, tokovi, navodila |
| `02_AREAS` | Stalna področja odgovornosti |
| `03_PROJECTS` | Aktivni projekti z jasnim izidom |
| `04_RESOURCES` | Viri, članki, ideje |
| `05_SCHOOL` | Formalna šola — predmeti, naloge, izpiti |
| `06_LEARNING` | Solo učenje — teme, skill trees, projekti |
| `07_AI` | AI workflowi, prompti, avtomatizacije |
| `08_TEMPLATES` | Predloge za nove note |
| `09_DASHBOARDS` | Vstopne točke in pregledi |

---

## Pravila Linkanja

1. **Vsak nov koncept dobi svojo opombo** ali se poveže na obstoječo.
2. **Prva omemba** pomembnega pojma dobi `[[wikilink]]`.
3. **Vsak note** mora imeti vsaj **2–5 relevantnih povezav**.
4. **Vsaka nova nota** mora biti linkana vsaj na:
   - en nadrejeni kontekst (predmet, tema, projekt)
   - en soroden koncept
   - en praktičen primer ali nalogo
5. Ne piši izoliranih seznamov — poveži z `[[Predmet]]`, `[[Projekt]]`, `[[Koncept]]`, `[[Vir]]`.

---

## Tipi Not in Poimenovanje

| Tip | Format | Primer |
|-----|--------|--------|
| Predmet | `Predmet - Ime` | `[[Predmet - Matematika]]` |
| Tema | `Tema - Ime` | `[[Tema - Programiranje]]` |
| Koncept | `Koncept - Ime` | `[[Koncept - Odvod]]` |
| Naloga | `Naloga - Predmet - Naziv` | `[[Naloga - Fizika - Vaje 3]]` |
| Izpit | `Izpit - Predmet - Rok` | `[[Izpit - Matematika - Junij 2026]]` |
| Study Plan | `Study Plan - Tema` | `[[Study Plan - Python Osnove]]` |
| Skill Tree | `Skill Tree - Tema` | `[[Skill Tree - Programiranje]]` |
| Projekt | `Projekt - Naziv` | `[[Projekt - Python Kalkulator]]` |
| Vir | `Vir - Naziv` | `[[Vir - Feynman Lectures]]` |
| Refleksija | `Refleksija - Datum` | `[[Refleksija - 2026-05-25]]` |

---

## Minimalna Struktura Note-a

Vsaka nota po možnosti vsebuje:
- **Namen** — zakaj ta nota obstaja
- **Glavne ideje** — bistvo v bullet points
- **Povezani koncepti** — `[[wikilinks]]`
- **Primeri** — konkretni primeri
- **Naslednji koraki** — kaj sledi

---

## Šolske Note — Obvezne Sekcije

- Kontekst (kateri predmet, kateri teden)
- Glavne točke
- Ključni koncepti (z linki)
- Povezave
- Naslednji koraki

---

## Learning Note — Obvezne Sekcije

- Zakaj je to pomembno
- Kaj že znam
- Kaj se učim zdaj
- Povezani koncepti
- Praksa / Mini projekt
- Naslednji koraki

---

## Dnevni Workflow

1. Capture v `00_INBOX`.
2. Obdelaj: premakni v pravo mapo, dodaj frontmatter.
3. Dodaj povezave na obstoječe koncepte.
4. Če je koncept nov → ustvari concept note.
5. Konec tedna: posodobi dashboarde in study plane.

---

## Tedenski Review Checklist

- [ ] Inbox prazen?
- [ ] Novi koncepti linkani?
- [ ] Study plani posodobljeni?
- [ ] Kateri predmeti potrebujejo pozornost?
- [ ] Kateri learning tracks stagnirajo?
- [ ] Kateri viri so dejansko koristni?

---

## Povezave

- [[CLAUDE]] — AI navodila za vault
- [[07_AI/AI Workflow|AI Workflow]] — kako delati z AI
- [[09_DASHBOARDS/Dashboard|Glavni Dashboard]]
- [[Solo Ucenje]] — metodologija solo učenja

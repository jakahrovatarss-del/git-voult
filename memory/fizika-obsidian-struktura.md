---
name: fizika-obsidian-struktura
description: "Obsidian vault struktura in pravila za shranjevanje fizika not"
metadata:
  node_type: memory
  type: reference
---

## Vault lokacija

`C:\Users\MojPC\Desktop\obsidian\`

## Mape

| Mapa | Namen |
|------|-------|
| `05_SCHOOL\Zapiski` | Konceptne note, predavanja |
| `05_SCHOOL\Naloge` | Naloge (rešitve) |
| `05_SCHOOL\Izpiti` | Izpit prep |
| `06_LEARNING` | Solo učenje — cross-disciplinarni koncepti |

Hub predmeta: `[[05_SCHOOL/School Hub]]`
Fizika hub: `[[Fizika Hub]]`

## Tipi not in poimenovanje

| Tip | Ime datoteke | Mapa |
|-----|-------------|------|
| Hub | `Fizika Hub.md` | `05_SCHOOL\` |
| Koncept | `Koncept - ImeKoncepta.md` | `05_SCHOOL\Zapiski\` |
| Predavanje/zapiski | `Fizika - Datum.md` | `05_SCHOOL\Zapiski\` |
| Naloga | `Naloga - Fizika - Naziv.md` | `05_SCHOOL\Naloge\` |
| Izpit prep | `Izpit - Fizika - Rok.md` | `05_SCHOOL\Izpiti\` |

## Obvezna struktura note

```markdown
---
tags: [fizika, poglavje-X]
predmet: Fizika
datum: YYYY-MM-DD
---

# Naslov

## Namen

## Teorija / Glavne ideje

## Enačbe (z izpeljavo)

## Primeri / Naloge

## Flashcards (vprašanja za ponavljanje)

## Povezave
```

## Pravila

- Vsaj 2 wikilinks na obstoječe note (`[[Fizika Hub]]`, `[[Koncept - X]]`, sorodni koncepti)
- Brez orphan not
- Obstoječe note DOPOLNI, ne ustvarjaj duplikatov:
  - `Specifična Toplota.md` → za toploto/kalorimetrijo
  - `mehanika.md` → za kinematiko/dinamiko
  - `Sledenje Soncu - LDR.md` → za elektriko
  - `Solarni Koncentrator.md` → za termodinamiko
- SVG slike shrani v `Attachments\fizika\` in vstavi z `![[ime.svg]]`

**Linked memories:** [[fizika-workflow]], [[fizika-viri-mape]]

---
name: mehanika-workflow
description: "Obvezen workflow za mehanika vprašanja — 4 viri, korak 0, slog izpeljav, shranjevanje not"
metadata:
  type: feedback
---

## Kdo
Jaka Hrovat, strojništvo student. Vprašanja o mehaniki (statika, kinematika, dinamika, trdnost materialov).
Jezik odgovorov: **slovenščina**.

## KORAK 0 — pred vsakim odgovorom
Preveri vault: `05_SCHOOL/Zapiski/` in `05_SCHOOL/Predmeti/`
Če nota obstaja → preberi in uporabi kot osnovo.

## Viri (vse štiri pri vsakem odgovoru)

| # | Vir | Pot / URL |
|---|-----|-----------|
| 1 | Skeniran zvezek | `Attachments/mehanika/` — relevantne strani glede na temo |
| 2 | PDF predavanja | PDF iz `Attachments/mehanika/` ki ustreza temi |
| 3 | NotebookLM | https://notebooklm.google.com/notebook/3c9ae58d-26fa-428e-a49c-022594020583 — odpri Chrome MCP, vpiši vprašanje |
| 4 | Obsidian vault | obstoječe note za wikilinks |

## Slog odgovorov — enačbe
1. Pogoj za varno delovanje
2. Osnovna enačba
3. Zakon/princip (Coulomb, Newton, Hooke...)
4. Izpeljava korak za korakom (brez preskakovanja)
5. Končna enačba: `$$\boxed{...}$$`
6. Tabela spremenljivk

## Risbe
- SVG z `show_widget`, vedno z legendo

## Shranjevanje not
- **Vprašaj pred shranjevanjem** — ne shranjuj samodejno
- Mapa: `05_SCHOOL\Zapiski\`
- Ime: `Koncept - ImeKoncepta.md`
- Vsaka nota: vsaj 2 wikilinks na obstoječe note
- Obvezna sekcija `Povezave`

### Frontmatter template
```markdown
---
tags: [mehanika, ...]
predmet: Mehanika
datum: YYYY-MM-DD
---
```

## Na koncu vsakega odgovora
Vedno ponudi:
> **Shranim kot noto v Obsidian?**
> Predlog: `05_SCHOOL\Zapiski\Koncept - [Tema].md`
> Linki: `[[...]]`, `[[...]]`, `[[Mehanika Hub]]`

**Why:** Jaka želi strukturirane note z wikilinki za vsak rešen problem. Za mehaniko vedno vprašaj pred shranjevanjem (za fiziko shranjuj samodejno).
**How to apply:** Sledi workflowu pri vsakem mehanika vprašanju.

**Linked memories:** [[fizika-workflow]], [[obsidian-note-style]], [[mehanika-vault-status]]

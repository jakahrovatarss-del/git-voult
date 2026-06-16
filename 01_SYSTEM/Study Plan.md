---
categories:
  - "[[Evergreen]]"
created: 2026-05-25
tags:
  - 0🌲
  - learning
  - template
related-to:
  - "[[Solo Ucenje]]"
  - "[[Skill Tree]]"
  - "[[Refleksija]]"
---

# Study Plan

Study Plan je **strukturiran načrt učenja** za eno temo ali področje. Ni samo seznam virov — je pot od točke A (ne znam) do točke B (znam in znam dokazati).

## Zakaj Plan in Ne Samo Učenje

Brez plana učenje hitro postane: brskanje po YouTubu → naključni koncepti → občutek napredka brez resničnega znanja.

Plan prisili k odgovorom na:
- Kaj točno hočem znati?
- V kakšnem vrstnem redu?
- Kdaj sem "done"?

## Struktura Study Plana

Ustvari nov plan z: `Study Plan - [Tema]`

```markdown
---
tema: "[[TEMA]]"
cilj: "Znam [X] in to dokazujem z [PROJEKT]"
trajanje: 14 dni
status: aktiven
started: YYYY-MM-DD
---

## Cilj
Kaj točno znam na koncu? Kako to dokažem?

## Prerequisites
Kaj moram znati prej?
- [[Koncept A]]
- [[Koncept B]]

## Učni Sklopi

### Sklop 1: [Ime] (Dnevi 1–3)
- Vir: [[VIR]]
- Koncepti: [[K1]], [[K2]]
- Mini projekt: [[Projekt - X]]

### Sklop 2: [Ime] (Dnevi 4–7)
...

## Self-test (konec vsakega sklopa)
- Vprašanje 1
- Vprašanje 2

## Refleksija
→ [[Refleksija - DATUM]]
```

## Dober Plan vs. Slab Plan

| Dober | Slab |
|-------|------|
| Jasen cilj + dokaz znanja | "Bom se naučil Python" |
| Časovni okvir | Odprt konec |
| Vrstni red konceptov | Naključni skoki |
| Mini projekti za vsak sklop | Samo teorija |
| Tedenski review | Brez refleksije |

## Integracija v Vault

- Vsak Study Plan linka na [[Skill Tree]] za to področje
- Vsak sklop linka na concept note
- Na koncu naredi [[Refleksija]]
- Projekt gre v `06_LEARNING/Projects/`

## Povezave

- [[Solo Ucenje]] — metodologija za katero je plan
- [[Skill Tree]] — vizualizacija napredka
- [[Refleksija]] — tedenski pregled plana
- [[Aktivni Priklic]] — integrira v vsak sklop
- [[06_LEARNING/Learning Hub|Learning Hub]] — kje živijo plani

---

## Viri

- [[Solo Ucenje]]
- [[07_AI/AI Prompti|AI Prompti]] — prompt za generiranje plana

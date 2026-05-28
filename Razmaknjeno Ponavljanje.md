---
categories:
  - "[[Evergreen]]"
created: 2026-05-25
rating: 5
tags:
  - 0🌲
related-to:
  - "[[Solo Ucenje]]"
  - "[[Aktivni Priklic]]"
  - "[[Feynmanova Tehnika]]"
---

# Razmaknjeno Ponavljanje

Razmaknjeno ponavljanje (angl. *spaced repetition*) je tehnika, ki izkorišča **krivuljo pozabljanja** — dejstvo, da pozabimo večino v prvih 24 urah, ampak vsako ponovitev "resetira" in podaljša zapomnitev.

## Kako Deluje

Hermann Ebbinghaus je odkril, da je pozabljanje eksponentno. Rešitev: ponoviš tik preden pozabiš.

```
1. dan:     Naučiš se koncepta
3. dan:     Prva ponovitev
7. dan:     Druga ponovitev
14. dan:    Tretja ponovitev
30. dan:    Četrta ponovitev
90. dan:    Peta ponovitev
```

Vsaka uspešna ponovitev → interval se podaljša. Neuspešna → resetira.

## Implementacija v Obsidianu

**Opcija 1: Obsidian Spaced Repetition Plugin**
- Inštaliraj plugin "Spaced Repetition"
- V note dodaj inline flashcards:

```markdown
Kaj je moment sile? :: Produkt sile in ročice M = F·d
```

- Plugin sam določi, kdaj naj ponavljaš

**Opcija 2: Ročni Sistem (brez plugina)**
V vsak [[Concept note]] dodaj frontmatter:
```yaml
review-date: 2026-05-28
review-interval: 3
```

Ko ponavljaš, posodobi datum in podvoji interval.

**Opcija 3: Anki**
Izvozi flashcards iz Obsidiana v [[Anki]] — specializirano orodje za spaced repetition.

## Kaj Dati v Ponovitve

✓ Definicije konceptov
✓ Formule in enačbe
✓ Ključne datume ali dejstva
✓ Vzorci in mehanizmi

✗ Celotni odstavki besedila
✗ Kompleksne razlage (te gredo v [[Feynmanova Tehnika]])

## Kdaj Nima Smisla

Razmaknjeno ponavljanje je za **dejstva in definicije**. Za globoko razumevanje konceptov potrebuješ [[Feynmanova Tehnika]] in [[Aktivni Priklic]].

## Povezave

- [[Solo Ucenje]] — celoten učni sistem
- [[Aktivni Priklic]] — komplementarna tehnika
- [[Feynmanova Tehnika]] — za razumevanje, ne samo zapomnitev
- [[Study Plan]] — kdaj vključiti ponovitve v plan

---

## Viri

- [[Solo Ucenje]]
- Hermann Ebbinghaus: *Über das Gedächtnis* (1885)

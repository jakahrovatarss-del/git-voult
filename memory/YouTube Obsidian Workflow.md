# YouTube → Obsidian Note Workflow

## Kontekst
Jaka pošlje YouTube link. Jaz potegnem transkripcijo (ali povzetek iz videa), jo obdelam in ustvarim strukturirano Obsidian noto.

## Jezik
Vedno slovenščina. Strokovni termini ostanejo v angleščini (peptidi, tehnika, itd.).

---

## Korak 1 — Potegni vsebino videa

Uporabi `mcp__workspace__web_fetch` ali WebSearch za:
- Naslov videa
- Avtorja / kanal
- Temo (o čem je video)
- Transkripcijo ali opis (YouTube auto-generated captions, opis, komentarji)

Če transkripcija ni dostopna → povzemi iz naslova, opisa in znanja o temi.

---

## Korak 2 — Določi tip note

Glede na vsebino videa izberi tip:

| Vsebina videa | Tip note | Mapa | Ime |
|---|---|---|---|
| Vir / referenca (video o temi) | `Vir - ...` | `04_RESOURCES/` | `Vir - [Naslov Videa].md` |
| Šolska snov / predavanje | `Koncept - ...` | `05_SCHOOL/Zapiski/` | `Koncept - [Ime].md` |
| Solo učenje / biohacking / tech | `Tema - ...` ali `Koncept - ...` | `06_LEARNING/Teme/` | `Tema - [Ime].md` ali `Koncept - [Ime].md` |
| Povzetek za skill tree | `Vir - ...` | `06_LEARNING/Summaries/` | `Vir - [Naslov].md` |

**Privzeto**: večina videov gre v `04_RESOURCES/` kot `Vir - [Naslov].md`.

---

## Korak 3 — Struktura note (Vir - Template)

```markdown
---
title: Vir - [Naslov Videa]
type: resource
category: [tema npr. peptide-protocols / biohacking / engineering]
source: youtube
url: [YouTube URL]
avtor: [Kanal / Avtor]
created: YYYY-MM-DD
---

# Vir - [Naslov Videa]

## Osnovni Podatki
**Avtor**: [Kanal]
**Tema**: [O čem je video]
**Format**: YouTube video ([X] min)
**URL**: [link]

---

## Ključni Zaključek
> En stavek — glavna poanta videa.

---

## Glavne Točke
[Strukturirano po sekcijah — enako kot obstoječe Vir note v 04_RESOURCES/]

---

## Actionable Ideje
- 
- 

## Opozorila / Napake (če relevantno)
- 

## Povezave
[[Tema / Koncept / Projekt ki je soroden]] | [[drugi sorodni]] | [[Hub note]]
```

---

## Korak 4 — Obvezna pravila

1. **Vsaj 2 wikilinks** na obstoječe note v vaultu.
2. **Nikoli orphan note** — vedno linki na hub ali temo.
3. **Sekcija `Povezave`** je obvezna.
4. **Frontmatter** vedno z `title`, `type`, `source: youtube`, `url`, `created`.
5. Pred shranjevanjem **vprašaj Jako**: "Shranim kot `[predlagana pot]`?"

---

## Korak 5 — Preveri obstoječe note

Preden ustvariš novo noto, preveri:
- `04_RESOURCES/` — ali že obstaja podoben Vir?
- `06_LEARNING/Teme/` — ali tema že obstaja?
- Če obstaja → **dopolni obstoječo**, ne ustvari duplikata.

---

## Primeri obstoječih Video not (za stil reference)

- `04_RESOURCES/Vir - GHK-Cu Protokol Video.md` — peptide video, detajlna struktura z napakami, protokoli, opozorili
- `04_RESOURCES/Vir - Peptide Protokoli Video Transkripcija.md` — multi-peptide video, strukturiran po peptidih

Oba imata: Osnovni Podatki → Ključni Zaključek → Sekcije po vsebini → Povezave.

---

## Povpraševanje ob koncu

Na koncu vsakega odgovora ponudi:

> **Shranim noto?**
> Predlog: `04_RESOURCES/Vir - [Naslov].md`
> Linki: `[[...]]`, `[[...]]`

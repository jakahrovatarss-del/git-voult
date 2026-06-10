# YouTube → Obsidian Note Workflow

## Jezik
Slovenščina. Strokovni termini v angleščini.

---

## NAJPREJ: Preveri vault

Preden karkoli ustvariš, poišči obstoječe note:
```bash
ls /sessions/.../mnt/obsidian/ | grep -i "[ključna beseda]"
```
Če nota že obstaja → **preberi jo in dopolni z novimi informacijami iz videa**. Nikoli duplikatov, nikoli nova nota za isto temo.

### Obstoječe note v root vaulta (junij 2026)
Agartha, Akceleranizem, Aktivni Priklic, Antisemitizem, Aromatase Inhibitor, Astralna projekcija, BPC-157, Beta-karoten, CJC-1295, Civilizacijski cikel, Clean Aesthetic Protocol, Curtis yarvin, Dnevnik sanj, Drža, EQ, Elon Musk, Feynmanova Tehnika, Frierdrich Thiel, GHK-Cu, Geopolitika - Civilizacijski Kolaps, Geopolitika - Velike Moci - Noi, Google Dorking, GrapheneOS, HCG, HPTA, HUMINT, Holokavst, Homo Sedatus, Injectable Glutathione, Ipamorelin, Kolagen in elastičnost, Lucidno sanjanje, MK-677, Masteron, Melanotan 2, Muhammad bin Salman, NAC, NEON, Namibija, Nasdaq, OPSEC, OSINT, Open AI, Ostarine, PCT, Peptidi, Peter Teal, Praxis- pametno mesto, Primobolan, Projekt - PLFM RADAR, Prosper City, Qubes OS, Razmaknjeno Ponavljanje, Retatrutide, Rothchilds, Saudska Arabija, Sherlock, Skill Tree, Solo Ucenje, SpaceX, Starlink, Study Plan, TB-500, TUDCA, Testosteron Enanthate, Tor Browser, Von Ungern-Sternberg, Von Ungern-Sternberg - Šambala in akceleranizem, Wayback Machine, Šambala, donald trump 2024 predcedništvo, mehanika, podjetna mesta, pronomos capital, xAI ...

---

## Dva tipa not

### Tip A — Hub poročilo (za video kot celoto)
Ime: `Tema - podnaslov.md` ali `ImeTeme.md`
Lokacija: root vault
Frontmatter:
```yaml
---
created: YYYY-MM-DD
tags:
  - note
  - journal
source: [URL]
---
```
Struktura:
```
# Uvod
# Struktura teme  ← seznam vej z [[WikiLinki]]
# [Sekcija 1]
# [Sekcija 2]
# ...
# Zaključek
# Viri
```

### Tip B — Konceptna opomba (za vsak nov koncept iz videa)
Ime: `ImKoncepta.md`
Lokacija: root vault (večina not je tam)
Frontmatter:
```yaml
---
categories:
  - "[[Koncepti]]"
created: YYYY-MM-DD
---
```
Struktura:
```
# Kaj je
[1-3 stavki]

# [Funkcionalna sekcija]
[kratko, modularno]

# Viri / Povezano
[[Hub poročilo]]
[[Sorodni koncepti]]
```

**Pravilo:** Konceptna opomba = en koncept. Če postane dolga → razbiješ na dva.

---

## Postopek za YouTube video

1. **Potegni transkripcijo**: `https://youtubetotranscript.com/transcript?v=[VIDEO_ID]`
2. **Preveri vault** — kaj od tega že obstaja?
3. **Ustvari hub poročilo** z vsebino videa
4. **Identificiraj nove koncepte** → kratke konceptne opombe
5. **Vzpostavi WikiLinke**: hub ↔ koncepti ↔ obstoječe note
6. **Vprašaj pred shranjevanjem**: "Shranim? Predlog: `ImeNote.md`"

---

## Pravila stila

- Kratko, modularno, z lastnimi besedami — nikoli copy-paste
- Sekcija `# Povezano` ali `# Viri` je obvezna
- Vsaj 2 WikiLinka na obstoječe note
- Nikoli orphan note
- Brez emoji v notah
- Brez samodejnega shranjevanja — vedno vprašaj najprej

---

## Pravilo: Maksimalni wikilinki

**Vedno poveži z VSEM relevantnim v vaultu** — ne le z očitnimi note. Preden zaključiš, premisli:
- Katera obstoječa nota ima sorodno temo? (anche indirektno)
- Ali se nova nota dotika iste osebe, koncepta, ali tradicije kot obstoječa nota?
- Ali obstaja vzporednica ki jo wikilink razkrije?

Cilj: vsaka nova nota ima vsaj 5+ wikilinkov navzven.

---

## Note dodane junij 2026

Iz videa "Do You Want Civilization To Collapse?" (fJoOKZ7pgUM):
- Homo Sedatus

Iz videa "Did CERN Try to Destroy the Earth?" (UuYcpI6MX5o):
- CERN - Ali smo poskusili uničiti Zemljo (hub)
- CERN, Kvantna nesmrtnost, Dvojna reža, Brahman in Maya, Singularnost

Iz videa "They Want To Live Forever In The Black Cube" (3pBYk3gCFm8):
- Simulated Leviathan - Črna Kocka in Nesmrtnost (hub)
- Kult Kronosa, Saturn - Simbolizem, Tikkun Olam, Gnosticizem in Demiurg, Črna Kocka, Simulacijska teorija
- Dopolnjene: Jeffrey Epstein, Singularnost, Brahman in Maya, Akceleranizem, CERN

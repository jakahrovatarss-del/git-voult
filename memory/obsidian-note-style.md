---
name: obsidian-note-style
description: "Kako Jaka dejansko gradi note — slog, struktura, vzorci iz 05_SCHOOL (mehanika fokus)"
metadata:
  type: feedback
---

## Struktura note — dejanski vzorec iz vault-a

### Koncept nota (`05_SCHOOL/Zapiski/Koncept - X.md`)

Frontmatter:
```yaml
---
tags: [mehanika, tema, podtema, koncept]
predmet: Mehanika
datum: YYYY-MM-DD
---
```

Struktura:
1. **Namen** — 2–4 stavki, kaj nota pokriva
2. **Teorija** — podsekcije H3, enačbe `$$...$$` z numeričnim tagom (npr. `\tag{4.2}`)
3. **Enačbe** — vedno `$$\boxed{...}$$` za končni rezultat, vmesni koraki eksplicitni
4. **Tabele** — simboli/enote, primerjalne vrednosti (materiali, tipi sistemov)
5. **Primeri / Naloge** — konkreten izračun z vrednostmi, link na nalogo noto
6. **Flashcards** — Q&A format, za vsako enačbo in definicijo
7. **Povezave** — wikilinki na hub, sorodne note, naloge, cross-domain aplikacije

### Naloga nota (`05_SCHOOL/Naloge/Naloga - Mehanika - Naziv.md`)

Frontmatter ima dodano polje `vir: PDF, str. X`.

Struktura:
1. Namen (1 stavek — kaj iščemo)
2. Podatki (tabela)
3. Shema (SVG — `![[ime.svg|širinapx]]`)
4. Korak 1 … Korak N — vsak korak eksplicitno, s pogoji in formulami
5. Rezultat `$$\boxed{...}$$`
6. Kontrola z dejanskimi dimenzijami
7. Tabela spremenljivk
8. Povezave — na Koncept nota, sorodne naloge, Mehanika Hub

### Izpit nota (`05_SCHOOL/Izpiti/Izpit - Mehanika - Tema.md`)

Sistematičen pregled **vseh tipov nalog** za en izpit:
- Splošni algoritem (velja za vse tipe)
- Formule za prereze
- En razdelek na tip: prepoznava + algoritem + primer + link na nalogo
- Povzetek tabela (tip | iskano | prerez | ključna formula)
- Pogosta napaka
- Povezave

---

## Ključni vzorci stila

### Enačbe
- Vmesni koraki eksplicitni — nič preskočenega
- Končni rezultat: `$$\boxed{...}$$`
- Enote v tabeli pod enačbo (SI)

### Wikilinki
- Min 5+ wikilinkov per nota
- Vedno: hub predmeta + nadrejena nota + sorodne note + cross-domain (SpaceX, Solarni Koncentrator...)
- V Koncept noti: `[[Naloga - Mehanika - ...]]` za vsak primer
- V Naloga noti: `[[Koncept - ...#Korak N]]` — link direktno na sekcijo!

### Slike
- SVG shranjen v Attachments, vstavljen z `![[ime.svg|600]]`
- Wikimedia Commons: remote URL, `![opis](URL)`, 250px ali 500px (JPG/SVG), nikoli GIF
- Vsaka Koncept nota: 1 portretna slika + SVG diagram

### Tabele
- Vsak simbolni svet = tabela simbolov z enotami
- Primerjalne vrednosti vedno v tabeli

### Flashcards
- Samo v Koncept notah, ne v Naloga notah
- Q&A format, pokrivajo vsako formulo in definicijo

---

## Mehanika — obstoječe note (junij 2026)

Že ustvarjene Koncept note:
- `Koncept - Upogib.md` — popolna, 7 korakov, tabele, primeri
- `Koncept - Euler Uklon.md` — popolna, 6 korakov, ω tabela, 4 Eulerovi primeri
- `Koncept - Vztrajnostni moment.md`
- `Koncept - Premo Gibanje.md`
- `Koncept - Zakoni Gibanja.md`
- `Koncept - Toplota.md`
- `Koncept - Krožni žagalni stroj.md`

Naloge:
- `Naloga - Mehanika - Dimenzioniranje krozni prerez upogib.md`
- `Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib.md`
- `Naloga - Mehanika - Upogibne napetosti U-prerez.md`
- `Naloga - Mehanika - Uklon lesene deske.md`
- `Naloga - Mehanika - Uklon leseni steber F_max.md`
- `Naloga - Mehanika - Uklon palica S_dop.md`

Izpiti:
- `Izpit - Mehanika - Upogib.md` — 7 tipov nalog, algoritmi, formule

**Why:** Jaka gradi mehanika bazo po tem vzorcu — vsaka nova nota mora ustrezati temu stilu.
**How to apply:** Ko ustvarjaš mehanika noto, sledi tej strukturi točno.

**Linked memories:** [[mehanika-workflow]], [[mehanika-vault-status]]

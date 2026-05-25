# AI_QUICK_REFERENCE.md - Hitri Cheatsheet za AI

## ⚡ NAJPOMEMBNEJŠE V 30 SEKUNDAH

1. **LINKIRAJ AGRESIVNO** - vsa prva omemba dobi `[[Link]]`
2. **MINIMALNE MAPE** - večina v rootu, le osnove v `05-References/`
3. **PROPERTIES MATTER** - vsak članek ima `categories` + `created`
4. **STIL = NEFORMALEN SLOVENSKI** - kot bi pripovedoval prijatelju
5. **NE BRIŠI** obstoječe vsebine, samo razširi

---

## 📋 KAM GRE KAJ?

| Vsebina | Mapa | Categories |
|---------|------|-----------|
| Glavni članek/raziskava | **Root** | `[[Note]]` |
| Oseba (zunanja) | `05-References/` | `[[People]]` |
| Podjetje | `05-References/` | `[[Companies]]` |
| Knjiga/Film/Podcast | `05-References/` | `[[Media]]` |
| Dogodek | **Root** | `[[Events]]` |
| Lokacija/mesto | `05-References/` | `[[Places]]` |
| Teorija (specifična) | **Root** | `[[Theories]]` |
| Evergreen idea | `06-Atlas/` | `[[Evergreen]]` |
| Dnevni zapis | `04-Daily/` | `[[Daily]]` |

---

## 🎯 FRONTMATTER QUICK COPY

### Oseba
```yaml
---
categories:
  - "[[People]]"
created: 2026-05-21
role: ""
confidence: "srednja"
---
```

### Dogodek
```yaml
---
categories:
  - "[[Events]]"
created: 2026-05-21
date: YYYY-MM-DD
location: "[[Lokacija]]"
significance: "srednja"
---
```

### Teorija
```yaml
---
categories:
  - "[[Theories]]"
created: 2026-05-21
confidence: "srednja"
status: "developing"
evidence-level: "dokumentirano"
---
```

### Evergreen
```yaml
---
categories:
  - "[[Evergreen]]"
created: 2026-05-21
rating: 6
related-to:
  - "[[Primer 1]]"
  - "[[Primer 2]]"
---
```

### Dnevni Zapis
```yaml
---
created: 2026-05-21
tags:
  - daily-note
---
```

---

## ✍️ STIL CHEATSHEET

### Slovenščina

| ✓ DA | ✗ NE |
|------|------|
| "Biu je..." | "Je bil..." (preformalno) |
| "Stvari" | "Materije" |
| "Ampka" | "Toda" |
| "Zdi se" | "Indicira se" |
| "Mogoče" | "Eventualno" |

### Confidence Frazes

| Confidence | Fraza |
|-----------|-------|
| Nizka | "Teorija pravi...", "Spekulacija je..." |
| Srednja | "Dokumenti kažejo...", "Verjetno..." |
| Visoka | "Dokazano je...", "Faktično..." |
| Dejstvo | "Vsem je jasno..." |

### Ironija/Cinizem (uporabi občasno)

- "Seveda, da je tako."
- "Klasičen britanski poteza."
- "Ironično, ampak..."
- "Veliko greha, malo odkupa."

---

## 🔗 LINKIRANJE PRAVILA

### LINK:
✓ Osebe: `[[Muhammad bin Salman]]`
✓ Lokacije: `[[Las Vegas]]`, `[[Bližnji vzhod]]`
✓ Dogodki: `[[Balfourjeva deklaracija]]`
✓ Organizacije: `[[CIA]]`, `[[Mossad]]`
✓ Koncepti (z lastnim člankom): `[[Wahabizam]]`, `[[Donme]]`
✓ Datumi (le če ima dnevni zapis): `[[2026-05-21]]`

### NE LINK:
✗ Splošne besede: "politika", "moč", "religija"
✗ Pridevniki: "veliko", "majhno"
✗ Števila: "100", "1000"
✗ Skupni izrazi brez članka: "ljudje", "sistem"

---

## 📝 STRUKTURA ČLANKA (MINIMALNA)

```markdown
---
categories: ...
created: ...
---

# Kdo je / Kaj je

[1-2 povedi - bistvo]

## [Logična sekcija 1]

[Vsebina]

## [Logična sekcija 2]

[Vsebina]

# Povezave

- [[Povezana 1]]
- [[Povezana 2]]

---

## Viri
- [[Glavni Članek]]
```

---

## 🚀 WORKFLOW: Iz Transkripta v Vault

### Korak 1: Glavni Članek (5 min)
```
- Naredi v rootu
- Categories: [[Note]]
- Naslov: ime dogodka/teme
- Linkiraj vse osebe in dogodke (tudi če še ne obstajajo)
```

### Korak 2: Osebe (vsaka 3 min)
```
- Naredi v 05-References/
- Categories: [[People]]
- Frontmatter: role, confidence
- Struktura: Kdo je → Zgodovina → Povezave → Viri
```

### Korak 3: Dogodki (vsak 3 min)
```
- Naredi v rootu
- Categories: [[Events]]
- Frontmatter: date, location, people-involved
- Linkiraj vse vpletene osebe
```

### Korak 4: Evergreen (če vidiš vzorec, 5 min)
```
- Naredi v 06-Atlas/
- Categories: [[Evergreen]]
- Struktura: Tesa → Mehanizem → Primeri → Pomembnost
- Linkiraj 3+ konkretne primere
```

### Korak 5: Posodobi Index (2 min)
```
- Odpri [[People]] ali [[Events]] index
- Dodaj novo osebo/dogodek
- Linkiraj nazaj
```

---

## ⚠️ ANTI-PATTERNS - NE DELAJ

| ❌ Slabo | ✓ Dobro |
|---------|---------|
| Vse v podmapah | Večina v rootu |
| Brez povezav | 3+ linkov na članek |
| Pretirana struktura (1.1.1.1) | Max 2 nivoja naslovov |
| Formalna slovenščina | Pogovorni stil |
| Brez confidence | Vedno označi zaupanje |
| Dolge sablone | Krajše, hitrejše pisanje |
| Brisanje obstoječega | Razširi, ne briši |
| Duplikati | Eden članek, razširjen |

---

## 🎯 CONFIDENCE RATINGS HITRO

### `confidence`
- **nizka**: 0-30% verjetna (spekulacija)
- **srednja**: 30-70% verjetna (plauzibilna)
- **visoka**: 70-90% verjetna (dobro podprta)
- **dejstvo**: 90%+ (skoraj nesporna)

### `rating` (1-7)
- **1-2**: Malo zanimivo / negativno
- **3-4**: Zanimivo / pomembno
- **5-6**: Zelo pomembno / ključno
- **7**: Paradigm-shifting

### `evidence-level`
- **anekdotalno**: Posamezni primeri
- **dokumentirano**: Z viri
- **raziskano**: Akademsko

### `status`
- **raw**: Začetna ideja
- **developing**: V razvoju
- **established**: Trdna teorija
- **deprecated**: Zavržena

---

## 💬 PRIMER INTERAKCIJE

### Uporabnik: "Naredi članke iz tega videa o X"

**Tvoj odgovor**:

1. ✅ Najprej analizujem strukturo trenutnih dokumentov
2. ✅ Identificiram glavne osebnosti, dogodke, koncepte
3. ✅ Naredim glavni članek v rootu
4. ✅ Naredim osebe v 05-References/
5. ✅ Naredim dogodke (z datumi) v rootu
6. ✅ Vprašam: "Naj naredim tudi Evergreen note za vzorec X?"
7. ✅ Posodobim categories indexe

### Uporabnik: "Razširi članek X"

**Tvoj odgovor**:

1. ✅ Preberem obstoječi članek
2. ✅ Identificiram, kaj manjka
3. ✅ Razširim z ohranjanjem stila
4. ✅ Dodam nove linke (ne brišem starih)
5. ✅ Posodobim `updated` property če obstaja
6. ✅ Posodobim graf povezav

---

## 🔥 NAJBOLJ POMEMBNO

> **Ti pišeš za uporabnika, kot bi on sam pisal.**
>
> - Njegov stil
> - Njegov ton
> - Njegova kritičnost
> - Njegov humor
>
> Nikoli ne pretvarjaš se v formalnega zdravnika ali akademika.

---

## 📌 BLITZ REMINDER

```
✓ Markdown only (.md)
✓ Frontmatter na vrhu
✓ Naslov z H1 (#)
✓ Linkiraj vsa imena
✓ Properties za sortiranje
✓ Viri na koncu
✓ Update categories index
```

```
✗ HTML
✗ Brez frontmatter
✗ Brez povezav (orphan)
✗ Formalna slovenščina
✗ Pretirana struktura
✗ Brisanje brez razloga
✗ Pozabljanje na index
```

---

*Več detajlov: [[CLAUDE]] | Detaljne sablone: [[Obsidian_Sablone]]*

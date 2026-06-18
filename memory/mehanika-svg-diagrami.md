---
name: mehanika-svg-diagrami
description: "SVG risanje mehanika diagramov — barvna paleta, struktura, vzorci, konvencije"
metadata:
  node_type: memory
  type: project
---

# SVG Diagrami — Mehanika

## Dva stila (tema)

### Temni stil (dark theme) — primerno za konceptne diagrame:
```svg
<svg viewBox="0 0 800 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Ozadje -->
  <rect width="800" height="520" fill="#1a1a2e"/>
  <!-- Paneli / sekcije -->
  <rect x="10" y="10" width="380" height="200" rx="8" fill="#0d1b2a" stroke="#1e3a5f" stroke-width="1.5"/>
```

### Svetli stil (light theme) — primerno za naloge, nosilci:
```svg
<svg viewBox="0 0 820 430" xmlns="http://www.w3.org/2000/svg">
  <!-- Ozadje belo -->
  <rect width="820" height="430" fill="#ffffff"/>
  <!-- Paneli -->
  <rect x="10" y="10" width="400" height="200" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
```

---

## Standardna barvna paleta

### Konstrukcijski elementi:
| Element | Barva | Hex |
|---------|-------|-----|
| Nosilec (temni) | Rumena | `#FFD700` |
| Nosilec (svetli) | Svetlo modra fill + modra stroke | `fill="#bfdbfe" stroke="#1d4ed8"` |
| Podpora (temni) | Svetlo modra | `#90CAF9` |
| Tla / hatching | Siva | `#94a3b8` |

### Sile in napetosti:
| Element | Barva | Hex |
|---------|-------|-----|
| Sila / obtežba | Oranžna | `#FF9800` |
| Tlak / kompresija | Rdeča | `#F44336` |
| Nateg / tenzija | Modra | `#2196F3` |
| Nevtralna os | Cyan dashed | `#00E5FF` |
| Pozitivni moment | Zelena | `#4CAF50` ali `#22c55e` |
| Negativni moment | Rdeča | `#EF4444` |
| Reakcija | Zelena | `#4CAF50` |
| Moment para | Vijolična | `#9C27B0` |

### Tekst:
- Temni stil: `fill="#e2e8f0"` (svetla)
- Svetli stil: `fill="#1e293b"` (temna)
- Oznake enačb: `fill="#94a3b8"` ali `fill="#64748b"`
- Formule / poudarjeno: `fill="#FFD700"` ali `fill="#f59e0b"`

---

## Puščice (arrowhead markers)

### Z defs/marker:
```svg
<defs>
  <marker id="arrow" markerWidth="10" markerHeight="7"
          refX="9" refY="3.5" orient="auto">
    <path d="M0,0 L0,7 L10,3.5 Z" fill="#FF9800"/>
  </marker>
  <!-- ali manjša -->
  <marker id="arrowSmall" markerWidth="7" markerHeight="7"
          refX="6" refY="3.5" orient="auto">
    <path d="M0,0 L7,3.5 L0,7 Z" fill="#FF9800"/>
  </marker>
</defs>
<!-- Uporaba -->
<line x1="100" y1="50" x2="200" y2="50" 
      stroke="#FF9800" stroke-width="2" marker-end="url(#arrow)"/>
```

### Za vsak element svoja barva → loči markerje po id:
```
id="arrowForce"   fill="#FF9800"
id="arrowReact"   fill="#4CAF50"
id="arrowMoment"  fill="#9C27B0"
```

---

## Podpore

### Vrtljiva podpora (pin / členkasta):
```svg
<!-- Trikotnik navzdol -->
<polygon points="200,300 185,325 215,325" 
         fill="#90CAF9" stroke="#60A5FA" stroke-width="1.5"/>
<!-- Tla - hatching linija -->
<line x1="175" y1="325" x2="225" y2="325" 
      stroke="#90CAF9" stroke-width="2"/>
<!-- Kratke šrafure -->
<line x1="180" y1="325" x2="175" y2="332" stroke="#60A5FA" stroke-width="1"/>
<line x1="190" y1="325" x2="185" y2="332" stroke="#60A5FA" stroke-width="1"/>
<line x1="200" y1="325" x2="195" y2="332" stroke="#60A5FA" stroke-width="1"/>
<line x1="210" y1="325" x2="205" y2="332" stroke="#60A5FA" stroke-width="1"/>
<line x1="220" y1="325" x2="215" y2="332" stroke="#60A5FA" stroke-width="1"/>
```

### Drsna podpora (roller):
```svg
<!-- Trikotnik + krog -->
<polygon points="400,300 385,325 415,325" fill="none" stroke="#90CAF9" stroke-width="1.5"/>
<circle cx="400" cy="330" r="4" fill="#90CAF9"/>
```

### Vpetje (cantilever):
```svg
<!-- Navpična črta + šrafure -->
<line x1="50" y1="280" x2="50" y2="380" stroke="#90CAF9" stroke-width="3"/>
<line x1="30" y1="280" x2="50" y2="280" stroke="#60A5FA" stroke-width="1"/>
<line x1="30" y1="295" x2="50" y2="295" stroke="#60A5FA" stroke-width="1"/>
<!-- ... -->
```

---

## M-diagram (upogibni moment)

### Bezier krivulja za parabolično obliko:
```svg
<!-- Kvadratna bezier: M x y Q cx cy x2 y2 -->
<path d="M 100 300 Q 300 150 500 300" 
      stroke="#4CAF50" stroke-width="2.5" fill="none"/>
<!-- Z zapolnjenim območjem -->
<path d="M 100 300 Q 300 150 500 300 L 500 300 L 100 300 Z" 
      fill="#4CAF50" fill-opacity="0.15" stroke="#4CAF50" stroke-width="2"/>
```

### Tipični M-diagrami:
- Enakomerna obtežba: parabola navzdol (pozitivni M) ali navzgor (negativni)
- Točkovna sila: trikotnik (linearna na levi, linearna na desni)
- Vpeti konec: skoči na M_reakcija, potem pade

---

## NTM diagrami — layout

```
Vodoravna os: x (0 → L)
N-diagram pod nosičem: + navzgor (nateg), − navzdol (tlak)
T-diagram pod N: + navzgor, − navzdol
M-diagram spodaj: + navzdol (sagging = pozitivno po konvenciji)
```

### Predznak M — konvencija:
- **Sagging** (q navzdol, upogib navzdol = vlakna spodaj v nategu) → **M > 0**
- **Hogging** (upogib navzgor = vlakna zgoraj v nategu) → **M < 0**

---

## Porazdeljeno breme

```svg
<!-- Enaka razdalja med puščicami -->
<line x1="150" y1="80" x2="150" y2="130" stroke="#FF9800" stroke-width="1.5" marker-end="url(#arrowForce)"/>
<line x1="200" y1="80" x2="200" y2="130" stroke="#FF9800" stroke-width="1.5" marker-end="url(#arrowForce)"/>
<line x1="250" y1="80" x2="250" y2="130" stroke="#FF9800" stroke-width="1.5" marker-end="url(#arrowForce)"/>
<!-- Vodoravna črta nad puščicami -->
<line x1="150" y1="80" x2="350" y2="80" stroke="#FF9800" stroke-width="1.5"/>
<!-- Oznaka q -->
<text x="360" y="85" fill="#FF9800" font-size="14">q</text>
```

---

## Tekst in oznake

```svg
<!-- Naslovi -->
<text x="400" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#e2e8f0">
  N, T, M Diagrami
</text>
<!-- Enačbe -->
<text x="50" y="100" font-size="13" fill="#94a3b8" font-family="monospace">
  σ = M·e/J
</text>
<!-- Oznake točk -->
<text x="198" y="295" font-size="12" fill="#90CAF9">A</text>
```

---

## viewBox priporočila

| Vsebina | viewBox |
|---------|---------|
| En diagram | `0 0 600 400` |
| Dva diagrama vzporedno | `0 0 800 450` |
| Tri/štiri diagrami | `0 0 860 620` |
| Nosič + NTM diagrami | `0 0 820 500` |
| Conceptual full-page | `0 0 900 700` |

---

## Checklist za vsak SVG

- [ ] viewBox definiran
- [ ] xmlns="http://www.w3.org/2000/svg"
- [ ] Ozadje (`<rect width="..." height="..." fill="..."/>`)
- [ ] `<defs>` z markerji za puščice (pred vsemi elementi)
- [ ] Vse puščice imajo `marker-end="url(#id)"`
- [ ] Podpore: trikotnik + hatching
- [ ] Tekst berljiv (kontrastna barva glede na ozadje)
- [ ] Oznake dimenzij in sil
- [ ] Nevtralna os = dashed cyan `stroke-dasharray="5,4"`

**Linked memories:** [[mehanika-vault-status]], [[mehanika-reševanje-nalog]]

---
tags:
  - daily
predmet: mehanika
profesor: un kurac
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

# [[STATIKA]]



[[Statika-enačbe statičnega ravnovesja, osnovni principi statike,redukcija sistema sil.]]










# VIRI
[[arne mehanika strojništvo.pdf]]







## Notes

![[Daily.base]]

---

# Fizika — Kinematika in Dinamika (BF UNI 2025)

> Dopolnjeno iz Skripta-FIzika-BFUNI-2025.pdf, Poglavja 2–4

## Premo gibanje — ključne enačbe

| Enačba | Pomen |
|--------|-------|
| $\Delta x = x_2 - x_1$ | premik |
| $v = dx/dt$ | trenutna hitrost (odvod lege) |
| $a = dv/dt$ | trenutni pospešek (odvod hitrosti) |
| $v(t) = v_0 + at$ | hitrost pri EPG |
| $x(t) = x_0 + v_0 t + \frac{1}{2}at^2$ | lega pri EPG |
| $v^2 = v_0^2 + 2a\Delta x$ | EPG brez časa |

Prosti pad: $g = 9{,}81\ \text{m/s}^2$, $y_{max} = v_{0y}^2 / (2g)$

→ Podrobno: [[Koncept - Premo Gibanje]]

## Newtonovi zakoni

1. $\sum \vec{F} = 0 \iff \vec{v} = \text{konst.}$ (vztrajnost)
2. $\sum \vec{F} = m\vec{a}$ (osnovna enačba gibanja)
3. $\vec{F}_{12} = -\vec{F}_{21}$ (akcija = reakcija)

Gravitacija: $F_g = G m_1 m_2 / r^2$, blizu Zemlje: $F_g = mg$

Trenje: $F_s \leq \mu_s F_n$ (statično), $F_t = \mu_t F_n$ (kinetično)

Klanec ($\varphi$): $a = g(\sin\varphi - \mu_t \cos\varphi)$

→ Podrobno: [[Koncept - Zakoni Gibanja]] | [[STATIKA]] | [[ravnovesje delca]]
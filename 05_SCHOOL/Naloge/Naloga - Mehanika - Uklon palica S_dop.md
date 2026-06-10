---
tags: [mehanika, uklon, euler, jeklo, palica, naloga]
predmet: Mehanika
datum: 2026-06-10
vir: IMG_1241.pdf, str. 21, naloga 2
---

# Naloga: Dopustna sila S za palico (1) v konstrukciji (uklon)

## Namen

Poiskati maksimalno zunanjo silo S, da se jeklena I-palica (1) v triangularni konstrukciji še ne ukloni.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| E | 21000 kN/cm² | modul elastičnosti (jeklo) |
| ν | 3 | uklonska varnost |
| σ_dop | 16 kN/cm² | dopustna napetost (jeklo) |
| Vpetje | obe strani členkasto | β = 1 |
| Razpon | 3 m | horizontalna razdalja med podporama |
| Kot palice | 45° | palica (1) je diagonala |

## Konstrukcija

![[uklon_palica_Sdop.svg]]

Triangularna konstrukcija:
- **A** = spodaj-levo (členkasta podpora)
- **B** = spodaj-desno (členkasta podpora)
- **C** = zgoraj-desno (vozlišče, sila S vodoravno)
- **Palica (1)** = diagonala AC, 45°, dolžina L = 3√2 m

## Korak 1 — Ravnotežje (notranja sila v palici 1)

Sila S deluje vodoravno v vozlišču C. Ravnotežje horizontalnih sil:

$$\sum F_x = 0: \quad -S + N_1 \cdot \cos(45°) = 0$$

$$\boxed{N_1 = \frac{S}{\cos 45°} = S\sqrt{2}}$$

> Palica (1) je **tlačno** obremenjena s silo $N_1 = S\sqrt{2}$.

## Korak 2 — Lastnosti I-prereza

Prerez: **B = 8 cm**, **H = 12 cm**, **t_f = 1 cm**, **t_w = 1 cm** (h_stojine = 10 cm)

$$A = 2 \cdot B \cdot t_f + h_w \cdot t_w = 2 \cdot 8 \cdot 1 + 10 \cdot 1 = \mathbf{26 \text{ cm}^2}$$

**Minimalni vztrajnostni moment** (šibka os y):

$$I_{min} = I_y = 2 \cdot \frac{t_f \cdot B^3}{12} + \frac{h_w \cdot t_w^3}{12} = 2 \cdot \frac{1 \cdot 8^3}{12} + \frac{10 \cdot 1}{12}$$

$$= 85{,}33 + 0{,}83 = \mathbf{86{,}17 \text{ cm}^4}$$

## Korak 3 — Dolžina in vitkost

$$L = 3\sqrt{2}\ \text{m} = 424{,}26\ \text{cm}, \quad \beta = 1, \quad l_u = 424{,}26\ \text{cm}$$

$$i = \sqrt{\frac{I_{min}}{A}} = \sqrt{\frac{86{,}17}{26}} = 1{,}820\ \text{cm}$$

$$\lambda = \frac{l_u}{i} = \frac{424{,}26}{1{,}820} = 233 \quad > \quad \lambda_e \approx 114 \quad \Rightarrow \text{ Euler velja ✓}$$

*(Za jeklo: $\lambda_e = \pi\sqrt{E/\sigma_{dop}} = \pi\sqrt{21000/16} \approx 114$)*

## Korak 4 — Eulerjeva kritična sila

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2} = \frac{9{,}870 \cdot 21000 \cdot 86{,}17}{424{,}26^2} = \frac{17{.}868{.}000}{180{.}000} = \boxed{99{,}3\ \text{kN}}$$

## Korak 5 — Dopustna sila v palici

$$F_{dop} = \frac{F_k}{\nu} = \frac{99{,}3}{3} = 33{,}1\ \text{kN}$$

## Korak 6 — Dopustna zunanja sila S

Pogoj: $N_1 = S \cdot \sqrt{2} \leq F_{dop}$

$$S_{dop} = \frac{F_{dop}}{\sqrt{2}} = \frac{33{,}1}{1{,}414}$$

$$\boxed{\boxed{S_{dop} = 23{,}4\ \text{kN}}}$$

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| L | 424,26 cm | dolžina palice (3√2 m) |
| β | 1 | uklonski faktor (obe strani členek) |
| l_u | 424,26 cm | uklonska dolžina |
| A | 26 cm² | površina prereza |
| I_min | 86,17 cm⁴ | min. vztrajnostni moment (šibka os) |
| i | 1,820 cm | vztrajnostni polmer |
| λ | 233 | vitkost |
| F_k | 99,3 kN | Eulerjeva kritična sila |
| F_dop | 33,1 kN | dopustna sila v palici |
| N₁ | S√2 | notranja tlačna sila (iz ravnotežja) |
| **S_dop** | **23,4 kN** | **iskana dopustna zunanja sila** |

## Povezave

- [[Koncept - Euler Uklon]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Uklon leseni steber F_max]]
- [[mehanika]]
- [[Mehanika Hub]]

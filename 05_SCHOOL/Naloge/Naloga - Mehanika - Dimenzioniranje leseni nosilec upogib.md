---
tags: [mehanika, upogib, dimenzioniranje, les, naloga]
predmet: Mehanika
datum: 2026-06-11
vir: IMG_1241.pdf, str. 3 in str. 6
---

# Naloga: Dimenzioniranje lesenega nosilca na upogib

## Namen

Določiti dimenzije pravokotnega lesenega prereza ($a \times b$) previsnega nosilca, obremenjenega z enakomerno obtežbo na konzolnem delu.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| q | 5 kN/m | enakomerna obtežba |
| L_AB | 3 m | razpon med podporama |
| L_BC | 2 m | konzolni del (previs) |
| σ_dop | 1,0 kN/cm² | dopustna napetost (les) |
| a | 3x | širina prereza |
| b | 5x | višina prereza |

## Shema konstrukcije

![[upogib_lesen_nosilec.svg|637]]

- **A** = členkasta podpora (levo)
- **B** = členkasta podpora (desno, pri x=3m)
- **C** = prosti konec konzole (pri x=5m)
- Obtežba q = 5 kN/m deluje le na konzolnem delu B–C

## Korak 1 — Največji upogibni moment

Največji moment nastopi pri podpori **B** (vpetje konzole):

$$M_{max} = \frac{q \cdot L_{BC}^2}{2} = \frac{5 \cdot 2^2}{2} = \mathbf{10\ \text{kNm}} = 1000\ \text{kNcm}$$

> Moment je negativen (konzola se uklanja navzdol pri B), za dimenzioniranje vzamemo absolutno vrednost.

## Korak 2 — Vztrajnostni moment prereza

Prerez: širina $a = 3x$, višina $b = 5x$:

$$I_x = \frac{a \cdot b^3}{12} = \frac{3x \cdot (5x)^3}{12} = \frac{3x \cdot 125x^3}{12} = \frac{375x^4}{12} = 31{,}25x^4\ \text{cm}^4$$

## Korak 3 — Odpornostni moment prereza

Razdalja od nevtralne osi do skrajnega vlakna: $e = b/2 = 2{,}5x$

$$W_x = \frac{I_x}{e} = \frac{31{,}25x^4}{2{,}5x} = 12{,}5x^3\ \text{cm}^3$$

## Korak 4 — Pogoj dopustne napetosti

$$\sigma = \frac{M_{max}}{W_x} \leq \sigma_{dop}$$

$$1{,}0 = \frac{1000}{12{,}5x^3}$$

$$x^3 = \frac{1000}{1{,}0 \cdot 12{,}5} = 80\ \text{cm}^3$$

$$\boxed{x = \sqrt[3]{80} = 4{,}31\ \text{cm}}$$

## Korak 5 — Dimenzije prereza

$$a = 3x = 3 \cdot 4{,}31 = 12{,}93\ \text{cm} \approx \mathbf{13\ \text{cm}}$$

$$b = 5x = 5 \cdot 4{,}31 = 21{,}55\ \text{cm} \approx \mathbf{22\ \text{cm}}$$

$$\boxed{\boxed{a \times b = 13 \times 22\ \text{cm}}}$$

## Korak 6 — Kontrola

Dejanski odpornostni moment z zaokroženimi dimenzijami:

$$W_{dej} = \frac{a \cdot b^2}{6} = \frac{13 \cdot 22^2}{6} = \frac{13 \cdot 484}{6} = \frac{6292}{6} = 1048{,}7\ \text{cm}^3$$

$$\sigma_{dej} = \frac{M_{max}}{W_{dej}} = \frac{1000}{1048{,}7} = 0{,}953\ \text{kN/cm}^2 < 1{,}0\ \text{kN/cm}^2\ ✓$$

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| q | 5 kN/m | obtežba |
| L_BC | 2 m | konzolna dolžina |
| M_max | 10 kNm = 1000 kNcm | max. upogibni moment |
| I_x | 31,25x⁴ cm⁴ | vztrajnostni moment prereza |
| W_x | 12,5x³ cm³ | odpornostni moment |
| e | 2,5x cm | razdalja skrajnega vlakna od NO |
| x | 4,31 cm | osnovna dimenzija |
| **a × b** | **13 × 22 cm** | **rezultat** |
| σ_dej | 0,953 kN/cm² | dejanska napetost (< σ_dop ✓) |

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[mehanika]]
- [[Mehanika Hub]]

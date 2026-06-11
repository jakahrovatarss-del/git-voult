---
tags: [mehanika, upogib, napetosti, U-prerez, Steiner, naloga]
predmet: Mehanika
datum: 2026-06-11
vir: IMG_1241.pdf, str. 9 (naloga 2), rešitev str. 11
---

# Naloga: Ekstremne upogibne napetosti za U-prerez

## Namen

Izračunati mesta in velikosti ekstremnih upogibnih napetosti v previsnem nosilcu z U-profilom. Narisati diagram upogibnih momentov.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| F | 10 kN | točkovna sila na koncu previsa |
| q | 16 kN/m | enakomerna obtežba v polju |
| L_previs | 1 m | dolžina previsa (levo od A) |
| L_AB | 2,5 m | razpon med podporama A-B |
| B | 40 cm | zunanja širina U-profila |
| H | 15 cm | višina U-profila |
| t | 7 cm | debelina sten in pasnice |

## Shema

![[upogib_U_prerez_napetosti.svg|637]]

## Korak 1 — Reakcije

Izhodišče na levem prostem koncu (x=0), A pri x=1m, B pri x=3,5m.

$$\sum M_B = 0: \quad R_A \cdot 2{,}5 = F \cdot 3{,}5 + q \cdot 2{,}5 \cdot 1{,}25 = 35 + 50 = 85$$

$$\boxed{R_A = 34\ \text{kN}} \qquad R_B = 50 - 34 = \boxed{16\ \text{kN}}$$

## Korak 2 — Diagram upogibnih momentov

Koordinata ξ od A v desno:

$$M(\xi) = -10 + 24\xi - 8\xi^2 \quad \text{[kNm]}$$

| Mesto | ξ [m] | M [kNm] |
|-------|--------|---------|
| Prosti konec | — | 0 |
| **Podpora A** | 0 | **−10** |
| **Max v polju** | **1,5** | **+8** |
| Podpora B | 2,5 | 0 |

Max v polju: $dM/d\xi = 24 - 16\xi = 0 \Rightarrow \xi = 1{,}5\ \text{m}$, $M = +8\ \text{kNm}$

## Korak 3 — Geometrija U-prereza

Prerez razdeljen na 3 dele (steni + pasnica):

| Del | Dimenzije | $A_i$ [cm²] | $y_i$ [cm] | $A_i y_i$ [cm³] |
|-----|-----------|-------------|------------|-----------------|
| leva stena | 7×15 | 105 | 7,5 | 787,5 |
| desna stena | 7×15 | 105 | 7,5 | 787,5 |
| spodnja pasnica | 26×7 | 182 | 3,5 | 637,0 |
| **Σ** | | **392** | | **2212** |

$$\boxed{y_T = \frac{2212}{392} = 5{,}6428\ \text{cm}} \quad \text{(od spodnjega roba)}$$

**Vztrajnostni moment** (Steinerjevo pravilo):

$$J = 2\left[\frac{7 \cdot 15^3}{12} + 105 \cdot (7{,}5 - 5{,}6428)^2\right] + \left[\frac{26 \cdot 7^3}{12} + 182 \cdot (3{,}5 - 5{,}6428)^2\right]$$

$$= 2 \cdot 2330{,}95 + 1578{,}9$$

$$\boxed{J_{x_T} = 6240{,}8\ \text{cm}^4}$$

Razdalji skrajnih vlaken:

$$e_{zg} = 15 - 5{,}6428 = 9{,}357\ \text{cm} \qquad e_{sp} = 5{,}6428\ \text{cm}$$

## Korak 4 — Napetosti pri podpori A ($M = -1000\ \text{kNcm}$, hogging)

Negativen moment → **zgoraj nateg, spodaj tlak**:

$$\sigma_{zg} = \frac{|M| \cdot e_{zg}}{J} = \frac{1000 \cdot 9{,}357}{6240{,}8} = \boxed{+1{,}500\ \text{kN/cm}^2\ \text{(nateg)}}$$

$$\sigma_{sp} = \frac{|M| \cdot e_{sp}}{J} = \frac{1000 \cdot 5{,}643}{6240{,}8} = \boxed{-0{,}904\ \text{kN/cm}^2\ \text{(tlak)}}$$

## Korak 5 — Napetosti v polju ($M = +800\ \text{kNcm}$, sagging, ξ=1,5m od A)

Pozitiven moment → **spodaj nateg, zgoraj tlak**:

$$\sigma_{sp} = \frac{800 \cdot 5{,}643}{6240{,}8} = +0{,}723\ \text{kN/cm}^2\ \text{(nateg)}$$

$$\sigma_{zg} = \frac{800 \cdot 9{,}357}{6240{,}8} = \boxed{-1{,}199\ \text{kN/cm}^2\ \text{(tlak)}}$$

## Rezultati — Ekstremne napetosti

| Napetost | Vrednost | Mesto | Vlakno |
|----------|----------|-------|--------|
| **Max nateg** | **+1,50 kN/cm²** | Podpora A (x=1m) | zgornji rob |
| **Max tlak** | **−1,20 kN/cm²** | ξ=1,5m od A (x=2,5m) | zgornji rob |

> ⚠️ **Ključna ugotovitev:** U-prerez je asimetričen — $e_{zg} = 9{,}36\ \text{cm} > e_{sp} = 5{,}64\ \text{cm}$. Zato je **zgornji rob kritičen pri obeh predznaknih momentih**. Samo primerjava $|M_A|$ in $|M_{max}|$ ni dovolj — preveriti je treba napetosti pri vsakem prerezu posebej.

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| y_T | 5,6428 cm | težišče od spodnjega roba |
| e_zg | 9,357 cm | razdalja od NO do zgornjega roba |
| e_sp | 5,643 cm | razdalja od NO do spodnjega roba |
| J | 6240,8 cm⁴ | vztrajnostni moment glede na težiščno os |
| R_A | 34 kN | reakcija pri A |
| R_B | 16 kN | reakcija pri B |
| M_A | −10 kNm | moment pri podpori A |
| M_max | +8 kNm | max moment v polju |

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]]
- [[mehanika]]
- [[Mehanika Hub]]

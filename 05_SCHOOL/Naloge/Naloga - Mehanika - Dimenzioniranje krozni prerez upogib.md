---
tags: [mehanika, upogib, dimenzioniranje, krozni-prerez, naloga]
predmet: Mehanika
datum: 2026-06-11
vir: IMG_1241.pdf, str. 24 (naloga), str. 26 (rešitev)
---

# Naloga: Dimenzioniranje krožnega prereza na upogib

## Namen

Določiti minimalni premer $d$ krožnega prereza previsnega nosilca, obremenjenega s točkovno silo $F$ in enakomerno obtežbo $q$.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| F | 4 kN | točkovna sila (vodoraven, ročica 1,5 m) |
| q | 2 kN/m | enakomerna obtežba v polju A–B |
| L_previs | 1,5 m | ročica sile F do podpore A |
| L_AB | 3 m | razpon med podporama |
| σ_dop | 1,2 kN/cm² | dopustna napetost |
| d | ? | premer krožnega prereza |

## Shema konstrukcije

![[upogib_krozni_prerez.svg|637]]

- **A** = leva podpora (pri x = 0)
- **B** = desna podpora (pri x = 3 m)
- Obtežba $q = 2$ kN/m deluje na polju A–B
- Sila $F = 4$ kN deluje vodorovno z ročico 1,5 m → ustvari moment pri A

---

## Korak 1 — Reakcije

Vpnemo vrtišče v **B** (izniči neznano $B_y$):

$$\sum M_B = 0: \quad -F \cdot 1{,}5 - A_y \cdot 3 + q \cdot 3 \cdot 1{,}5 = 0$$

$$A_y \cdot 3 = q \cdot 3 \cdot 1{,}5 - F \cdot 1{,}5 = 9 - 6 = 3$$

$$\boxed{A_y = 1\ \text{kN}}$$

Iz ravnotežja navpičnih sil ($F$ je vodoroven → ne prispeva k $\sum F_y$):

$$B_y = q \cdot 3 - A_y = 6 - 1 = \boxed{5\ \text{kN}}$$

**Moment pri podpori A** (od ročice $F$):

$$M_A = -F \cdot 1{,}5 = -4 \cdot 1{,}5 = -6\ \text{kNm} \quad \text{(hogging)}$$

> **glej:** [[Koncept - Upogib#Korak 1 — Statični sistem in reakcije]]

---

## Korak 2 — Diagram upogibnih momentov

Koordinata $x$ od **B** v levo (0 pri B, 3 pri A):

$$M(x) = B_y \cdot x - \frac{q \cdot x^2}{2} = 5x - x^2 \quad [\text{kNm}]$$

Kontrola robnih vrednosti:

| Mesto | x [m] | M [kNm] |
|-------|--------|---------|
| Podpora B | 0 | 0 ✓ |
| Podpora A | 3 | $5 \cdot 3 - 9 = 6$ kNm |
| Prosti konec | — | 0 ✓ |

Maksimum v polju — iščemo z $dM/dx = 0$:

$$\frac{dM}{dx} = 5 - 2x = 0 \quad \Rightarrow \quad x = 2{,}5\ \text{m\ od\ B}$$

$$M_{max} = 5 \cdot 2{,}5 - (2{,}5)^2 = 12{,}5 - 6{,}25 = \boxed{+6{,}25\ \text{kNm}}$$

**Primerjava kritičnih momentov:**

$$|M_{max,\,polje}| = 6{,}25\ \text{kNm} \quad > \quad |M_A| = 6{,}00\ \text{kNm}$$

→ **Merodajni moment:** $M_{mer} = 6{,}25\ \text{kNm} = \mathbf{625\ \text{kNcm}}$

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov]]

---

## Korak 3 — Geometrija krožnega prereza

Za krožni prerez s premerom $d$:

$$I_x = \frac{\pi d^4}{64} \qquad W_x = \frac{\pi d^3}{32} \qquad e = \frac{d}{2}$$

Preveritev zveze:

$$W_x = \frac{I_x}{e} = \frac{\pi d^4 / 64}{d/2} = \frac{\pi d^3}{32} \quad ✓$$

> **glej:** [[Koncept - Vztrajnostni moment#Korak 1 — Enačbe za enostavne prereze]]

---

## Korak 4 — Pogoj dopustne napetosti

$$\sigma = \frac{M_{mer}}{W_x} \leq \sigma_{dop}$$

$$W_x \geq \frac{M_{mer}}{\sigma_{dop}} = \frac{625\ \text{kNcm}}{1{,}2\ \text{kN/cm}^2} = 520{,}83\ \text{cm}^3$$

Vstavimo $W_x = \pi d^3 / 32$:

$$\frac{\pi d^3}{32} \geq 520{,}83$$

$$d^3 \geq \frac{32 \cdot 520{,}83}{\pi} = \frac{16666{,}7}{3{,}1416} = 5305{,}2\ \text{cm}^3$$

$$\boxed{d \geq \sqrt[3]{5305{,}2} \approx 17{,}44\ \text{cm}}$$

> **glej:** [[Koncept - Upogib#Korak 5 — Dimenzioniranje]]

---

## Korak 5 — Rezultat in kontrola

$$\boxed{d_{min} = 17{,}44\ \text{cm}}$$

**Kontrola** z $d = 17{,}44$ cm:

$$W_{dej} = \frac{\pi \cdot (17{,}44)^3}{32} = \frac{\pi \cdot 5302{,}0}{32} = 521{,}0\ \text{cm}^3$$

$$\sigma_{dej} = \frac{625}{521{,}0} = 1{,}20\ \text{kN/cm}^2 \leq 1{,}2\ \text{kN/cm}^2 \quad ✓$$

> **glej:** [[Koncept - Upogib#Korak 4 — Napetosti in predznak]]

---

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| A_y | 1 kN | reakcija pri podpori A |
| B_y | 5 kN | reakcija pri podpori B |
| M_A | −6 kNm = −600 kNcm | moment pri A (hogging) |
| M_max | +6,25 kNm = 625 kNcm | max moment v polju (sagging) |
| M_mer | 625 kNcm | merodajni moment za dimenzioniranje |
| W_x | πd³/32 | odpornostni moment krožnega prereza |
| d³ | 5305,2 cm³ | izračunano iz pogoja σ ≤ σ_dop |
| **d** | **≥ 17,44 cm** | **minimalni premer** |

---

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]]
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]]
- [[Mehanika Hub]]

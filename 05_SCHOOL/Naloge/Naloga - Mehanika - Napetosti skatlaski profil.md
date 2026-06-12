---
tags: [mehanika, upogib, napetosti, skatlaski-profil, votli-prerez, naloga]
predmet: Mehanika
datum: 2026-06-12
vir: IMG_1241.pdf, str. 34 (naloga), str. 35–36 (rešitev)
---

# Naloga: Največja upogibna napetost v škatlastem profilu

## Namen

Za prostoležeči nosilci z enakomerno obtežbo $q$ na polovici razpona določiti $M_{max}$, izračunati $I_z$ škatlastega prereza in najti $\sigma_{max}$.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| q | 2 kN/m | enakomerna obtežba (desna polovica) |
| L | 10 m | skupni razpon (5 m + 5 m) |
| b_zun | 7,5 cm | zunanja širina prereza |
| h_zun | 10 cm | zunanja višina prereza |
| b_not | 5,5 cm | notranja širina (votlina) |
| h_not | 8 cm | notranja višina (votlina) |
| σ_dop | 115 MPa | dopustna napetost (za preverjanje) |

## Shema konstrukcije

![[upogib_skatlaski_profil.svg|760]]

- Prostoležeči nosilci, razpon 10 m (5 m + 5 m)
- Obtežba $q = 2$ kN/m deluje samo na **desni 5 m razpon**
- Škatlasti prerez: votla pravokotna cev

---

## Korak 1 — Reakcije

Moment ravnotežja okrog **A** ($\sum M_A = 0$):

$$-q \cdot 5\ \text{m} \cdot 7{,}5\ \text{m} + B_y \cdot 10\ \text{m} = 0$$

$$B_y = \frac{2 \cdot 5 \cdot 7{,}5}{10} = \frac{75}{10} = \boxed{7{,}5\ \text{kN}}$$

Iz ravnotežja navpičnih sil:

$$A_y + B_y = q \cdot 5 = 10\ \text{kN}$$

$$\boxed{A_y = 10 - 7{,}5 = 2{,}5\ \text{kN}}$$

> **glej:** [[Koncept - Upogib#Korak 1 — Statični sistem in reakcije]]

---

## Korak 2 — Diagram upogibnih momentov

**Leva polovica** ($x \in [0,\ 5\ \text{m}]$ od A):

$$T(x) = A_y = 2{,}5\ \text{kN} \quad \Rightarrow \quad M(x) = 2{,}5 \cdot x$$

$$M(5\ \text{m}) = 12{,}5\ \text{kNm} \quad \text{(vrednost pri vmesni točki)}$$

**Desna polovica** ($x \in [0,\ 5\ \text{m}]$ od B):

$$T(x) = -B_y + q \cdot x = -7{,}5 + 2x$$

$$M(x) = B_y \cdot x - \frac{q \cdot x^2}{2} = 7{,}5x - x^2$$

Kontrola zveznosti pri $x = 5$ m od B: $M(5) = 37{,}5 - 25 = 12{,}5$ kNm ✓

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov]]

---

## Korak 3 — Lokacija in vrednost M_max

Iščemo $x_0$, kjer je $T(x_0) = 0$:

$$T(x_0) = -7{,}5 + 2 \cdot x_0 = 0 \quad \Rightarrow \quad x_0 = \frac{7{,}5}{2} = \boxed{3{,}75\ \text{m od B}}$$

$$M_{max} = 7{,}5 \cdot 3{,}75 - (3{,}75)^2 = 28{,}125 - 14{,}0625$$
$

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov
$$\boxed{M_{max} = 14{,}06\ \text{kNm} = 1406\ \text{kNcm}}$]]

---

## Korak 4 — Vztrajnostni moment škatlastega prereza

Votli pravokotni prerez — **metoda odštevanja**:

$$I_z = \frac{b_{zun} \cdot h_{zun}^3}{12} - \frac{b_{not} \cdot h_{not}^3}{12}$$

$$= \frac{7{,}5 \cdot 10^3}{12} - \frac{5{,}5 \cdot 8^3}{12}$$

$$= \frac{7500}{12} - \frac{2816}{12} = 625 - 234{,}67$$

$$\boxed{I_z = 390{,}33\ \text{cm}^4 = 3{,}904 \cdot 10^{-6}\ \text{m}^4}$$

Razdalja do ekst­remnega vlakna (simetričen prerez):

$$e = \frac{h_{zun}}{2} = \frac{10}{2} = \boxed{5\ \text{cm} = 0{,}05\ \text{m}}$$

> **glej:** [[Koncept - Vztrajnostni moment#Korak 1 — Enačbe za enostavne prereze]]

---

## Korak 5 — Največja upogibna napetost

$$\sigma_{max} = \frac{M_{max} \cdot e}{I_z} = \frac{14{,}06\ \text{kNm} \cdot 0{,}05\ \text{m}}{3{,}904 \cdot 10^{-6}\ \text{m}^4}$$

$$= \frac{0{,}703\ \text{kNm}^2/\text{m}^2}{3{,}904 \cdot 10^{-6}\ \text{m}^4} = \frac{703\ \text{N}}{3{,}904 \cdot 10^{-6}\ \text{m}^2}$$

$$\boxed{\sigma_{max} = 180 \cdot 10^6\ \text{Pa} = 180\ \text{MPa}}$$

**Preverjanje dopustne napetosti** ($\sigma_{dop} = 115$ MPa):

$$\sigma_{max} = 180\ \text{MPa} > \sigma_{dop} = 115\ \text{MPa} \quad \Rightarrow \quad \text{prerez ni ustrezen!}$$

> **glej:** [[Koncept - Upogib#Korak 5 — Dimenzioniranje]]

---

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| q | 2 kN/m | obtežba na desni polovici |
| A_y | 2,5 kN | reakcija pri podpori A |
| B_y | 7,5 kN | reakcija pri podpori B |
| x₀ | 3,75 m od B | lokacija M_max (kjer T=0) |
| M_max | 14,06 kNm = 1406 kNcm | merodajni moment |
| b_zun × h_zun | 7,5 × 10 cm | zunanja dimenzija |
| b_not × h_not | 5,5 × 8 cm | notranja dimenzija (votlina) |
| I_z | 390,33 cm⁴ | vztrajnostni moment |
| e | 5 cm = 0,05 m | ekst. vlakno |
| **σ_max** | **180 MPa** | **največja napetost** |
| σ_dop | 115 MPa | dopustna (prekoračena!) |

---

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Upogibne napetosti C-prerez]]
- [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]]
- [[Mehanika Hub]]

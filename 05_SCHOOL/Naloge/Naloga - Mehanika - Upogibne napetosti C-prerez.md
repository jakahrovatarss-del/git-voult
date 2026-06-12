---
tags: [mehanika, upogib, napetosti, prerez, naloga]
predmet: Mehanika
datum: 2026-06-12
vir: IMG_1241.pdf, str. 22 (naloga), str. 23 (rešitev)
---

# Naloga: Ekstremne upogibne napetosti za C-prerez

## Namen

Za konzolni nosilci z znano obtežbo $F$ določiti napetosti v ekst­remnih vlaknih prereza (točke a–e vzdolž višine) in izračunati ekstremne upogibne napetosti.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| F | 400 N | točkovna sila (na prostem koncu) |
| a | 15 cm | ročica — razdalja od sile do vpetja |
| b | 1,5 cm | širina pravokotnega prereza |
| h | 5 cm | višina pravokotnega prereza |
| σ_dop | — | ni dan (samo izračun napetosti) |

## Shema konstrukcije

![[upogib_c_prerez.svg|700]]

- Konzolni nosilci vpet na desni, prosta leva konica
- Sila $F = 400$ N deluje navpično na prostem koncu
- Analiziramo napetosti v prerezu na mestu vpetja (max M)
- Točke a, b, c, d, e so porazdeljene po višini prereza

---

## Korak 1 — Upogibni moment v prerezu

Merodajni prerez je **na mestu vpetja** (konzola — max M pri vpetju):

$$M = F \cdot a = 400\ \text{N} \cdot 15\ \text{cm} = 6000\ \text{Ncm} = 6\ \text{kNcm}$$

$$\boxed{M = 6\ \text{kNcm}}$$

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov]]

---

## Korak 2 — Geometrija prereza

Pravokotni polni prerez z $b = 1{,}5$ cm in $h = 5$ cm:

$$I_z = \frac{b \cdot h^3}{12} = \frac{1{,}5 \cdot 5^3}{12} = \frac{1{,}5 \cdot 125}{12} = \frac{187{,}5}{12}$$

$$\boxed{I_z = 15{,}625\ \text{cm}^4}$$

Razdalja do ekst­remnih vlaken (simetrični prerez):

$$e = \frac{h}{2} = \frac{5}{2} = \boxed{2{,}5\ \text{cm}}$$

Odpornostni moment:

$$W = \frac{I_z}{e} = \frac{15{,}625}{2{,}5} = \boxed{6{,}25\ \text{cm}^3}$$

> **glej:** [[Koncept - Vztrajnostni moment#Korak 1 — Enačbe za enostavne prereze]]

---

## Korak 3 — Napetosti v točkah a–e

Splošna enačba upogibne napetosti (**Navierjev zakon**):

$$\sigma(y) = \frac{M \cdot y}{I_z}$$

kjer je $y$ razdalja od nevtralne osi (pozitivno navzgor).

| Točka | $y$ [cm] | $\sigma$ [N/cm²] | $\sigma$ [MPa] | Opomba |
|-------|----------|-----------------|----------------|--------|
| **e** | +2,5 | +960 | +9,6 | zg. vlakno — **nateg** |
| **d** | +1,25 | +480 | +4,8 | — |
| **c** | 0 | 0 | 0 | nevtralna os |
| **b** | −1,25 | −480 | −4,8 | — |
| **a** | −2,5 | −960 | −9,6 | sp. vlakno — **tlak** |

Izračun za ekstremno vlakno ($y = e = 2{,}5$ cm):

$$\sigma_{max} = \frac{M}{W} = \frac{6000\ \text{Ncm}}{6{,}25\ \text{cm}^3} = 960\ \text{N/cm}^2$$

> **glej:** [[Koncept - Upogib#Korak 4 — Napetosti in predznak]]

---

## Korak 4 — Ekstremne napetosti (rezultat)

$$\boxed{\sigma_{e} = +\frac{M}{W} = +960\ \text{N/cm}^2 = +9{,}6\ \text{MPa} \quad \text{(nateg — zgornje vlakno)}}$$

$$\boxed{\sigma_{a} = -\frac{M}{W} = -960\ \text{N/cm}^2 = -9{,}6\ \text{MPa} \quad \text{(tlak — spodnje vlakno)}}$$

Porazdelitev je **linearna** — narašča od $\sigma = 0$ na nevtralni osi do ekst­remnih vrednosti na robovih prereza.

> **glej:** [[Koncept - Upogib#Korak 5 — Dimenzioniranje]]

---

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| F | 400 N | točkovna sila |
| a | 15 cm | ročica |
| M | 6000 Ncm = 6 kNcm | upogibni moment v prerezu |
| b | 1,5 cm | širina prereza |
| h | 5 cm | višina prereza |
| I_z | 15,625 cm⁴ | vztrajnostni moment |
| e | 2,5 cm | razdalja do ekst. vlakna |
| W | 6,25 cm³ | odpornostni moment |
| **σ_max** | **±9,6 MPa** | **ekstremni napetosti** |

---

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]]
- [[Naloga - Mehanika - Napetosti skatlaski profil]]
- [[Mehanika Hub]]

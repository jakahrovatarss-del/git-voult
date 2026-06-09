---
tags: [mehanika, uklon, euler, les, steber, naloga]
predmet: Mehanika
datum: 2026-06-09
vir: IMG_1241.pdf, str. 9–11, naloga 3
---

# Naloga: Maksimalna sila za lesen steber (uklon)

## Namen

Poiskati maksimalno zunanjo silo F, da se lesen steber T-rame še ne ukloni.

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| L | 4 m = 400 cm | višina stebra |
| b = h | 12 cm | dimenzija kvadratnega prereza |
| E | 1000 kN/cm² | modul elastičnosti (les, iglavci) |
| σ_dop | 1,0 kN/cm² | dopustna napetost |
| ν | 3 | uklonska varnost |
| Vpetje | spodaj + zgoraj členkasto | β = 1, l_u = L |

## Konstrukcija

T-rama: horizontalni tram (2 m + 4 m) na vrhu stebra, sila F na desnem koncu.

![[steber_uklon_maksimalna_sila.svg]]

## Ravnotežje — notranja sila v stebru

$$\sum M_A = 0: \quad N \cdot 2 = F \cdot 6 \quad \Rightarrow \quad N = 3 \cdot F$$

## Lastnosti prereza 12×12 cm

$$A = 144 \text{ cm}^2, \quad I_{min} = \frac{12^4}{12} = 1728 \text{ cm}^4, \quad i = \sqrt{12} = 3{,}464 \text{ cm}$$

## Vitkost

$$\lambda = \frac{l_u}{i} = \frac{400}{3{,}464} = 115{,}5 \quad > \quad \lambda_e \approx 100 \quad \Rightarrow \text{ Euler velja ✓}$$

## Eulerjeva kritična sila

$$F_k = \frac{\pi^2 \cdot E \cdot I}{l_u^2} = \frac{\pi^2 \cdot 1000 \cdot 1728}{400^2} = \boxed{106{,}59 \text{ kN}}$$

## Dopustna sila in F_max

$$F_{dop} = \frac{F_k}{\nu} = \frac{106{,}59}{3} = 35{,}53 \text{ kN}$$

$$\boxed{F_{max} = \frac{F_{dop}}{3} = \frac{35{,}53}{3} = 11{,}84 \text{ kN}}$$

## Povezave

- [[Koncept - Euler Uklon]]
- [[Naloga - Mehanika - Uklon lesene deske]]
- [[mehanika]]
- [[Mehanika Hub]]

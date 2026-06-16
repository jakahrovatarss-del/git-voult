---
tags: [mehanika, uklon, euler, les, naloga]
predmet: Mehanika
datum: 2026-06-09
vir: IMG_1241.pdf, str. 22, naloga 3
---

# Naloga: Uklon navpične lesene deske

## Namen

Izračunati kritično uklonsko silo $F_k$ navpično stoječe lesene deske, ki je spodaj vbetonirana in zgoraj prosta (konzola — Euler 4. primer).

## Podatki

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| $L$ | 3,5 m = 350 cm | višina deske |
| $b$ | 2,5 cm | tanjša dimenzija prereza |
| $h$ | 20 cm | širša dimenzija prereza |
| $E$ | 1000 kN/cm² | modul elastičnosti lesa |
| Vpetje | spodaj vpeta, zgoraj prosta | Euler 4. primer, $\beta = 2$ |

## Skica

![[uklon_lesena_deska.svg]]

## Izpeljava

### 1. Uklonska dolžina

$$l_u = \beta \cdot L = 2 \cdot 350 = 700 \text{ cm}$$

### 2. Minimalni vztrajnostni moment (šibka os)

Uklon nastopi okoli šibke osi ($b = 2{,}5$ cm):

$$I_{min} = \frac{h \cdot b^3}{12} = \frac{20 \cdot (2{,}5)^3}{12} = \frac{312{,}5}{12} = 26{,}04 \text{ cm}^4$$

### 3. Eulerjeva formula

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2} = \frac{9{,}8696 \cdot 1000 \cdot 26{,}04}{700^2} = \frac{257056}{490000}$$

$$\boxed{F_k = 0{,}524 \text{ kN} \approx 524 \text{ N}}$$

## Zaključek

Deska je kritično vitka v smeri $b = 2{,}5$ cm. Že ~524 N osne tlačne sile zadostuje za uklon. V praksi bi bila potrebna bočna podpora.

## Povezave

- [[Koncept - Euler Uklon]]
- [[Mehanika Hub]]
- [[STATIKA]]
- [[Mehanika Hub]]

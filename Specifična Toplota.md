---
categories:
  - "[[Koncepti]]"
created: 2026-06-10
---

# Kaj je

![Kalorimeter — merjenje specifične toplote snovi](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Calorimeter_scheme.png/250px-Calorimeter_scheme.png)
*Kalorimeter — naprava za merjenje toplote in specifične toplote snovi*

Specifična toplota (c) je količina energije [J] ki jo je treba dovediti 1 g snovi da se segreje za 1 °C. Osnovna veličina termodinamike.

**Voda: c = 4,18 J/(g·°C)** — ena od najvišjih vrednosti med navadnimi snovmi. Zato je voda odličen toplotni hranilnik in prenosnik.

# Formula

**Q = m · c · ΔT**

| Simbol | Pomen | Enota |
|---|---|---|
| Q | toplota (energija) | J |
| m | masa snovi | g |
| c | specifična toplota | J/(g·°C) |
| ΔT | sprememba temperature | °C |

# Moč iz segrevanja

Če poznamo čas segrevanja, dobimo moč:

**P = Q / t**

Primer iz [[Concept Crafted - DIY Solarni Koncentrator]]:
- m = 20.000 g (20 L vode)
- c = 4,18 J/(g·°C)
- ΔT = 44,2 − 22,6 = 21,6 °C
- t = 1.952 s (32 min)

Q = 20.000 × 4,18 × 21,6 = **183.840 J**
P = 183.840 / 1.952 = **~924 W**

# Primerjava specifičnih toplot

| Snov | c [J/(g·°C)] |
|---|---|
| Voda | 4,18 |
| Etanol | 2,44 |
| Aluminij | 0,90 |
| Baker | 0,39 |
| Železo | 0,45 |
| Zrak | 1,01 |

Baker ima nizko specifično toploto → hitro se segreje → dober material za kolektor pri solarnem koncentratorju ([[Solarni Koncentrator]]).

# Aplikacije

- Kalorimetrija — merjenje energije kemičnih reakcij
- Inženiring — dimenzioniranje toplotnih sistemov
- Solarni sistemi — izračun moči zbiralnika [[Solarni Koncentrator]]
- Klimatizacija — toplota ki jo je treba odvesti/dovesti

# Fazni prehodi — Latentna toplota

> Iz Skripta-FIzika-BFUNI-2025.pdf, Poglavje 11

Pri faznem prehodu se temperatura **ne spreminja** kljub dovajanju toplote:

$$Q = \pm mq$$

| Prehod | Konstanta | Voda |
|--------|-----------|------|
| Taljenje | $q_t$ (specifična talilna toplota) | **333 kJ/kg** |
| Izhlapevanje | $q_i$ (specifična izparilna toplota) | **2260 kJ/kg** |

Led se tali pri 0°C, voda vre pri 100°C — oba procesa pri **konstantni temperaturi**.

# Prevajanje toplote (kondukcija)

$$P = -\frac{\lambda A \Delta T}{l}$$

Toplotni upor: $R = l/(\lambda A)$ → analogija z Ohmovim zakonom  
Stiropor: $\lambda = 0{,}04\ \text{W/(m·K)}$ | Baker: $\lambda = 400\ \text{W/(m·K)}$

# Sevanje — Stefan-Boltzmann

$$P = e\sigma A(T^4 - T_0^4), \quad \sigma = 5{,}67 \times 10^{-8}\ \text{W/m}^2\text{K}^4$$

→ Podrobno: [[Koncept - Toplota]]

# Povezano

[[Solarni Koncentrator]]
[[Concept Crafted - DIY Solarni Koncentrator]]
[[mehanika]]
[[Koncept - Toplota]]

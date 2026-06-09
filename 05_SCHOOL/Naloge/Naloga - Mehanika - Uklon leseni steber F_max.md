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

![[ravnotezje_T_rama.svg]]

Vzamemo točko A (leva podpora) kot vrtišče — reakcija $R_A$ pri tem odpade (ročica = 0). Ostaneta samo $N$ in $F$:

| Sila | Ročica od A | Moment |
|------|-------------|--------|
| F (navzdol) | 6 m | F · 6 — v smeri ure |
| N (navzgor) | 2 m | N · 2 — nasprotno |

$$\sum M_A = 0: \quad N \cdot 2 = F \cdot 6 \quad \Rightarrow \quad N = 3 \cdot F$$

> **Intuicija:** Steber je bližje podpori (2 m) kot sila F (6 m) — zato nosi 3× večjo silo. Enako kot gugalnica: bližje sredini = večja sila za ravnotežje.

## Lastnosti prereza 12×12 cm

$$A = 12^2 = 144 \text{ cm}^2$$

$$I_{min} = \frac{a^4}{12} = \frac{12^4}{12} = 1728 \text{ cm}^4$$

$$i = \sqrt{\frac{I}{A}} = \sqrt{\frac{1728}{144}} = \sqrt{12} = 3{,}464 \text{ cm}$$

## Vitkost

$$\lambda = \frac{l_u}{i} = \frac{400}{3{,}464} = 115{,}47 \quad > \quad \lambda_e \approx 100 \quad \Rightarrow \text{ Euler velja ✓}$$

---

## Metoda 1 — Euler

$$F_k = \frac{\pi^2 \cdot E \cdot I}{l_u^2} = \frac{\pi^2 \cdot 1000 \cdot 1728}{400^2} = \boxed{106{,}59 \text{ kN}}$$

$$F_{dop} = \frac{F_k}{\nu} = \frac{106{,}59}{3} = 35{,}53 \text{ kN}$$

$$\boxed{F_{max} = F_{dop} \cdot \frac{2}{6} = \frac{35{,}53}{3} = 11{,}84 \text{ kN}}$$

---

## Metoda 2 — ω postopek

Upošteva vitkost palice preko koeficienta ω iz tabel (upošteva nepopolnosti realne palice).

$$\lambda = 115{,}47 \quad \Rightarrow \quad \omega = 4{,}00743 \quad \text{(iz tabel za iglavce)}$$

$$F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega} = \frac{1{,}0 \cdot 144}{4{,}00743} = 35{,}933 \text{ kN}$$

$$\boxed{F_{max} = F_{dop} \cdot \frac{2}{6} = \frac{35{,}933}{3} = 11{,}977 \text{ kN}}$$

---

## Primerjava metod

| Metoda | F_dop | F_max |
|--------|-------|-------|
| Euler | 35,53 kN | **11,84 kN** |
| ω postopek | 35,93 kN | **11,98 kN** |

Razlika ~1 %. ω metoda je natančnejša — Euler je nekoliko konzervativnejši pri tej vitkosti.

## Povezave

- [[Koncept - Euler Uklon]]
- [[Naloga - Mehanika - Uklon lesene deske]]
- [[mehanika]]
- [[Mehanika Hub]]

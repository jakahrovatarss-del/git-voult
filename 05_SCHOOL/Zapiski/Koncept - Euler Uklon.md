---
tags: [mehanika, uklon, euler, stabilnost, koncept]
predmet: Mehanika
datum: 2026-06-09
---

# Koncept: Euler Uklon (Uklonska stabilnost)

## Namen

Uklon (buckling) nastopi, ko tlačno obremenjena vitka palica izgubi stabilnost in se bočno ukloni. Eulerjeva teorija določa kritično silo, pri kateri pride do uklona.

## Eulerjeva formula

$$\boxed{F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2}}$$

## Uklonska dolžina

$$l_u = \beta \cdot L$$

### Uklonski faktorji $\beta$ — 4 Eulerovi primeri

| Primer | Vpetje | $\beta$ | $l_u$ |
|--------|--------|---------|-------|
| 1 | obe strani členkasto | 1,0 | $L$ |
| 2 | spodaj vpeta, zgoraj členkasta | 0,7 | $0{,}7L$ |
| 3 | obe strani vpeti | 0,5 | $0{,}5L$ |
| 4 | spodaj vpeta, zgoraj prosta (konzola) | **2,0** | $2L$ |

## Minimalni vztrajnostni moment

Uklon nastopi vedno okoli **šibke osi** (os z najmanjšim $I$).

Za pravokoten prerez $b \times h$ (kjer $b < h$):

$$I_{min} = \frac{h \cdot b^3}{12}$$

## Vitkost in meja Eulerja

$$\lambda = \frac{l_u}{i}, \quad i = \sqrt{\frac{I_{min}}{A}}$$

Euler velja samo, če je $\lambda > \lambda_e$. Za les (iglavci): $\lambda_e \approx 100$.

- $\lambda > \lambda_e$ → Euler
- $\lambda \leq \lambda_e$ → Tetmajer ali ω postopek

## Uklonska varnost in dopustna sila

### Euler

$$F_{dop} = \frac{F_k}{\nu}$$

Za les: $\nu = 3$ (tipično). Dopustna napetost: $\sigma_{dop} = 1{,}0$ kN/cm² (iglavci).

### ω postopek

Natančnejša metoda — upošteva vitkost in nepopolnosti realne palice:

$$F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega}$$

Vrednost $\omega$ se odčita iz **ω tabel** glede na $\lambda$. Za iglavce, $\lambda = 115{,}47$ → $\omega = 4{,}007$.

> **Razlika Euler vs. ω:** Euler je nekoliko konzervativnejši. Pri $\lambda \approx 115$ sta rezultata praktično enaka (~1 % razlika).

## Spremenljivke

| Simbol | Pomen | Enota |
|--------|-------|-------|
| $F_k$ | kritična uklonska sila | kN |
| $F_{dop}$ | dopustna osna sila ($F_k / \nu$) | kN |
| $E$ | modul elastičnosti (Young) | kN/cm² |
| $I_{min}$ | minimalni vztrajnostni moment | cm⁴ |
| $l_u$ | uklonska (nadomestna) dolžina | cm |
| $\beta$ | uklonski faktor | — |
| $L$ | dejanska dolžina palice | cm |
| $\lambda$ | vitkost | — |
| $i$ | vztrajnostni polmer | cm |
| $\nu$ | uklonska varnost | — |

## Grafični prikazi (reference)

Statična skica — Euler 4. primer (konzola):

![[uklon_lesena_deska.svg]]

Interaktivni prikaz z vsemi 4 Eulerjevimi primeri in kalkulatorjem:

[Odpri interaktivni prikaz](Attachments/mehanika/uklon_interaktivni_prikaz.html)

## Primeri nalog

- [[Naloga - Mehanika - Uklon lesene deske]] — konzola (β=2), 2,5×20 cm, L=3,5m → $F_k = 0{,}524$ kN
- [[Naloga - Mehanika - Uklon leseni steber F_max]] — T-rama, obe strani členkasto (β=1), 12×12 cm, L=4m → $F_{max} = 11{,}84$ kN *(ravnotežje: N = 3·F)*

## Povezave

- [[Koncept - Vztrajnostni moment]]
- [[mehanika]]
- [[STATIKA]]
- [[Naloga - Mehanika - Uklon lesene deske]]
- [[Naloga - Mehanika - Uklon leseni steber F_max]]
- [[Mehanika Hub]]

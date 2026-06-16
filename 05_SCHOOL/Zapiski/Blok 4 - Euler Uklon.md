---
tags: [mehanika, euler, uklon, stabilnost, lambda, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 4 — Euler Uklon

## VSE ENAČBE

```
EULERJEVA KRITIČNA SILA:
  Fk = π²·E·Imin / lu²

UKLONSKA DOLŽINA:
  lu = β·L

β TABELA:
  β = 0.5   → oba konca vpeta (most conservative)
  β = 0.7   → eno vpetje + en prosti konec (pin)
  β = 1.0   → oba konca na členkastih podporah ← STANDARD
  β = 2.0   → konzola (vpetje + prost konec) ← NAJNEVARNEJŠA

VITKOST:
  λ = lu / i,   kjer i = √(Imin/A)  ... polmer inercije
  λe = π·√(E/σdop)    ... mejna vitkost

EULER VELJA: λ > λe
JEKLO: λe = π·√(21000/16) ≈ 114
LES:   λe = π·√(1000/1.2) ≈ 90.7   (ali z 1.0: ≈ 99.3)

KRITIČNA NAPETOST (Euler):
  σkrit = π²·E / λ²

VARNOSTNI FAKTOR:
  ν = Fk / F  ≥ ν_zahtevani  (tipično ν = 3 za les)
  Les: ν = 3–10 (odvisno od zahtev)

DIMENZIONIRANJE:
  Imin_potreben = F·lu²·ν / π²·E

TETMAJER (les, neelastični uklon, 20 < λ < 100):
  σkrit = 29.3 - 0.194·λ  [MPa]

ω-POSTOPEK:
  σ = ω·F/A ≤ σdop  →  Fdop = σdop·A/ω
  (ω iz tabel glede na λ in material)

MEJE VELJAVNOSTI (les):
  λ < 20:  samo σ = F/A (ni uklona)
  20 ≤ λ < 100:  Tetmajer / ω-postopek
  λ ≥ 100:  Euler
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "steber", "tlačna palica", "tlačna obremenitev"
- "uklon", "stabilnost", "uklonska dolžina"
- "varnostni faktor za uklon"
- "Euler"
- Podana: **tlačna sila F**, dolžina L, material

**Kaj je podano:**
- $F$ = tlačna sila [kN]
- $L$ = dolžina palice [m ali cm]
- Robni pogoji (oba vpeta, konzola, ...)
- Material (les ali jeklo → E in $\sigma_{dop}$)
- Prerez ali varnostni faktor $\nu$

**Kaj se sprašuje:**
- Ali ukloni ($F < F_k$?)
- Varnostni faktor $\nu = F_k/F$
- Minimalne dimenzije prereza (dimenzioniranje)
- Kontrola vitkosti (Euler ali Tetmajer/Johnson)

---

## Kako začeti reševati

**Korak 1:** Določi $\beta$ iz robnih pogojev
- Nariši shemo — kateri konci so vpeti, kateri prosti
- Zapomni si: konzola $\beta = 2$ je **najnevarnejša**

**Korak 2:** Izračunaj uklonsko dolžino:
$$lu = \beta \cdot L$$

**Korak 3:** Preveri vitkost
- Izračunaj $\lambda = lu / i$ (ali oceni iz prereza)
- Če $\lambda > \lambda_e$: **velja Euler** → nadaljuj
- Če $\lambda < \lambda_e$: **ne velja Euler** → Johnson/Tetmajer formula

**Korak 4:** Izračunaj $F_k$:
$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2}$$

> ⚠️ Vedno vzami **I_min** — šibka os je kritična!

**Korak 5:** Varnostni faktor ali dimenzioniranje:
$$\nu = \frac{F_k}{F} \geq \nu_{zahtevani}$$

---

## Prepoznavanje razlik med podtipi nalog

| Tip                | Kako prepoznaš                              | Posebnost                                                   |
| ------------------ | ------------------------------------------- | ----------------------------------------------------------- |
| Kontrola uklona    | Dana $F$, $L$, prerez → izračunaj $\nu$     | Preveri $\lambda > \lambda_e$                               |
| Dimenzioniranje    | Dana $F$, $\nu$, $L$ → poišči dimenzijo     | Iz $I_{min,potr}$ izrazi $b$, $d$...                        |
| Konzola            | $\beta = 2$, pogosto manj očitno v besedilu | Tipično: steber z vpetjem spodaj                            |
| Asimetričen prerez | $I_{min}$ ni očiten                         | Izračunaj obe osi, vzami manjši!                            |
| Les vs. Jeklo      | Različen $\lambda_e$                        | Les: $\lambda_e \approx 90$, Jeklo: $\lambda_e \approx 114$ |

---

## β tabela — grafično

```
β = 0.5         β = 0.7         β = 1.0         β = 2.0
                                
  ═══ (vpeto)     ═══ (vpeto)     ○ (členek)      ╔══╗ (vpeto)
   |               |               |                |
   |               |               |                |
  ═══ (vpeto)     ○ (členek)     ○ (členek)         (prost)

  lu = L/2       lu = 0.7L       lu = L          lu = 2L
```

---

## ω-Postopek (za vmesno vitkost)

Ko je $\lambda_e < \lambda < \lambda_{max}$ (ni čisto Euler, ni čisto tlak):

$$\sigma = \omega \cdot \frac{F}{A} \leq \sigma_{dop}$$

$$F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega}$$

Faktor $\omega \geq 1$ se odčita iz tabel glede na $\lambda$ in material. Upošteva možnost uklona brez polnega elastičnega področja.

---

## Tetmajerjev postopek (za les, neelastični uklon)

Velja za les pri $20 < \lambda < 100$:

$$\sigma_{krit} = 29{,}3 - 0{,}194 \cdot \lambda \quad [\text{MPa}]$$

Za jeklo (St37): $\sigma_{krit} = 310 - 1{,}14 \cdot \lambda$ [MPa]

| $\lambda$ | Postopek | Opomba |
|-----------|---------|--------|
| $\lambda < 20$ | Čisti tlak: $\sigma = F/A \leq \sigma_{dop}$ | Uklon ni merodajen |
| $20 \leq \lambda < \lambda_e$ | Tetmajer / ω-postopek | Neelastični uklon |
| $\lambda \geq \lambda_e$ | **Euler** $F_k = \pi^2EI/l_u^2$ | Elastični uklon |

---

## Kombinacije z drugimi bloki

### Blok 1.5 + 4 (Geometrija prereza → Uklon)
Naloga: Izračunaj $I_{min}$ za T-prerez, nato $F_k$.
1. Steiner → $I_x$ in $I_y$ (oba!)
2. $I_{min} = \min(I_x, I_y)$
3. Euler formula

### Blok 2 + 4 (N+M + uklon)
Naloga: Steber pod $F$ z ekscentričnostjo $e$.
- Upogibni moment $M = F \cdot e$
- Dodatno preveri uklon s Euler
- Kombinirana kontrola: $\sigma_{max} = N/A + M/W \leq \sigma_{dop}$ **IN** $\nu_{ukl} \geq \nu$

### Blok 4 + 3.5 (Uklon + VM)
Redkeje — konzolna palica z $F$ + $M_t$.

---

## Materialni podatki

| Material | $E$ [kN/cm²] | $\sigma_{dop}$ [kN/cm²] | $\lambda_e$ |
|----------|--------------|------------------------|-------------|
| Les (iglavci) | 1 000 | 1,0–1,2 | 90–99 |
| Jeklo S235 | 21 000 | 16 | 114 |

---

## Pogosta napaka

- Vzeti $I_{max}$ namesto $I_{min}$ — **uklon vedno po šibki osi!**
- Pozabiti $\beta$ — privzeti $lu = L$ ko je konzola ($lu = 2L$)
- Ne preveriti pogoja Euler ($\lambda > \lambda_e$) — formula ne velja za kratke stebrovke!
- Enote: $E$ v kN/cm², $I$ v cm⁴, $lu$ v cm → $F_k$ v kN

---

## Povezave

- [[Koncept - Euler Uklon]] ← podrobna izpeljava
- [[Blok 1.5 - Geometrijske Karakteristike]] ← izračun I_min
- [[Blok 2 - Upogib]] ← kombinacija N+M
- [[Vaje - Trdnost in dimenzioniranje]] ← N2 (konzola, β=2), N6 (β=1)
- [[Naloga - Mehanika - Uklon lesene deske]] ← konzola β=2, I_min šibka os!
- [[Naloga - Mehanika - Uklon leseni steber F_max]] ← T-rama ravnotežje, Euler vs ω
- [[Naloga - Mehanika - Uklon palica S_dop]] ← jeklo I-prerez, λ=233 → Euler
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

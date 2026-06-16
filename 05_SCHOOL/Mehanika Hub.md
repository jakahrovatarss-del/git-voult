---
tags: [mehanika, hub, upogib, uklon, statika, kinematika]
predmet: Mehanika
datum: 2026-06-11
---

# Mehanika Hub

Centralna vstopna točka za vse vsebine predmeta Mehanika.

---

## Koncepti

| Koncept | Ključna formula | Status |
|---------|----------------|--------|
| [[Koncept - Upogib]] | $\sigma = M/W \leq \sigma_{dop}$ | ✅ razširjen |
| [[Koncept - Euler Uklon]] | $F_k = \pi^2 EI/l_u^2$ | ✅ razširjen |
| [[Koncept - Vztrajnostni moment]] | $I = \sum[I_i + A_i e_i^2]$ | ✅ razširjen |
| [[Koncept - Premo Gibanje]] | $v = dx/dt$, EPG enačbe | ✅ |
| [[Koncept - Zakoni Gibanja]] | $\sum F = ma$, Hooke, trenje | ✅ |

---

## Naloge

### Upogib
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] — pravokotnik, konzola, $q=5$ kN/m → **13×22 cm**
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] — U-prerez, previs+polje → **σ_max = 1,50 kN/cm²**

### Uklon
- [[Naloga - Mehanika - Uklon lesene deske]] — konzola ($\beta=2$) → $F_k = 0{,}524$ kN
- [[Naloga - Mehanika - Uklon leseni steber F_max]] — T-rama → $F_{max} = 11{,}84$ kN
- [[Naloga - Mehanika - Uklon palica S_dop]] — jeklo, triangularna konstr. → $S_{dop} = 23{,}4$ kN

---

## Izpit prep

- [[Izpit - Mehanika - Upogib]] — 7 tipov nalog s kompletnimi algoritmi

---

## SVG diagrami (Attachments)

- `[[Attachments/mehanika/m_diagram_predznak.svg]]` — sagging vs. hogging, napetosti
- `[[Attachments/mehanika/m_diagram_tipi.svg]]` — 4 tipični M diagrami
- `[[Attachments/mehanika/upogib_lesen_nosilec.svg]]` — previsni nosilci, pravokotni prerez
- `[[Attachments/mehanika/upogib_U_prerez_napetosti.svg]]` — U-prerez, asimetričen prerez
- `[[Attachments/mehanika/uklon_lesena_deska.svg]]` — 4 Eulerovi primeri

---

## Algoritem — Upogib (hitri pregled)

```
1. Statični sistem → reakcije (ΣF=0, ΣM=0)
2. M(x) funkcija → M diagram → M_max in predznak
3. Geometrija prereza → yT, J, e_zg, e_sp (Steiner za sestavljene)
4. σ = M·e/J ≤ σ_dop  ali  reši za neznanko
5. Zaokroži navzgor + kontrola
```

## Algoritem — Uklon (hitri pregled)

```
1. Vpetje → β → l_u = β·L
2. I_min (šibka os) → i = √(I/A) → λ = l_u/i
3. Preveri λ > λ_e? → Euler ali ω
4. F_k = π²EI/l_u²  →  F_dop = F_k/ν
5. Ravnotežje (če sila ni direktno vzdolž palice)
```

---

## Povezave

- [[mehanika]] — osnovna nota
- [[STATIKA]] — statika in ravnotežje
- [[05_SCHOOL/School Hub]] — hub vseh predmetov

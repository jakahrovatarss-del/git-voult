---
tags: [mehanika, izpit, cheat-sheet, celoletni, 2026]
predmet: Mehanika
datum: 2026-06-16
izpit-datum: 2026-06-19
---

# Izpit — Mehanika: Celoletni 2026 (Master Reference)

## Namen

> 📚 **MASTER PREP NOTA** — vsi algoritmi, vse enačbe, vsi bloki.
> Za kompakten cheat sheet na dan izpita → [[Izpit - Mehanika - Junij 2026]]

---

## Pregled vseh blokov

| Blok | Tema | Pogostost | Link |
|------|------|-----------|------|
| **0** | Statika (reakcije, paličje, trenje, 3D) | ⭐⭐⭐ | [[Blok 0 - Statika]] |
| **1** | N, T, M Diagrami | ⭐⭐⭐ | [[Blok 1 - NTM Diagrami]] |
| **1.5** | Geometrijske karakteristike (I, W, Steiner) | ⭐⭐⭐ | [[Blok 1.5 - Geometrijske Karakteristike]] |
| **2** | Upogib: Napetosti in dimenzioniranje | ⭐⭐⭐ | [[Blok 2 - Upogib]] |
| **2.5** | Deformacije pri upogibu (povesi, enačba) | ⭐⭐ | [[Blok 2.5 - Deformacije pri Upogibu]] |
| **3** | Napetostno stanje / Mohrova krožnica | ⭐⭐⭐ | [[Blok 3 - Napetostno Stanje]] |
| **3.5** | Hipoteze porušitve (Tresca, Von Mises) | ⭐⭐⭐ | [[Blok 3.5 - Hipoteze Porusitve]] |
| **4** | Euler Uklon | ⭐⭐ | [[Blok 4 - Euler Uklon]] |
| **5** | Torzija | ⭐⭐ | [[Blok 5 - Torzija]] |
| **6** | Kinematika | ⭐⭐ | [[Blok 6 - Kinematika]] |
| **7** | Dinamika in Nihanje | ⭐⭐ | [[Blok 7 - Dinamika Nihanje]] |

**Pričakovana struktura izpita (iz analize preteklih rokov):**
- N1: Statika (Blok 0) ali NTM diagrami (Blok 1)
- N2: NTM + Upogib (Blok 1 + 2), ali Deformacije (Blok 2.5)
- N3: Napetostno stanje / Mohr / VM / Tresca (Blok 3 + 3.5)
- N4: Euler uklon, Torzija ali Kinematika (Blok 4/5/6)

---

## BLOK 0 — Statika ⭐⭐⭐

**→ [[Blok 0 - Statika]] | [[STATIKA]]**

### Enačbe ravnotežja:

$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \quad \text{(2D)}$$

### Podpore:

| Podpora | Reakcije |
|---------|----------|
| Tečaj/pin | $A_x$, $A_y$ |
| Drsnik/valj | $B_y$ |
| Vpetje | $A_x$, $A_y$, $M_A$ |

### Paličje:
```
VOZLIŠČE: ΣFx=0, ΣFy=0 za vsako vozlišče
PREREZ:   Odreži 3 palice → 3 enačbe
          ΣM okrog presečišča 2 neznank → direktno 3.
```

### Trenje:
$$F_{tr} \leq \mu_s \cdot N, \qquad \tan\alpha \leq \mu_s$$

---

## BLOK 1 — N, T, M Diagrami ⭐⭐⭐

**→ [[Blok 1 - NTM Diagrami]] | [[Koncept - NTM Diagrami]]**

### Algoritem:

```
1. Reakcije: ΣFx=0, ΣFy=0, ΣM=0 pri podpori
2. Polja: razdeli na segmente
3. Rez na x → seštej levo: T(x) = ΣFy,levo, M(x) = ΣM_levo
4. T=0 → M_max (ekstremen)
5. Robni pogoji: M=0 pri prostem koncu, M=0 pri členku!
```

### Diferencialni odnosi:

$$\frac{dT}{ds} = -q, \qquad \frac{dM}{ds} = T$$

### Oblika diagrama po obtežbi:

| Obtežba | T(x) | M(x) |
|---------|------|------|
| Točkovna F | skok | prelom (kink) |
| Porazdeljena q | linearna | **parabola** |
| Točkovni M₀ | brez vpliva | skok |
| Brez obtežbe | konstantna | linearna |

### Tipični Mmax:

```
Prostoležeč q:     Mmax = qL²/8
Prostoležeč F sr.: Mmax = FL/4
Kombinacija q+F:   Mmax = qL²/8 + FL/4
Konzola F:         Mmax = F·L
Konzola q:         Mmax = qL²/2
```

> ⚠️ $M = 0$ pri **vsakem členku** in **prostem koncu**!

---

## BLOK 1.5 — Geometrijske karakteristike ⭐⭐⭐

**→ [[Blok 1.5 - Geometrijske Karakteristike]] | [[Koncept - Vztrajnostni moment]]**

### Težišče:

$$y_T = \frac{\sum A_i y_i}{\sum A_i}$$

### Vztrajnostni momenti:

| Prerez | $I_x$ | $W_x$ |
|--------|-------|-------|
| Pravokotnik $b \times h$ | $bh^3/12$ | $bh^2/6$ |
| Krog $d$ | $\pi d^4/64$ | $\pi d^3/32$ |
| Krog torzija | $I_p = \pi d^4/32$ | $W_t = \pi d^3/16$ |

### Steinerjev stavek:

$$\boxed{I = \sum\left(\frac{b_i h_i^3}{12} + A_i \cdot d_i^2\right)}, \quad d_i = y_i - y_T$$

### Asimetričen prerez:

$$W_{sp} = \frac{I}{e_{sp}}, \quad W_{zg} = \frac{I}{e_{zg}} \quad \Leftarrow \text{OBA! Kritičen je manjši!}$$

### Radij inercije (za uklon):

$$i = \sqrt{\frac{I_{min}}{A}} \quad \Rightarrow \quad \lambda = \frac{l_u}{i}$$

---

## BLOK 2 — Upogib: Napetosti ⭐⭐⭐

**→ [[Blok 2 - Upogib]] | [[Koncept - Upogib]]**

### Osnovna enačba:

$$\sigma = \frac{M \cdot e}{I} = \frac{M}{W} \leq \sigma_{dop}$$

### Dimenzioniranje:

$$W_{min} = \frac{M_{max}}{\sigma_{dop}}$$

| Prerez | Enačba | Rešitev |
|--------|--------|---------|
| $h = 2b$ | $W = 2b^3/3$ | $b = \sqrt[3]{3W_{min}/2}$ |
| Krog $d$ | $W = \pi d^3/32$ | $d = \sqrt[3]{32W_{min}/\pi}$ |

### Strig (Žuravski):

$$\tau = \frac{T \cdot S}{I \cdot b}, \qquad \text{Pravokotnik: } \tau_{max} = 1{,}5 \cdot \frac{T}{A}$$

### Ekscentrično (N + M):

$$\sigma_{max} = \frac{N}{A} - \frac{M}{W} \quad \text{(stran sile)}, \qquad \sigma_{min} = \frac{N}{A} + \frac{M}{W} \quad \text{⚠ NATEG možen!}$$

> ⚠️ **Enote:** $M$ v kNcm, $W$ v cm³, $\sigma$ v kN/cm² — ne mešaj m in cm!

---

## BLOK 2.5 — Deformacije pri upogibu ⭐⭐

**→ [[Blok 2.5 - Deformacije pri Upogibu]]**

### Diferencialna enačba:

$$EI \cdot y''(x) = M(x)$$

### Tipični povesi:

| Sistem | $y_{max}$ |
|--------|-----------|
| Konzola, $F$ na koncu | $FL^3/(3EI)$ |
| Konzola, $q$ | $qL^4/(8EI)$ |
| Prostoležeč, $F$ na sredini | $FL^3/(48EI)$ |
| Prostoležeč, $q$ | $5qL^4/(384EI)$ |
| Prostoležeč, $F$ na $a,b$ | $Fa^2b^2/(3EIL)$ |

### Robni pogoji:

```
Vpetje:   y = 0,  y' = 0
Členek:   y = 0
ymax:     kjer y'(x) = 0
```

### Superpozicija:

$$y_{skupni} = y_1 + y_2 + \ldots$$

---

## BLOK 3 — Napetostno stanje / Mohr ⭐⭐⭐

**→ [[Blok 3 - Napetostno Stanje]] | [[Koncept - Napetostno stanje]]**

### Algoritem:

```
1. Odčitaj σx, σy, τxy iz tenzorja σij
2. σsr = (σx+σy)/2
3. R = √[((σx-σy)/2)² + τxy²]
4. σ1 = σsr + R,  σ2 = σsr - R
5. τmax = R
6. φ0 = ½·arctan(2τxy/(σx-σy))
7. KONTROLA: σ1+σ2 = σx+σy  ← vedno!
```

### Posebni primeri:

| Stanje | σ₁ | σ₂ | τmax | φ₀ |
|--------|----|----|------|-----|
| Enoosno | σ | 0 | σ/2 | 45° |
| Čisto strižno | +τ | −τ | τ | 45° |
| σx=σy | σ | σ | 0 | — |

---

## BLOK 3.5 — Hipoteze porušitve ⭐⭐⭐

**→ [[Blok 3.5 - Hipoteze Porusitve]] | [[Koncept - Hipoteze Porusitve]]**

### Formule:

$$\sigma_{ekv,T} = \sigma_1 - \sigma_3 \quad \text{(Tresca)}$$

$$\sigma_{ekv,VM} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\right]} \quad \text{(Von Mises)}$$

**2D poenostavitev** ($\sigma$, $\tau$, ostalo 0):

$$\text{Tresca: } \sqrt{\sigma^2 + 4\tau^2}, \qquad \text{VM: } \sqrt{\sigma^2 + 3\tau^2}$$

> **TRIK:** Tresca = faktor **4** pred $\tau^2$, VM = faktor **3** pred $\tau^2$
> ⚠️ Razvrstiti: $\sigma_1 \geq \sigma_2 \geq \sigma_3$ je obvezno!

| | Tresca | Von Mises |
|--|--------|-----------|
| $\sigma_{ekv}$ | večji (bolj konzervativna) | manjši |
| Faktor | $4\tau^2$ | $3\tau^2$ |

---

## BLOK 4 — Euler Uklon ⭐⭐

**→ [[Blok 4 - Euler Uklon]] | [[Koncept - Euler Uklon]]**

### Eulerjeva sila:

$$F_k = \frac{\pi^2 E I_{min}}{l_u^2}, \qquad l_u = \beta L$$

### β tabela:

| Vpetje | $\beta$ |
|--------|---------|
| Oba členkovito | 1,0 |
| Spodaj vpeto, zgoraj členek | 0,7 |
| Oba vpeto | 0,5 |
| Spodaj vpeto, zgoraj **prosto** (konzola) | 2,0 |

### Vitkost in mejna vrednost:

$$\lambda = \frac{l_u}{i}, \qquad \lambda_e = \pi\sqrt{\frac{E}{\sigma_{dop}}}$$

- Jeklo: $\lambda_e \approx 114$; Les: $\lambda_e \approx 91$
- Euler velja samo za $\lambda > \lambda_e$!

$$\nu = \frac{F_k}{F} \geq \nu_{dop}$$

---

## BLOK 5 — Torzija ⭐⭐

**→ [[Blok 5 - Torzija]] | [[Koncept - Torzija]]**

### Polni krog:

$$\tau_{max} = \frac{M_t}{W_t}, \quad W_t = \frac{\pi d^3}{16} = 2W$$

$$\varphi = \frac{M_t \cdot L}{G \cdot I_p}, \quad I_p = \frac{\pi d^4}{32} = 2I$$

### Bredt (zaprti tankosteni profil):

$$\tau = \frac{M_t}{2 \cdot A_m \cdot t}, \quad A_m = \text{ploščina znotraj srednje linije}$$

### Kombinirano (M + Mt):

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2}, \quad \sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2}$$

---

## BLOK 6 — Kinematika ⭐⭐

**→ [[Blok 6 - Kinematika]] | [[Koncept - Kinematika Mehanizmi]]**

### Pol hitrosti:

```
1. Nariši smeri hitrosti znanih točk
2. Pravokotnice na smeri → presečišče = pol P
3. ω = v_A / r_PA,  v_B = ω · r_PB
```

### Kolo, ki se kotali:

$$v_{tal} = 0, \quad v_{sr} = \omega R, \quad v_{vrha} = 2v_{sr}$$

### Pospešek:

$$\vec{a}_B = \vec{a}_A + a_{B/A}^n + a_{B/A}^t$$
$$a^n = \omega^2 r \quad \text{(kaže v center)}, \quad a^t = \alpha r \quad \text{(⊥ na r)}$$

---

## BLOK 7 — Dinamika in Nihanje ⭐⭐

**→ [[Blok 7 - Dinamika Nihanje]]**

### Newton II:

$$\sum F = m \cdot a, \qquad \sum M_O = I_O \cdot \alpha$$

### Prosto nihanje:

$$m\ddot{x} + kx = 0 \quad \Rightarrow \quad \omega_0 = \sqrt{\frac{k}{m}}, \quad T_0 = \frac{2\pi}{\omega_0}$$

### Momenti inercije:

| Telo | Os | $I$ |
|------|----|-----|
| Palica $L$ | skozi konec | $mL^2/3$ |
| Palica $L$ | skozi sredino | $mL^2/12$ |
| Disk $R$ | os | $mR^2/2$ |

### Energijska metoda:

$$E_k = E_p \quad \Rightarrow \quad \frac{1}{2}mv^2 = \frac{1}{2}kx^2 \quad \Rightarrow \quad \omega_0 = \sqrt{k/m}$$

---

## Hitri seznam formul — VSI BLOKI

```
═══════════════════════════════════════════
BLOK 0 — STATIKA:
  ΣFx=0,  ΣFy=0,  ΣM_A=0
  Trenje: Ftr ≤ μN,  tan(α) ≤ μs

BLOK 1 — NTM:
  T(x) = ΣFy,levo,  M(x) = ΣM_levo
  dT/ds=-q,  dM/ds=T,  T=0 → Mmax
  M=0 pri prostem koncu in členku!
  Mmax: qL²/8,  FL/4,  F·L(konzola)

BLOK 1.5 — GEOMETRIJA:
  yT = ΣAiyi/ΣA
  I = Σ(bh³/12 + A·d²)  [Steiner!]
  W = I/emax  →  Wsp=I/esp, Wzg=I/ezg  OBA!
  i = √(I/A)  [za uklon]

BLOK 2 — UPOGIB:
  σ = M/W ≤ σdop
  Wmin = M/σdop
  h=2b: b=∛(3M/2σdop),  d=∛(32M/πσdop)
  τ = T·S/(I·b),  prav: τmax = 1.5T/A
  N+M: σ = N/A ± M/W  ⚠ NATEG možen!

BLOK 2.5 — DEFORMACIJE:
  EI·y'' = M(x),  y(0)=0,  y'(0)=0(vpetje)
  Konzola F: ymax = FL³/3EI
  Konzola q: ymax = qL⁴/8EI
  Prosl. F:  ymax = FL³/48EI
  Prosl. q:  ymax = 5qL⁴/384EI

BLOK 3 — NAPETOSTNO STANJE:
  σsr = (σx+σy)/2
  R = √[((σx-σy)/2)² + τxy²]
  σ1,2 = σsr ± R,  τmax = R
  φ0 = ½·arctan(2τxy/(σx-σy))
  KONTROLA: σ1+σ2 = σx+σy

BLOK 3.5 — PORUŠITEV:
  Tresca: σekv = σ1-σ3  →  2D: √(σ²+4τ²)
  VM:     σekv = √[½Σ(σi-σj)²]  →  2D: √(σ²+3τ²)
  TRIK: Tresca=4τ², VM=3τ²  ← zapomni!

BLOK 4 — EULER UKLON:
  Fk = π²EImin/lu²,  lu = β·L
  β: 0.5(oba vpeta), 0.7, 1.0(členki), 2.0(konzola)
  λe: jeklo≈114, les≈91
  ν = Fk/F ≥ νdop

BLOK 5 — TORZIJA:
  τ = Mt/Wt,  Wt = πd³/16 = 2W
  φ = Mt·L/(G·Ip),  Ip = πd⁴/32 = 2I
  BREDT (zaprti): τ = Mt/(2·Am·t)
  M+Mt: VM √(σ²+3τ²), Tresca √(σ²+4τ²)

BLOK 6 — KINEMATIKA:
  vB = ω · rPB  (od pola P)
  Kotaljenje: vpol=0, vsr=ωR, vvrha=2vsr
  an = ω²r (→ center),  at = α·r (⊥ r)

BLOK 7 — DINAMIKA/NIHANJE:
  ΣF = m·a,  ΣM = I·α
  ω₀ = √(k/m),  T₀ = 2π/ω₀
  Palica (konec): I = mL²/3
  Disk: I = mR²/2
═══════════════════════════════════════════
```

---

## Materialni podatki

| Material | $E$ [kN/cm²] | $\sigma_{dop}$ [kN/cm²] | $G$ [kN/cm²] | $\lambda_e$ |
|----------|-------------|------------------------|-------------|-------------|
| Les (iglavci) | 1 000 | 1,0 – 1,2 | — | ≈ 91–99 |
| Jeklo S235 | 21 000 | 16 | ≈ 8 077 | ≈ 114 |

---

## Pogosta napaka na izpitu

1. **Reakcije:** vodoravna sila ne prispeva k $\sum F_y$!
2. **M-diagram:** pozabiti preveriti $M=0$ pri prostem koncu in členu
3. **Asimetričen prerez:** preveriti **oba** roba ($W_{sp}$ in $W_{zg}$)
4. **Torzija:** $W_t = 2W$ za polni krog — ne $W_t = W$!
5. **Euler:** $I_{min}$ (ne max!) in pravilni $\beta$
6. **Tresca/VM:** razvrstiti $\sigma_1 \geq \sigma_2 \geq \sigma_3$ OBVEZNO
7. **Bredt $A_m$:** ploščina ZNOTRAJ SREDNJE LINIJE — ne zunanja!
8. **Enote:** vse v enakomernih enotah (kN/cm² ali MPa, ne mešati)

---

## Vzorci na izpitih

| Naloga | Jul 2018 | Feb 2019 |
|--------|----------|----------|
| N1 | Statika + NTM | Statika + NTM |
| N2 | Upogib (dimenzioniranje) | Upogib (Steiner) |
| N3 | Čisto strižno stanje (Mohr, φ₀=45°) | Tresca + Von Mises (3D) |
| N4 | Dimenzioniranje prereza (les, h:b=2:1) | Torzija Bredt (škatlast) |

---

## Povezave — vsi bloki

- [[Blok 0 - Statika]]
- [[Blok 1 - NTM Diagrami]]
- [[Blok 1.5 - Geometrijske Karakteristike]]
- [[Blok 2 - Upogib]]
- [[Blok 2.5 - Deformacije pri Upogibu]]
- [[Blok 3 - Napetostno Stanje]]
- [[Blok 3.5 - Hipoteze Porusitve]]
- [[Blok 4 - Euler Uklon]]
- [[Blok 5 - Torzija]]
- [[Blok 6 - Kinematika]]
- [[Blok 7 - Dinamika Nihanje]]
- [[Izpit - Mehanika - Junij 2026]] ← kompakten cheat sheet
- [[Mehanika Hub]]
- [[05_SCHOOL/School Hub]]

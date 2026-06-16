---
tags: [mehanika, izpit, cheat-sheet, celoletni, 2026]
predmet: Mehanika
datum: 2026-06-14
izpit-datum: 2026-06-19
---

# Izpit — Mehanika: Celoletni 2026 (19.6.2026)

## Analiza izpitnih nalog (iz IMG_1183.pdf)

Vsak izpit vsebuje tipično **3 naloge**:

| Naloga | Tema | Pogostost | Pripravljenost |
|--------|------|-----------|----------------|
| 1 | Kinematika ali Statika (reakcije) | ⭐⭐⭐ | 🟡 |
| 2 | N, T, M diagrami + upogibne napetosti | ⭐⭐⭐ | 🟢 |
| 3 | Napetostno stanje (tenzor → Mohr → σ₁,₂) | ⭐⭐⭐ | 🟡 |

**Dodatno (manj pogosto):** Euler uklon, torzija, elastična linija, togo telo (kinematika)

---

## BLOK 1 — N, T, M Diagrami ⭐⭐⭐

**→ [[Koncept - NTM Diagrami]]**

### Hitra formula:

```
1. Reakcije: ΣFx=0, ΣFy=0, ΣM=0 pri podpori
2. Rez na x → seštej levo: T(x) = ΣFy,levo, M(x) = ΣM_levo
3. T=0 → M_max (ekstremen)
4. Robni pogoji: M=0 pri prostem koncu, M=0 pri členku
```

### Oblika diagrama po obtežbi:

| Obtežba | T(x) | M(x) |
|---------|------|------|
| Točkovna F | skok | prelom |
| Porazdeljena q | linearna | parabola |
| Točkovni M₀ | brez vpliva | skok |

### Predznaki:

- $T > 0$: levi del ↑ (ali desni del ↓)
- $M > 0$: sagging (upogib navzdol, spodaj nateg)

> ⚠️ $M = 0$ pri **vsakem členku** in **prostem koncu**!

---

## BLOK 2 — Upogib: Napetosti ⭐⭐⭐

**→ [[Koncept - Upogib]] | [[Izpit - Mehanika - Upogib]]**

### Osnovna enačba:

$$\sigma = \frac{M \cdot e}{I} = \frac{M}{W} \leq \sigma_{dop}$$

### Formule za prereze:

| Prerez | $I_x$ | $W_x$ | $e$ |
|--------|--------|--------|-----|
| Pravokotnik $a \times b$ ($b$ = višina) | $ab^3/12$ | $ab^2/6$ | $b/2$ |
| Krog $d$ | $\pi d^4/64$ | $\pi d^3/32$ | $d/2$ |
| Votel pravokotnik $BH - bh$ | $(BH^3-bh^3)/12$ | $(BH^3-bh^3)/6H$ | $H/2$ |
| Sestavljeni | $\sum(I_i + A_i e_i^2)$ | $I/e_{max}$ | $H-y_T$ |

**Steiner:** $I_{x_T} = \sum\left[\frac{a_i b_i^3}{12} + A_i(y_i - y_T)^2\right]$

**Težišče:** $y_T = \frac{\sum A_i y_i}{\sum A_i}$

### Dimenzioniranje:

$$W_{min} = \frac{M_{max}}{\sigma_{dop}}, \qquad d = \sqrt[3]{\frac{32 M_{max}}{\pi \sigma_{dop}}}$$

> ⚠️ Pri **asimetričnem prerezu** (U, C, T): preveriti $\sigma$ pri **obeh** robih ($e_{zg}$, $e_{sp}$) **v vsakem kritičnem prerezu**!

---

## BLOK 3 — Napetostno stanje / Mohr ⭐⭐⭐

**→ [[Koncept - Napetostno stanje]]**

### Vhod: $\sigma_x$, $\sigma_y$, $\tau_{xy}$

### Formule:

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2}, \qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

$$\boxed{\sigma_{1,2} = \sigma_{sr} \pm R}, \qquad \boxed{\tau_{max} = R}$$

$$\boxed{\varphi_0 = \frac{1}{2}\arctan\frac{2\tau_{xy}}{\sigma_x - \sigma_y}}$$

### Algoritem:

```
1. Izpiši σx, σy, τxy iz tenzorja σij
2. σsr = (σx+σy)/2
3. R = √[((σx-σy)/2)² + τxy²]
4. σ1 = σsr + R,  σ2 = σsr - R
5. τmax = R
6. φ0 = ½·arctan(2τxy / (σx-σy))
7. Kontrola: σ(φ0) = σ1 ali σ2?
```

### Posebni primeri:

| Stanje | σ₁ | σ₂ | τmax | φ₀ |
|--------|----|----|------|-----|
| Enoosno | σ | 0 | σ/2 | 45° |
| Čisto strižno | +τ | −τ | τ | 45° |
| σx=σy | σ | σ | 0 | — |

---

## BLOK 3.5 — Hipoteze porušitve ⭐⭐⭐

**→ [[Koncept - Hipoteze Porusitve]] | [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]]**

### Algoritem:

```
1. Iz σij izračunaj σ1 ≥ σ2 ≥ σ3 (Mohrova metoda ali lastne vrednosti)
2. Tresca:    σ_ekv = σ1 − σ3  (max − min!)
3. Von Mises: σ_ekv = √[½((σ1−σ2)²+(σ2−σ3)²+(σ3−σ1)²)]
4. Preveri: σ_ekv ≤ σ_dop?
```

### Formule:

$$\boxed{\sigma_{ekv,T} = \sigma_1 - \sigma_3}$$

$$\boxed{\sigma_{ekv,VM} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2\right]}}$$

**2D poenostavitev** ($\sigma_x = \sigma$, $\tau_{xy} = \tau$, ostalo 0):

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2}$$

### Primerjava:

| | Tresca | Von Mises |
|--|--------|-----------|
| σ_ekv | **večji** (bolj konzervativna) | manjši |
| Osnova | max strižna napetost | energija oblike |
| Za izpit | pogosteje zavrne | bliže eksperimentu |

> ⚠️ **Razvrstitev σ₁ ≥ σ₂ ≥ σ₃ je obvezna!** — $\sigma_z = 0$ ni nujno $\sigma_3$!
>
> **Primer (Feb 2019):** σ₁=+385.4, σ₂=0, σ₃=−285.4 MPa → Tresca=670.8 MPa ❌, Von Mises=583.1 MPa ✓

---

## BLOK 4 — Euler Uklon ⭐⭐

**→ [[Koncept - Euler Uklon]]**

### Eulerjeva sila:

$$F_k = \frac{\pi^2 E I_{min}}{l_u^2}$$

### Uklonska dolžina:

| Vpetje | $\beta$ | $l_u = \beta L$ |
|--------|---------|----------------|
| Oba členkovito | 1,0 | $L$ |
| Spodaj vpeto, zgoraj členk | 0,7 | $0{,}7L$ |
| Oba vpeto | 0,5 | $0{,}5L$ |
| Spodaj vpeto, zgoraj prosto | 2,0 | $2L$ |

### Varnostni faktor:

$$S_{ukl} = \frac{F_k}{F_{max}} \geq S_{dop}$$

---

## BLOK 5 — Torzija ⭐⭐

**→ [[Koncept - Torzija]]**

### Napetost in zasuk:

$$\tau_{max} = \frac{M_t}{W_t}, \qquad W_t = \frac{\pi d^3}{16} \quad \text{(polni krog)}$$

$$\varphi = \frac{M_t \cdot L}{G \cdot I_p}, \qquad I_p = \frac{\pi d^4}{32}$$

$$G_{jeklo} \approx 80\ 000\ \text{MPa} = 8 \cdot 10^4\ \text{kN/cm}^2$$

### Tankosteni zaprti prerezi — Bredt:

$$\boxed{\tau = \frac{M_t}{2 \cdot A_m \cdot t}}$$

- $A_m$ = ploščina znotraj **srednje linije** (ne zunanja, ne notranja kontura!)
- Škatlast prerez $B \times H$, debelina $t$: $A_m = (B-t)(H-t)$
- Ko $t = \text{konst.}$: $\tau = \text{konst.}$ po vsem obodu

> **Primer (Feb 2019):** $10 \times 15$ cm, $t=1$ cm → $A_m = 9 \times 14 = 126\ \text{cm}^2$, $M_t=3\ \text{kNm}$ → $\tau=11{,}9\ \text{MPa}$

### Kombinirano (upogib + torzija):

$$\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop}$$

---

## BLOK 6 — Kinematika ⭐

**→ [[Koncept - Kinematika Mehanizmi]]**

### Pol hitrosti:

1. Nariši smeri hitrosti znanih točk
2. Pravokotnice na smeri → presečišče = pol P
3. $\omega = v_A / r_{PA}$, $v_B = \omega \cdot r_{PB}$

### Kolo, ki se kotali:

$$\omega = \frac{v_{sr}}{R}, \qquad v_{vrha} = 2 v_{sr}, \qquad v_{tal} = 0$$

---

## Hitri seznam formul (za prepisati na list)

```
═══════════════════════════════════════════
STATIKA (reakcije):
  ΣFx=0,  ΣFy=0,  ΣM_A=0
  M=0 pri prostem koncu in členku!

N,T,M (rez, seštejem levo):
  T(x) = ΣFy,levo
  M(x) = Σ(F·ročica) levo

UPOGIB:
  σ = M·e/I = M/W ≤ σ_dop
  W_krog = πd³/32,  I_krog = πd⁴/64
  W_prav = ab²/6,   I_prav = ab³/12
  d = ∛(32M/πσ_dop)

STEINER: I = Σ(Ii + Ai·ei²)
  yT = Σ(Ai·yi) / ΣAi

NAPETOSTNO STANJE:
  σsr = (σx+σy)/2
  R = √[((σx-σy)/2)² + τxy²]
  σ1,2 = σsr ± R
  τmax = R
  φ0 = ½·arctan(2τxy/(σx-σy))

EULER UKLON:
  Fk = π²EI/lu²
  lu: β=1(členki), 0.7, 0.5, 2.0(prosto)

TORZIJA:
  τ = Mt/Wt,  Wt = πd³/16  (polni krog)
  φ = Mt·L/(G·Ip),  Ip = πd⁴/32
  σekv = √(σ²+3τ²)
  BREDT (zaprti tankosteni): τ = Mt/(2·Am·t)
    Am = ploščina znotraj srednje linije!

HIPOTEZE PORUŠITVE:
  σ1 ≥ σ2 ≥ σ3  ← razvrstiti OBVEZNO!
  Tresca:    σekv = σ1 − σ3
  Von Mises: σekv = √[½((σ1−σ2)²+(σ2−σ3)²+(σ3−σ1)²)]
  2D: σekv = √(σ²+3τ²)
  Tresca > Von Mises → Tresca bolj konzervativna
═══════════════════════════════════════════
```

---

## Pogosta napaka na izpitu

1. **Reakcije:** vodoravna sila ne prispeva k $\sum F_y$!
2. **M-diagram:** pozabiti preveriti robne pogoje (M=0 pri prostem koncu)
3. **Asimetričen prerez:** preveriti oba roba, ne samo kjer je $|M|$ max
4. **Napetostni tenzor:** $\tau_{xy}$ je nediago­nalnih — paziti na predznak!
5. **Euler:** $I_{min}$ (ne max!) in pravilni $\beta$
6. **Enote:** vse v enakomernih enotah! (kN/cm² ali MPa, ne mešati)
7. **Tresca/Von Mises:** $\sigma_z = 0$ ni nujno $\sigma_3$ — razvrstiti $\sigma_1 \geq \sigma_2 \geq \sigma_3$ najprej!
8. **Bredt $A_m$:** ploščina ZNOTRAJ SREDNJE LINIJE — ne zunanja ($B \times H$) in ne notranja!

---

## Vzorci na izpitih (Jul 2018 + Feb 2019)

| Naloga | Jul 2018 | Feb 2019 |
|--------|----------|----------|
| N1 | Statika + NTM | Statika + NTM |
| N2 | Upogib (dimenzioniranje) | Upogib (Steiner) |
| N3 | **Čisto strižno stanje** (Mohr, φ₀=45°) | **Tresca + Von Mises** (3D tenzor) |
| N4 | Dimenzioniranje prereza (les, h:b=2:1) | **Torzija Bredt** (škatlast prerez) |

**Pogoste teme na izpitu:**
- NTM diagrami (vsak izpit!)
- Upogib / Steiner / dimenzioniranje (vsak izpit!)
- Napetostno stanje / Mohr — pogosto
- Tresca/Von Mises + Bredt torzija — pojavljata se skupaj (2019)

---

## Viri

| Tema | Obsidian nota | PDF vir |
|------|--------------|---------|
| N, T, M | [[Koncept - NTM Diagrami]] | NotrSileVaje (1).pdf |
| Upogib | [[Koncept - Upogib]], [[Izpit - Mehanika - Upogib]] | IMG_1241.pdf |
| Napetostno stanje | [[Koncept - Napetostno stanje]] | IMG_1183.pdf str. 1-2 |
| Euler uklon | [[Koncept - Euler Uklon]] | IMG_1241.pdf |
| Torzija | [[Koncept - Torzija]] | IMG_1183.pdf str. 50 |
| Bredt torzija | [[Naloga - Mehanika - Izpit Feb2019 - Torzija Bredt skatlast]] | — |
| Hipoteze porušitve | [[Koncept - Hipoteze Porusitve]] | — |
| Kinematika | [[Koncept - Kinematika Mehanizmi]] | IMG_1183.pdf str. 14-15 |
| Vztrajnostni moment | [[Koncept - Vztrajnostni moment]] | IMG_1241.pdf |

---

## Povezave

- [[Koncept - NTM Diagrami]]
- [[Koncept - Upogib]]
- [[Koncept - Napetostno stanje]]
- [[Koncept - Torzija]]
- [[Koncept - Euler Uklon]]
- [[Koncept - Kinematika Mehanizmi]]
- [[Koncept - Vztrajnostni moment]]
- [[Izpit - Mehanika - Upogib]]
- [[Mehanika Hub]]
- [[05_SCHOOL/School Hub]]

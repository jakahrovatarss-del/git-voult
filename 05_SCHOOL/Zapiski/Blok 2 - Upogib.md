---
tags: [mehanika, upogib, napetosti, dimenzioniranje, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 2 — Upogib: Napetosti in Dimenzioniranje

## VSE ENAČBE

```
NORMALNA NAPETOST PRI UPOGIBU:
  σ(z) = My / Iy · z
  σmax = Mmax / W  ≤ σdop

ODPORNOSTNI MOMENTI:
  Pravokotnik b×h:   W = b·h²/6
  Krog d:             W = π·d³/32
  h=2b:               W = 2b³/3

DIMENZIONIRANJE:
  Wmin = Mmax / σdop
  h=2b:  b = ∛(3Wmin/2)
  krog:  d = ∛(32M / π·σdop)

STRIG PRI UPOGIBU (Žuravski):
  τ = T·S / (I·b)
  Pravokotnik: τmax = 1.5·T/A   (v nevtralni osi)

EKSCENTRIČNO (N + M):
  σmax = N/A - M/W   (stran sile = VEČJA tlačna)
  σmin = N/A + M/W   ⚠ mogoč NATEG!

MATERIALNI PODATKI:
  Les:   E=1000 kN/cm²,  σdop = 1.0–1.2 kN/cm²
  Jeklo: E=21000 kN/cm², σdop = 16 kN/cm²
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "preveri trdnost", "dimenzioniranje prereza"
- "dopustna napetost $\sigma_{dop}$"
- "določi $b$ in $h$", "minimalni prerez"
- "pravokoten prerez $h = 2b$"
- Podano: $M_{max}$ ali celoten nosilec z obtežbo

**Kaj je podano:**
- $M_{max}$ [kNm ali kNcm] — ali računamo sami iz bloka 1
- Oblika prereza: $h = 2b$, krog, T-prerez...
- Material: $\sigma_{dop}$ [kN/cm²]

**Kaj se sprašuje:**
- Minimalne dimenzije prereza ($b$, $h$, $d$)
- Maksimalna napetost $\sigma_{max}$
- Ali je prerez ustrezen ($\sigma_{max} \leq \sigma_{dop}$)

---

## Kako začeti reševati

**Korak 1 — Poišči $M_{max}$** (iz Blok 1 ali formula):

| Sistem | $M_{max}$ |
|--------|-----------|
| Prostoležeč $q$ | $qL^2/8$ |
| Prostoležeč $F$ sr. | $FL/4$ |
| Konzola $F$ | $FL$ |
| Konzola $q$ | $qL^2/2$ |

> ⚠️ **Enote:** $M$ v kNcm (prevedi m→cm, krat 100)!

**Korak 2 — Izračunaj $W_{min}$:**
$$W_{min} = \frac{M_{max}}{\sigma_{dop}}$$

**Korak 3 — Dimenzioniranje iz oblike prereza:**

| Prerez | Enačba | Rešitev |
|--------|--------|---------|
| $h = 2b$ | $W = 2b^3/3$ | $b = \sqrt[3]{3W_{min}/2}$ |
| Krog $d$ | $W = \pi d^3/32$ | $d = \sqrt[3]{32W_{min}/\pi}$ |

**Korak 4 — Zaokroži navzgor** (na mm ali cm) in **kontroliraj:**
$$\sigma_{dej} = \frac{M_{max}}{W_{dej}} \leq \sigma_{dop} \quad ✓$$

---

## Asimetričen prerez — Steiner postopek

Velja za T-, L-, U-prereze:

1. $y_T = \sum A_i y_i / \sum A_i$
2. $J = \sum (b_i h_i^3/12 + A_i d_i^2)$, kjer $d_i = y_i - y_T$
3. $W_{sp} = J / e_{sp}$, $W_{zg} = J / e_{zg}$
4. Preveri **oba roba**: $\sigma = M / W$ — kritičen je **manjši $W$**!

---

## Strižne napetosti pri upogibu (Žuravski)

$$\tau = \frac{T \cdot S}{I \cdot b}$$

- $S$ = statični moment dela prereza nad točko
- Za **pravokotnik** — maksimum v nevtralni osi:

$$\tau_{max} = 1{,}5 \cdot \frac{T}{A}$$

- Za **I-profil** — maksimum v stojini:

$$\tau_{max} = \frac{T \cdot S_{max}}{I \cdot t_{stojine}}$$

---

## Ekscentrična obremenitev (N + M)

$$\sigma = \frac{N}{A} \pm \frac{M}{W}$$

| Stran | Enačba | Opomba |
|-------|--------|--------|
| Stran sile (večji tlak) | $\sigma_{max} = N/A - M/W$ | Tlak = negativno |
| Nasprotna stran | $\sigma_{min} = N/A + M/W$ | Lahko NATEG! |

> ⚠️ Kljub tlačni sili $N$ se na nasprotni strani pojavi **nateg** — morda nevaren za beton/les!

---

## Diferencialna enačba upogibnice

$$EI \cdot y'' = M(x) \quad \Rightarrow \quad y(x) = \frac{1}{EI} \iint M(x)\, dx^2 + C_1 x + C_2$$

Konstanti iz robnih pogojev:
- Prostoležeč: $y = 0$ pri obeh podporah
- Vpetje: $y = 0$, $y' = 0$

→ **Podrobneje:** [[Blok 2.5 - Deformacije pri Upogibu]]

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Posebnost |
|-----|----------------|-----------|
| Dimenzioniranje $h=2b$ | "pravokoten prerez", "les" | $b = \sqrt[3]{3W/2}$ |
| T-prerez Steiner | "varjeni prerez", "T-profil" | OBA $W$! |
| Ekscentrično N+M | "steber", "ekscentrično" | NATEG možen! |
| Strig preverjanje | "strižna napetost", "strig" | Žuravski |
| Krog $d$ | "okrogel", "gredi" | $W = \pi d^3/32$ |

---

## Kombinacije z drugimi bloki

### Blok 1 + 2 (NTM → Upogib) ← **OSNOVA**
Najpogostejši zaporedje:
1. Reakcije (Blok 0)
2. $M_{max}$ (Blok 1)
3. $W_{min}$, dimenzije (Blok 2)

### Blok 1.5 + 2 (Steiner + Upogib)
T-prerez: najprej Steiner → $J$, $W_{sp}$, $W_{zg}$, nato $\sigma$.

### Blok 2 + 3.5 (Upogib + VM/Tresca)
Gredi: $\sigma = M/W$ iz upogiba, $\tau = Mt/Wt$ iz torzije → VM.

### Blok 2 + 4 (Upogib + Euler Uklon)
Steber z ekscentrično obremenitvijo: N+M kombinacija + uklon kontrola.

---

## Materialni podatki

| Material | $\sigma_{dop}$ [kN/cm²] | $E$ [kN/cm²] |
|----------|------------------------|--------------|
| Les (iglavci) | 1,0 – 1,2 | 1 000 |
| Jeklo S235 | 16 | 21 000 |
| Beton (tlak) | 1,5 – 2,5 | 3 000 |

---

## Profesorjev »ček-list«

1. ⚠️ **Enote:** $M$ v kNcm, $W$ v cm³, $\sigma$ v kN/cm² — ne mešaj m in cm!
2. $M_{max}$: tam kjer $T = 0$
3. Asimetričen prerez: **oba** $W$, kritičen je **manjši**
4. $h = 2b$: najpogostejša lesarska naloga — $W = 2b^3/3$

---

## Povezave

- [[Koncept - Upogib]] ← podrobna razlaga
- [[Blok 1.5 - Geometrijske Karakteristike]] ← I in W prereza
- [[Blok 2.5 - Deformacije pri Upogibu]] ← povesi
- [[Blok 3 - Napetostno Stanje]] ← kombinirana napetostna stanja
- [[Blok 3.5 - Hipoteze Porusitve]] ← VM, Tresca
- [[Vaje - Trdnost in dimenzioniranje]] ← N1 (h=2b), N3 (T-prerez), N4 (N+M)
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

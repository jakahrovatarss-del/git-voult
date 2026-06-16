---
tags: [mehanika, napetostno-stanje, mohr, tenzor, glavne-napetosti, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 3 — Napetostno Stanje in Mohrova Krožnica

## VSE ENAČBE

```
NAPETOSTNI TENZOR 3D:
  σij = | σx  τxy τxz |
        | τyx σy  τyz |
        | τzx τzy σz  |
  (SIMETRIJA: τxy=τyx, τxz=τzx, τyz=τzy)

NAPETOSTNI TENZOR 2D (ravninsko stanje):
  σij = | σx   τxy |
        | τyx  σy  |

NAPETOSTNI VEKTOR NA RAVNINI (normala n = cosα, cosβ, cosγ):
  px = σx·cosα + τyx·cosβ + τzx·cosγ
  py = τxy·cosα + σy·cosβ + τzy·cosγ
  pz = τxz·cosα + τyz·cosβ + σz·cosγ
  σn = p⃗ · n⃗  (normalna napetost)
  τn = √(|p⃗|² - σn²)  (strižna napetost)

GLAVNE NAPETOSTI 2D:
  σ1,2 = (σx+σy)/2 ± √[((σx-σy)/2)² + τxy²]
  σ1 ≥ σ2 ≥ σ3 = 0  (ravninsko stanje)

MOHROVA KROŽNICA:
  σsr = (σx + σy) / 2
  R   = √[((σx-σy)/2)² + τxy²]
  σ1  = σsr + R    (max normalna)
  σ2  = σsr - R    (min normalna)
  τmax = R

RISANJE MOHROVE KROŽNICE:
  Točka Px = (σx, -τxy)   ← konvencija: τ navzdol za x-ploskev
  Točka Py = (σy, +τxy)
  Središče S = ((σx+σy)/2, 0)
  Krožnica skozi Px in Py → presek z osjo σ = σ1, σ2

KOT ZASUKA DO GLAVNIH RAVNIN:
  tan(2φ) = 2τxy / (σx - σy)   → φ0 = ½·arctan(...)

NAPETOSTI NA RAVNINI POD KOTOM φ:
  σ(φ) = (σx+σy)/2 + (σx-σy)/2·cos(2φ) + τxy·sin(2φ)
  τ(φ) = -(σx-σy)/2·sin(2φ) + τxy·cos(2φ)

PRVA INVARIANTA (kontrola 3D):
  I1 = σx + σy + σz = σ1 + σ2 + σ3  ← nespremenljiva pri zasuku!

KONTROLA 2D (INVARIANTA):
  σ1 + σ2 = σx + σy   ← OBVEZNO preveri!

HOOKE-OV ZAKON 2D:
  εx = (σx - ν·σy) / E
  εy = (σy - ν·σx) / E
  γxy = τxy / G
  G = E / (2(1+ν))

HOOKE-OV ZAKON 3D (Laméjeve konstante):
  λ = E·ν / ((1-2ν)(1+ν))   ... Laméjeva konstanta
  G = E / (2(1+ν))           ... strižni modul
  εv = εx + εy + εz          ... volumska dilatacija
  σi = λ·εv + 2G·εi          ... (za i = x, y, z)
  τij = 2G·εij               ... strižne napetosti
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "napetostni tenzor", "komponente napetosti"
- "Mohrova krožnica", "nariši Mohrovo krožnico"
- "glavne napetosti", "σ1, σ2"
- "maksimalna strižna napetost"
- "ravnina pod kotom $\phi$"
- Podano: $\sigma_x$, $\sigma_y$, $\tau_{xy}$ — ali geometrija in obremenitev

**Kaj je podano:**
- Napetostni tenzor: $\sigma_x$, $\sigma_y$, $\tau_{xy}$
- Ali: konstrukcija → izračunaj σ in τ (iz Blok 1 + 2)

**Kaj se sprašuje:**
- Glavne napetosti $\sigma_1$, $\sigma_2$
- $\tau_{max}$
- Kot $\phi_0$ do glavnih ravnin
- Napetosti na ravnini pod kotom $\phi$
- Nariši Mohrovo krožnico

---

## Kako začeti reševati

**Korak 1 — Odčitaj tenzor:**

| Napetost | Vrednost | Opomba |
|----------|----------|--------|
| $\sigma_x$ | normalna v smeri x | pozitivna = nateg |
| $\sigma_y$ | normalna v smeri y | |
| $\tau_{xy}$ | strižna | paziti na predznak! |

**Korak 2 — Središče Mohrove krožnice:**
$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2}$$

**Korak 3 — Radij:**
$$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

**Korak 4 — Glavne napetosti:**
$$\sigma_1 = \sigma_{sr} + R, \qquad \sigma_2 = \sigma_{sr} - R$$

**Korak 5 — Kontrola:**
$$\sigma_1 + \sigma_2 \stackrel{?}{=} \sigma_x + \sigma_y \quad ✓$$

**Korak 6 — Kot in $\tau_{max}$:**
$$\tau_{max} = R, \qquad \phi_0 = \frac{1}{2} \arctan\frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

---

## 3D Napetostno Stanje — Karakteristična Enačba

Za 3D tenzor določimo glavne napetosti iz kubične enačbe:
$$\sigma^3 - I_1\sigma^2 + I_2\sigma - I_3 = 0$$

kjer je $I_1 = \sigma_x + \sigma_y + \sigma_z$ (prva invarianta).

Rešitve razvrstimo: $\sigma_1 \geq \sigma_2 \geq \sigma_3$.

V **ravninskem stanju** ($\sigma_z = 0$): tretja rešitev $\sigma_3 = 0$ — ne pozabiti pri VM/Tresca!

---

## Posebni napetostni primeri — Hitri rezultati

| Stanje | $\sigma_x$ | $\sigma_y$ | $\tau_{xy}$ | $\sigma_1$ | $\sigma_2$ | $\tau_{max}$ | $\phi_0$ |
|--------|-----------|-----------|-----------|----------|----------|------------|---------|
| Enoosno | $\sigma$ | 0 | 0 | $\sigma$ | 0 | $\sigma/2$ | 45° |
| Dvoosno enako | $\sigma$ | $\sigma$ | 0 | $\sigma$ | $\sigma$ | 0 | — |
| Čisto strižno | 0 | 0 | $\tau$ | $+\tau$ | $-\tau$ | $\tau$ | 45° |
| Hidrostatično tlačno | $-p$ | $-p$ | 0 | $-p$ | $-p$ | 0 | — |

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Posebnost |
|-----|----------------|-----------|
| Tenzor direktno dan | Podano $\sigma_x$, $\sigma_y$, $\tau_{xy}$ | Direktno v Mohr |
| Iz obremenitve | Podano F, M, Mt → najprej izračunaj napetosti | Blok 1+2+5 → Blok 3 |
| Enoosno stanje | $\sigma_y = 0$, $\tau = 0$ | Trivial: $\sigma_1 = \sigma$, $\sigma_2 = 0$ |
| Ravnina pod kotom | "Izračunaj napetosti na ravnini pod $\phi$°" | Transformacijska formula |
| 3D tenzor | 3×3 matrika | Lastne vrednosti (po potrebi) |

---

## Kombinacije z drugimi bloki

### Blok 2 + 3 (Upogib → Tenzor)
Gredi pod upogibom: $\sigma = M/W$ (normalna), $\tau = T \cdot S / (I \cdot b)$ (strižna).
→ Sestavi tenzor, poišči $\sigma_1$, $\sigma_2$.

### Blok 3 + 3.5 (Mohr → Porušitev) ← **NAJPOGOSTEJŠE SKUPAJ**
Ko imaš $\sigma_1$, $\sigma_2$ → vstavi v VM ali Tresca.

### Blok 5 + 3 (Torzija → Tenzor)
Čisto torzijsko stanje: $\tau_{xy} = \tau$, $\sigma_x = \sigma_y = 0$ → $\sigma_{1,2} = \pm \tau$, $\phi_0 = 45°$.

### Blok 2 + 5 + 3 + 3.5 (Kombinirana gredi)
Celoten postopek za gredi:
1. $M_{max}$ (Blok 1)
2. $\sigma = M/W$, $\tau = Mt/Wt$ (Blok 2 + 5)
3. Tenzor → $\sigma_1$, $\sigma_2$ (Blok 3)
4. VM/Tresca → $\sigma_{ekv}$ (Blok 3.5)

---

## Hitri seznam formul

```
σsr = (σx+σy)/2
R   = √[((σx-σy)/2)² + τxy²]
σ1  = σsr + R,   σ2 = σsr - R
τmax = R
φ0  = ½·arctan(2τxy/(σx-σy))

KONTROLA: σ1+σ2 = σx+σy  ← OBVEZNO!

ČISTO STRIG: σ1=+τ, σ2=−τ, φ0=45°
ENOOSNO:     σ1=σ, σ2=0,   τmax=σ/2
```

---

## Pogosta napaka

- Napačen predznak $\tau_{xy}$ pri odčitavanju tenzorja
- Pozabiti preveriti invarianto $\sigma_1 + \sigma_2 = \sigma_x + \sigma_y$
- $\phi_0$ je kot zasuka v **fizičnem prostoru** = polovica kota na Mohrovi krožnici
- Za 3D problem: $\sigma_3 = 0$ (ravninsko stanje) — ne pozabiti pri VM!

---

## Povezave

- [[Koncept - Napetostno stanje]] ← podrobna razlaga + Mohr
- [[Blok 3.5 - Hipoteze Porusitve]] ← naslednji korak (Tresca, Von Mises)
- [[Blok 2 - Upogib]] ← od kje pridejo σ in τ
- [[Blok 5 - Torzija]] ← torzijsko strižno stanje
- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← rešene naloge
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

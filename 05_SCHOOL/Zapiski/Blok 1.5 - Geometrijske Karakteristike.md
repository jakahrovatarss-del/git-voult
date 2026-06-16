---
tags: [mehanika, geometrija, prerezi, vztrajnostni-moment, težišče, steiner, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 1.5 — Geometrijske Karakteristike Prereza

## VSE ENAČBE

```
TEŽIŠČE:
  yT = ΣAi·yi / ΣA,   xT = ΣAi·xi / ΣA

AKSIALNI I (standardni prerezi, težiščna os):
  Pravokotnik b×h:  Ix = b·h³/12,   Iy = h·b³/12
  Krog d:           Ix = Iy = π·d⁴/64
  Votli krog:       Ix = π(dz⁴-dn⁴)/64

STEINERJEV STAVEK:
  Ix = Σ(Ix,i + Ai·Δyi²)
  Iy = Σ(Iy,i + Ai·Δxi²)

ODPORNOSTNI MOMENT:
  W = I / zmax    [cm³]
  Pravokotnik:     W = b·h²/6
  Krog:            W = π·d³/32
  Asimetričen:     Wsp = J/esp,  Wzg = J/ezg   ← OBA!

POLARNI IN TORZIJSKI:
  Ip = Ix + Iy
  Krog:  Ip = π·d⁴/32,   Wt = π·d³/16 = 2·W

RADIJ INERCIJE (za uklon):
  i = √(I/A)    ← iščemo imin!

DEVIACIJSKI MOMENT:
  Ixy = Σ(Ai·Δxi·Δyi)   ← za nesim. prereze

GLAVNI VZTRAJNOSTNI MOMENTI:
  I1,2 = (Ix+Iy)/2 ± √[((Ix-Iy)/2)² + Ixy²]
  tan(2α) = -2Ixy / (Ix-Iy)

STATIČNI MOMENT (za τ pri upogibu):
  S = A'·yT'   (A' = del prereza nad točko, yT' = težišče tega dela od skupnega T)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "izračunaj težišče", "določi I", "odpornostni moment"
- "T-prerez", "L-prerez", "sestavljen prerez"
- "Steinerjev stavek", "lastnosti prereza"
- Podano: skica prereza z dimenzijami

**Kdaj ga potrebujemo (posredno):**
- Vsakič pred Blok 2 (upogib): potrebujemo $W$
- Pred Blok 4 (uklon): potrebujemo $I_{min}$ in $i$
- Pred Blok 5 (torzija): potrebujemo $I_p$ in $W_t$

---

## Kako začeti reševati — Postopek (Tabela)

**Sestavljen prerez vedno rešuj s tabelo:**

| Del | $A_i$ [cm²] | $y_i$ [cm] | $A_i y_i$ | $I_{x0,i}$ | $A_i \cdot d_i^2$ | $I_{x,i}$ |
|-----|------------|------------|-----------|------------|-------------------|-----------|
| Del 1 | ... | ... | ... | $bh^3/12$ | $A(y_i-y_T)^2$ | Σ |
| Del 2 | ... | ... | ... | ... | ... | ... |
| **Σ** | ΣA | — | ΣAy | — | — | **J** |

**Korak 1:** Nariši prerez, razdeli na enostavne like

**Korak 2:** Izračunaj $y_T$:
$$y_T = \frac{\sum A_i y_i}{\sum A_i}$$

**Korak 3:** Steiner za vsak del ($d_i = y_i - y_T$):
$$J = \sum\left(\frac{b_i h_i^3}{12} + A_i d_i^2\right)$$

**Korak 4:** Odpornostna momenta:
$$W_{sp} = \frac{J}{e_{sp}} = \frac{J}{y_T}, \qquad W_{zg} = \frac{J}{e_{zg}} = \frac{J}{H - y_T}$$

> ⚠️ **Kritičen je MANJŠI W** — to je najpogostejša napaka!

---

## Standardni prerezi — Tabela

| Prerez | $A$ | $I_x$ | $W_x$ | $I_p$ | $W_t$ |
|--------|-----|-------|-------|-------|-------|
| Pravokotnik $b \times h$ | $bh$ | $bh^3/12$ | $bh^2/6$ | — | — |
| Krog $d$ | $\pi d^2/4$ | $\pi d^4/64$ | $\pi d^3/32$ | $\pi d^4/32$ | $\pi d^3/16$ |
| Votli krog $d_z, d_n$ | $\pi(d_z^2-d_n^2)/4$ | $\pi(d_z^4-d_n^4)/64$ | $\pi(d_z^4-d_n^4)/(32d_z)$ | $\pi(d_z^4-d_n^4)/32$ | — |
| Trikotnik $b \times h$ | $bh/2$ | $bh^3/36$ | — | — | — |

---

## Statični moment $S$ (za strižne napetosti)

$$S_x = A' \cdot y_{T'} \quad \text{[cm³]}$$

kjer $A'$ = ploščina prereza nad (ali pod) točko, kjer računamo $\tau$, in $y_{T'}$ = razdalja težišča tega dela od skupnega težišča.

**Za pravokotnik** (maksimum v nevtralni osi):
$$S_{max} = \frac{b \cdot (h/2)^2}{2} = \frac{bh^2}{8} \quad \Rightarrow \quad \tau_{max} = \frac{T \cdot S_{max}}{I \cdot b} = 1{,}5 \cdot \frac{T}{A}$$

---

## T-prerez — Primer

```
       bp
  ┌──────────┐  ← pasnica, debelina hp
  |          |
  |  stojina |  ← debelina bs, višina hs
  └──┘    └──┘
```

| Del | $A_i$ | $y_i$ (od spodaj) | $A_i y_i$ | $I_{0,i}$ | $A_i d_i^2$ |
|-----|-------|--------------------|-----------|-----------|-------------|
| Stojina $b_s \times h_s$ | $b_s h_s$ | $h_s/2$ | ... | $b_s h_s^3/12$ | $A_s(y_s - y_T)^2$ |
| Pasnica $b_p \times h_p$ | $b_p h_p$ | $h_s + h_p/2$ | ... | $b_p h_p^3/12$ | $A_p(y_p - y_T)^2$ |

→ $y_T = \sum A_i y_i / \sum A_i$, $e_{sp} = y_T$, $e_{zg} = H - y_T$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Oblika prereza | Posebnost |
|-----|----------------|-----------|
| Simetričen (kvadrat, krog) | $e_{sp} = e_{zg}$ | Samo en $W$ |
| Asimetričen (T, L, U) | $e_{sp} \neq e_{zg}$ | **OBA** $W$, kritičen je manjši |
| Sestavljen (lepljen, vijačen) | Ločeni deli | Steiner je nujen |
| Za uklon | Treba $I_{min}$ in $i$ | Preveri **OBE** osi! |
| Za torzijo (krog) | Treba $I_p$, $W_t$ | $W_t = 2W$, $I_p = 2I$ |

---

## Kombinacije z drugimi bloki

### Blok 1.5 + 2 (Geometrija → Upogib)
Osnovna veriga: $J$ → $W$ → $\sigma = M/W$

### Blok 1.5 + 4 (Geometrija → Uklon)
$I_{min}$ → $i_{min}$ → $\lambda = lu/i$ → Euler

### Blok 1.5 + 5 (Geometrija → Torzija)
$I_p$, $W_t$ → $\tau = Mt/Wt$

---

## Pogosta napaka

- Pozabiti Steinerjevo korekcijo $A \cdot d^2$
- Pri asimetričnem prerezu vzeti samo en $W$ — **kritičen je manjši!**
- Za uklon vzeti $I_{max}$ namesto $I_{min}$
- Enote: $I$ [cm⁴], $W$ [cm³], $i$ [cm]

---

## Povezave

- [[Koncept - Vztrajnostni moment]] ← podrobna razlaga
- [[Blok 1 - NTM Diagrami]] ← predhodni blok
- [[Blok 2 - Upogib]] ← uporaba I in W
- [[Blok 4 - Euler Uklon]] ← I_min, i
- [[Blok 5 - Torzija]] ← Ip, Wt
- [[Vaje - Trdnost in dimenzioniranje]] ← Naloga 3 (T-prerez Steiner)
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

---
tags: [mehanika, torzija, vrtilni-moment, zasuk, Bredt, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 5 — Torzija

## VSE ENAČBE

```
NAVOR (torzijski moment):
  Mt = F · a    (F = sila, a = ročica do osi zasuka)

KROŽNI PREREZ (polni):
  τ(r) = G · r · ϑ   (ϑ = specifični zasuk, τ linearno z r!)
  τmax  = Mt / Wt,    Wt = π·d³/16 = 2·W
  φ     = Mt·L / (G·Ip),    Ip = π·d⁴/32 = 2·I
  G     = E / (2(1+ν))    ← G_jeklo ≈ 8077 kN/cm²

VOTLI KROG (cevni prerez):
  Wt = π(do⁴-di⁴) / (16·do)
  Ip = π(do⁴-di⁴) / 32

BREDT (tankosten ZAPRT profil - BOX, CEV):
  τ = Mt / (2·Am·t)
  Am = ploščina znotraj SREDNJE linije stene (ne zunanja!)
  t  = minimalna debelina stene
  Za pravokotni box: Am = (a-t)·(b-t)

PRAVOKOTNI PREREZ (b×h, les):
  τmax = Mt / (C1·b²·h)    [C1 iz tabel glede na h/b]
  φ    = Mt·L / (C2·b³·h·G) [C2 iz tabel]

ODPRTI TANKOSTENSKI PREREZ (U, L, I — ŠIBKI!):
  Wt ≈ 1/3 · Σ(hi · ti³)   ← zelo majhen, izogibaj torziji!

DIMENZIONIRANJE:
  Wt_min = Mt_max / τdop   → iz tega d, a ali b

KOMBINIRANO M + Mt:
  σ = M / W   (upogib)
  τ = Mt / Wt (torzija)
  VM:     σekv = √(σ² + 3τ²)  ≤ σdop
  Tresca: σekv = √(σ² + 4τ²)  ≤ σdop

MOHROVA KROŽNICA za čisto torzijo:
  σx=0, σy=0, τxy=τ  →  σ1=+τ, σ2=-τ, φ0=45°

ZASUK:
  φ = Mt·L / (G·Ip)    [rad]   (1 rad = 57,3°)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "torzija", "vrtilni moment", "zasuk"
- "gredi", "os motorja", "prenos momenta"
- "Bredt", "tankosten prerez", "škatla"
- "strižna napetost iz torzije"
- Podano: $Mt$ = torzijski moment [kNm ali kNcm]

**Kaj je podano:**
- $Mt$ = torzijski moment [kNcm]
- Dimenzije prereza (premer $d$, stena $t$, škatla $a \times b$)
- Dolžina $L$, modul $G$
- Morda tudi $M$ (upogib) za kombinirano nalogo

**Kaj se sprašuje:**
- $\tau_{max}$ = maksimalna strižna napetost
- $\phi$ = zasuk konca gredi
- Dimenzioniranje: minimalni $d$
- Kombinirano: $\sigma_{ekv}$ (VM ali Tresca)

---

## Kako začeti reševati

**Enostavna torzija (polni krog):**

**Korak 1:** Pretvori enote — $Mt$ v kNcm, $d$ v cm

**Korak 2:** Izračunaj $Wt$:
$$Wt = \frac{\pi d^3}{16} = 2 \cdot W$$

**Korak 3:** Preveri napetost:
$$\tau = \frac{Mt}{Wt} \leq \tau_{dop}$$

**Korak 4 (če zasuk):** $G = E/[2(1+\nu)]$, nato:
$$\phi = \frac{Mt \cdot L}{G \cdot Ip}$$

---

**Bredt (zaprt tankosten profil):**

**Korak 1:** Izračunaj $Am$ — ploščino **znotraj srednje linije** (ne zunanje!):
$$Am = (a - t) \cdot (b - t) \quad \text{(za pravokotnino)}$$

**Korak 2:** Bredt:
$$\tau = \frac{Mt}{2 \cdot Am \cdot t}$$

> ⚠️ $Am$ je ploščina srednje linije — ne zunanja ploščina!

---

**Kombinirano M + Mt:**

**Korak 1:** $\sigma = M/W$ iz upogiba

**Korak 2:** $\tau = Mt/Wt$ iz torzije

**Korak 3:** Vstavi v VM ali Tresca (odvisno od naloge)

**Korak 4:** Preveri $\sigma_{ekv} \leq \sigma_{dop}$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Formula |
|-----|----------------|---------|
| Čista torzija, polni krog | dan $d$, dan $Mt$ | $\tau = Mt/Wt$, $Wt = \pi d^3/16$ |
| Čista torzija, votlo | dan $d_o$, $d_i$ | $Wt = \pi(d_o^4-d_i^4)/(16d_o)$ |
| Bredt / škatla (zaprt) | "tankosten", "box", stena $t$ | $\tau = Mt/(2A_m t)$ |
| Pravokotni prerez (les) | "b×h", "pravokoten" | $\tau = Mt/(C_1 b^2 h)$ — C iz tabel |
| Odprti profil (U, L) | "U-profil", "odprt prerez" | $Wt \approx \frac{1}{3}\sum h_i t_i^3$ — majhen! |
| Kombinirano M+Mt | podano oboje M in Mt | VM ali Tresca |
| Dimenzioniranje | iščemo $d$ ali $a$ | Iz $\tau_{dop}$ → $Wt_{min}$ → dimenzija |

---

## Kombinacije z drugimi bloki

### Blok 5 + 3.5 (Torzija + VM/Tresca) ← **NAJPOGOSTEJŠE**
Naloga: Gredi pod upogibom in torzijo → preveri trdnost.
1. $\sigma = M/W$ (upogib)
2. $\tau = Mt/Wt$ (torzija), kjer $Wt = 2W$ za polni krog
3. VM: $\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$
4. Tresca: $\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$

### Blok 1.5 + 5 (Geometrija → Torzija)
Naloga: Izračunaj $I_p$ za sestavljeni prerez → zasuk.

### Blok 5 + 1 (NTM + Torzija)
Naloga: Gredi obremenjena z več silami → najprej NTM diagrami, nato v kritičnem prerezu torzijska kontrola.

---

## Materialni podatki

| Material | $G$ [kN/cm²] | $\tau_{dop}$ [kN/cm²] |
|----------|-------------|----------------------|
| Jeklo S235 | ≈ 8 077 | $\sigma_{dop}/\sqrt{3} \approx 9{,}2$ |
| Aluminij | ≈ 2 700 | — |

> $G = E / [2(1+\nu)]$, za jeklo: $G = 21000/[2 \cdot 1.3] \approx 8077$ kN/cm²

---

## Pogosta napaka

- $Wt = W$ namesto $Wt = 2W$ za polni krog
- Bredt: vzeti zunanjo ploščino namesto $Am$ (srednja linija!)
- Enote: $Mt$ mora biti v kNcm, $Wt$ v cm³ → $\tau$ v kN/cm²
- Kombinirano: pozabiti, da $M$ povzroča $\sigma$, ne $\tau$

---

## Povezave

- [[Koncept - Torzija]] ← podrobna izpeljava
- [[Blok 3.5 - Hipoteze Porusitve]] ← kombinirano napetostno stanje
- [[Blok 1.5 - Geometrijske Karakteristike]] ← $I_p$, $W_t$
- [[Vaje - Trdnost in dimenzioniranje]] ← N5 (d=50mm, M+Mt)
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

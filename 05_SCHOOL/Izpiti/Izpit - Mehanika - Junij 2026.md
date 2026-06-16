---
tags: [mehanika, izpit, statika, napetosti, trdnost, uklon]
predmet: Mehanika (LE007)
datum: 2026-06-14
---

# Izpit - Mehanika - Junij 2026

## Namen

Celovita priprava na izpit iz Mehanike (LE007, BTF Lesarstvo UN). Analiza temelji na 10+ zbranih izpitih in kolokvijih (2013–2025), predavanjih, DN1 in zvezku.

---

## Struktura izpita

**90 minut · 4 enakovredne naloge · vsaka ~25 točk**

| Naloga | Snov | Verjetnost |
|--------|------|------------|
| 1. | N, T, M diagrami | **100%** |
| 2. | Napetostni tenzor + Mohrova krožnica | ~85% |
| 3. | Trdnost / dimenzioniranje (upogib, torzija, uklon) | ~85% |
| 4. | Statika posebnih teles ali kinematika | ~70% |

---

## NALOGA 1 — N, T, M diagrami

**Vedno na izpitu.** Tipično: portalni okvir ali linijska konstrukcija z $q$ + $F$ + morda $M_0$.

### Postopek

1. $\sum F_x = 0,\quad \sum F_y = 0,\quad \sum M_A = 0$ → reakcije
2. Metoda preseka — od leve ali od prostega konca
3. Nariši diagrame s predznaki

### Grafična pravila

| Obremenitev | $T$ (prečna sila) | $M$ (upogibni moment) |
|-------------|-------------------|-----------------------|
| Enakomerna $q$ | linearna | parabolična |
| Točkovna $F$ | skok | lom |
| Točkasti moment $M_0$ | brez spremembe | preskok |

> $M_{max}$ je **tam kjer $T = 0$**

> **glej:** [[STATIKA#Metoda preseka]]

---

## NALOGA 2 — Napetostni tenzor + Mohrova krožnica

### 2D primer (enostavnejši)

$$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

Mohrova krožnica: središče $C = \frac{\sigma_x+\sigma_y}{2}$, radij $R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}$

### 3D primer (jul. 2018, feb. 2019)

Podan tenzor npr.:
$$\sigma_{ij} = \begin{pmatrix} -100 & -300 & 0 \\ -300 & 200 & 0 \\ 0 & 0 & 0 \end{pmatrix} \text{ MPa}$$

→ $\sigma_3 = 0$ (ravninsko stanje) → rešuješ kvadratno enačbo za $\sigma_1, \sigma_2$

### Ekvivalentne napetosti

**Tresca** (bolj konzervativna, bolj "varna"):
$$\sigma_{ekv} = \max\left(|\sigma_1-\sigma_2|,\, |\sigma_2-\sigma_3|,\, |\sigma_3-\sigma_1|\right)$$

ali alternativno: $\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$

**von Mises** (manj konzervativna):
$$\sigma_{ekv} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\right]}$$

ali alternativno: $\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$

> ⚠️ **Tresca daje višjo vrednost** → bolj konzervativna → varnejša hipoteza

> **glej:** [[STATIKA#Napetostni tenzor]]

---

## NALOGA 3 — Trdnost in dimenzioniranje

### Materialni podatki

| Material | $E\ [\text{kN/cm}^2]$ | $\sigma_{dop}\ [\text{kN/cm}^2]$ |
|----------|----------------------|----------------------------------|
| Les (iglavci) | **1000** | **1,0 – 1,2** |
| Jeklo S235 | **21 000** | **16** |

---

### TIP A — Dimenzioniranje pravokotnega prereza

**Mmax za prostoležeč + q po vsej dolžini + F na sredini:**

$$M_{max} = \frac{qL^2}{8} + \frac{FL}{4}$$

**Dimenzioniranje za $h = 2b$:**

$$W_{min} = \frac{M_{max}}{\sigma_{dop}}, \quad W = \frac{2b^3}{3} \quad \Rightarrow \quad b = \sqrt[3]{\frac{3\,W_{min}}{2}}, \quad h = 2b$$

**Krog:** $W = \frac{\pi d^3}{32}$ → $d = \sqrt[3]{\frac{32\,M}{\pi\,\sigma_{dop}}}$

> ⚠️ Pretvori $M$ iz kNm v kNcm (× 100)!

> **Kontrola:** $\sigma = M/W_{dej} \leq \sigma_{dop}$ ✓

---

### TIP B — Euler uklon

$$\boxed{F_k = \frac{\pi^2 E\, I_{min}}{l_u^2}} \qquad l_u = \beta \cdot L$$

| Vpetje | $\beta$ | Opomba |
|--------|---------|--------|
| Prostoležeč – prostoležeč | 1 | standardno |
| Vpet – prostoležeč | 0,7 | |
| Vpet – vpet | 0,5 | najvarnejše |
| Vpet – **prost** (konzola!) | **2** | ⚠️ **najnevarnejše** |

**Dimenzioniranje:** $F_k = \nu \cdot F_{dej}$ → $I_{min} = F_k l_u^2 / (\pi^2 E)$

Kvadraten prerez: $I = a^4/12$ → $a = \sqrt[4]{12\,I_{min}}$

**Kontrola Eulerjevega območja (OBVEZNO):**

$$i = \sqrt{\frac{I_{min}}{A}}, \quad \lambda = \frac{l_u}{i}, \quad \lambda_e = \pi\sqrt{\frac{E}{\sigma_{dop}}}$$

$$\lambda_e^{les} = \pi\sqrt{\frac{1000}{1{,}2}} = 90{,}7 \qquad \lambda_e^{jeklo} = \pi\sqrt{\frac{21000}{16}} = 114$$

- $\lambda > \lambda_e$ → Euler ✓
- $\lambda < \lambda_e$ → **ω metoda** (tabele!)

**Šibka os:** Za $b \times h$ vedno vzami **manjšo** dimenzijo:
$I_{min} = h_{\text{večji}} \cdot b_{\text{manjši}}^3 / 12$

> **Varnostni faktor:** $\nu_{dej} = F_k / F_{dej} \geq \nu_{zaht}$

---

### TIP C — Asimetričen prerez (T, I, L) — Steiner

**Postopek:**

$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}, \quad d_i = y_i - y_T$$

$$J = \sum\!\left(\frac{b_i h_i^3}{12} + A_i \cdot d_i^2\right)$$

$$W_{sp} = \frac{J}{e_{sp}}, \quad W_{zg} = \frac{J}{e_{zg}} \quad \leftarrow \textbf{preveri OBA!}$$

$$\sigma_{sp} = \frac{M}{W_{sp}}, \quad \sigma_{zg} = \frac{M}{W_{zg}} \quad \leq \sigma_{dop}$$

> ⚠️ Kritičen je **manjši W** (večja razdalja od težišča)!

---

### TIP D — Ekscentrični N + M

$$\sigma_{max} = \frac{N}{A} - \frac{M}{W} \quad \text{(stran sile)}, \qquad \sigma_{min} = \frac{N}{A} + \frac{M}{W} \quad \text{(nasprotna)}$$

$$M = F \cdot e, \quad N = -F \text{ (tlak)}$$

> ⚠️ **Ključna past:** Kljub tlačni sili se na nasprotni strani pojavi **NATEG**, ko $|M/W| > |N/A|$!

---

### TIP E — Sestavljena M + Mt (gred)

$$W = \frac{\pi d^3}{32}, \quad W_t = 2W \quad \text{(velja za polni krog!)}$$

$$\sigma = \frac{M}{W}, \quad \tau = \frac{M_t}{W_t}$$

| Hipoteza | Formula | Faktor |
|----------|---------|--------|
| **Von Mises** | $\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$ | 3 |
| **Tresca** | $\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$ | 4 |

> 💡 **"Tresca 4, VM 3"** — Tresca je vedno bolj konzervativna!

---

### HITRA REFERENCA — vse na enem mestu

```
UPOGIB dim:   b = ∛(3M/2σdop)  [za h=2b]  →  h=2b
              d = ∛(32M/πσdop) [za krog]

STEINER:      yT = ΣAi·yi / ΣA
              J = Σ(bh³/12 + A·d²)
              W_sp = J/e_sp,  W_zg = J/e_zg  ← OBA!

EULER:        lu = β·L  (β=1/0.7/0.5/2)
              i = √(Imin/A),  λ = lu/i
              λe(les)=90.7,  λe(jeklo)=114
              λ>λe → Fk=π²EImin/lu²
              λ<λe → ω metoda (tabele)
              ŠIBKA OS: vzami manjši b za Imin!

EKS. N+M:    σmax = N/A - M/W  (tlak+upogib)
              σmin = N/A + M/W  ⚠ mogoč NATEG!

M+Mt(krog):  W=πd³/32, Wt=2W
              VM:  σekv = √(σ²+3τ²)
              T:   σekv = √(σ²+4τ²)  ← strožje

MAT LES:     E=1000 kN/cm², σdop=1.0–1.2 kN/cm²
MAT JEKLO:   E=21000 kN/cm², σdop=16 kN/cm²
```

> **Rešene naloge vseh tipov:** [[Vaje - Trdnost in dimenzioniranje]]

---

## NALOGA 4 — Statika posebnih teles

Na BTF izpitih se pojavljata:

- **Škripec/dvigalo** → ravnovesje sil v vozliščih (sile v A in B)
- **Valji v kupu** → normalne sile med valji (geometrija + ravnovesje)
- **Reakcije pri nagnjeni konstrukciji** → vključi komponente $F\cos\alpha$ in $F\sin\alpha$

---

## Vzporedno osni izrek (za sestavljene prereze)

$$I = I_0 + A \cdot d^2$$

kjer je $d$ razdalja med težiščnico elementa in skupno osjo prereza.

---

## A4 list — ključne formule

```
REAKCIJE:   ΣFx=0,  ΣFy=0,  ΣMA=0
NTM:        skok T = F,  skok M = M₀,  Mmax kjer T=0
UPOGIB:     σ = M/W,   W = bh²/6   (h=2b → W = 2b³/3)
UKLON:      Fkr = π²EI/lu²   +   skica vpetij!
MOHR 2D:    σ₁₂ = (σx+σy)/2 ± √[((σx-σy)/2)² + τxy²]
TRESCA:     σekv = max(|σ₁-σ₂|, |σ₂-σ₃|, |σ₃-σ₁|)
VON MISES:  σekv = √[½((σ₁-σ₂)²+(σ₂-σ₃)²+(σ₃-σ₁)²)]
LES:        E = 1000 kN/cm²
VZP. OSI:   I = I₀ + A·d²
```

---

## Viri za zadnjo pripravo

- `MohrKrog-DN2-2526.pdf` — vaje specifično za letošnji rok ⭐
- `defNapVaje.pdf` — vaje iz deformacij in napetosti
- `upogibVaje.pdf` — vaje iz upogiba
- `NotrSileVaje.pdf` — N, T, M primeri
- [[Koncept - Krožni žagalni stroj]] — kombinirana obremenitev

---

## Povezave

- [[STATIKA]]
- [[Mehanika Hub]]
- [[Koncept - Krožni žagalni stroj]]
- [[05_SCHOOL/School Hub]]

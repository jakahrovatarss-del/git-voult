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

### A) Dimenzioniranje lesenega prereza na upogib

$$\sigma_{max} = \frac{M_{max}}{W} \leq \sigma_{dop}$$

Za pravokotni prerez $h:b = 2:1 \implies h = 2b$:

$$W = \frac{b \cdot h^2}{6} = \frac{b \cdot (2b)^2}{6} = \frac{2b^3}{3}$$

→ Iz pogoja $\sigma_{dop}$ iščeš $b$, nato $h = 2b$.

### B) Uklon lesenega stebra (Euler)

$$F_{krit} = \frac{\pi^2 E I}{l_u^2}, \qquad \nu = \frac{F_{krit}}{F_{dej}}$$

Uklonska dolžina $l_u$:

| Vpetje | $l_u$ |
|--------|-------|
| Oba konca členkovita | $L$ |
| Spodaj vpeto, zgoraj prosto | $2L$ |
| Spodaj vpeto, zgoraj členkovito | $0{,}7L$ |
| Oba konca vpeta | $0{,}5L$ |

**Les:** $E = 1000\ \text{kN/cm}^2$

### C) Kombinirana obremenitev (torzija + upogib)

Kot [[Koncept - Krožni žagalni stroj]] / DN1:
- Izračunaj $N, T, M_b, M_t$ po prerezu
- Ekvivalentna napetost po Tresciju ali von Misesu
- Primerjaj z $\sigma_{dop}$

> **glej:** [[Koncept - Krožni žagalni stroj]]

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

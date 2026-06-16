---
tags: [mehanika, hipoteze-porušitve, tresca, von-mises, trdnost, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 3.5 — Hipoteze Porušitve (Tresca, Von Mises)

## VSE ENAČBE

```
TRESCA (hipoteza max strižnih napetosti):
  SPLOŠNO 3D:  σekv = max(|σ1-σ2|, |σ2-σ3|, |σ3-σ1|)
  POENOSTAVITEV (σ1 ≥ σ2 ≥ σ3):  σekv = σ1 - σ3
  2D (σ + τ):  σekv = √(σ² + 4τ²)  ≤ σdop

VON MISES / HMH (hipoteza distorzijske energije):
  SPLOŠNO 3D:  σekv = √{½·[(σ1-σ2)² + (σ2-σ3)² + (σ3-σ1)²]}
  POENOSTAVITEV 2D:  σekv = √(σ1² - σ1σ2 + σ2²)
  2D (σ + τ):  σekv = √(σ² + 3τ²)  ≤ σdop

TRIK: Tresca = 4τ², VM = 3τ²  (faktor pred τ²)
→ TRESCA vedno da VIŠJI σekv = bolj konzervativna!

MOHR (za σ1, σ2 iz tenzorja):
  σsr = (σx+σy)/2
  R   = √[((σx-σy)/2)² + τxy²]
  σ1  = σsr + R,  σ2 = σsr - R,  σ3 = 0 (2D!)

POGOJ TRDNOSTI:
  σekv ≤ σdop

VARNOSTNI FAKTOR:
  ν = Fkrit / Fdejanski  ALI  ν = σdop / σekv  (≥ ν_zahtevani)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "preveri trdnost", "varnostni faktor", "ali je varno"
- "gredi", "os", "vijak" obremenjen z **M + Mt** ali **σ + τ**
- Podano: $\sigma$ in $\tau$ hkrati, ali $\sigma_1$ in $\sigma_2$
- "Von Mises", "Tresca", "HMH", "σekv"
- Prerez ima **kombinirano** obremenitev (upogib + torzija, nateg + strig)

**Kaj je podano:**
- $\sigma$ (normalna napetost iz upogiba ali natega)
- $\tau$ (strižna napetost iz torzije ali prečne sile)
- ali direktno $\sigma_x$, $\sigma_y$, $\tau_{xy}$ (napetostni tenzor)

**Kaj se sprašuje:**
- $\sigma_{ekv}$ in ali $\sigma_{ekv} \leq \sigma_{dop}$
- varnostni faktor $\nu$
- minimalna dimenzija prereza

---

## Kako začeti reševati

**Korak 1:** Ugotovi, katera hipoteza je zahtevana
- Tresca: konzervativnejša, varnejša (večji $\sigma_{ekv}$)
- Von Mises: bolj "realna", manjši $\sigma_{ekv}$

**Korak 2:** Pridobi napetosti v točki prereza

| Vir napetosti | Enačba |
|---------------|--------|
| Upogib | $\sigma = M/W$ |
| Nateg/tlak | $\sigma = N/A$ |
| Torzija | $\tau = Mt/Wt$ |
| Prečna sila | $\tau = T \cdot S / (I \cdot b)$ |

**Korak 3:** Vstavi v hipotezo

$$\text{Tresca 2D:} \quad \sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$$

$$\text{Von Mises 2D:} \quad \sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$$

**Korak 4:** Preveri $\sigma_{ekv} \leq \sigma_{dop}$ ali izračunaj $\nu$

> **Trik:** Tresca = koeficient **4** pred $\tau^2$, VM = koeficient **3** pred $\tau^2$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Podano | Formula |
|-----|--------|---------|
| Čista upogibna os | samo $\sigma$ | $\sigma_{ekv} = \sigma$ |
| Čista torzija | samo $\tau$ | VM: $\tau_{dop} = \sigma_{dop}/\sqrt{3}$ |
| M + Mt (gredi) | $\sigma$ iz M, $\tau$ iz Mt | $\sqrt{\sigma^2 + c\tau^2}$ |
| Tenzor dan | $\sigma_x$, $\sigma_y$, $\tau_{xy}$ | Najprej Mohr → $\sigma_1$, $\sigma_2$ |
| 3D problem | $\sigma_1$, $\sigma_2$, $\sigma_3$ | Tresca: $\sigma_1 - \sigma_3$ |

---

## Grafična razlaga: Tresca vs. Von Mises

V koordinatnem sistemu ($\sigma_1$, $\sigma_2$):
- **Tresca** tvori **šestkotnik** — dokler je $(\sigma_1, \sigma_2)$ znotraj, ste varni
- **VM** tvori **elipso**, ki gre skozi oglišča Trescinega šestkotnika

Tresca je vedno **znotraj** VM elipse → Tresca je bolj konzervativna.

```
         σ2
          |     [VM elipsa]
    ------+------  ← σdop
   /      |      \
  | [Tresca       |
  |  šestkotnik]  |
   \      |      /
    ------+------
          |          σ1
```

> **Pravilo:** Katera hipoteza da **višji** $\sigma_{ekv}$ = **bolj varna** (konzervativna).
> V večini primerov: Tresca > VM.

---

## Kombinacije z drugimi bloki

### Blok 2 + 3.5 (Upogib + VM/Tresca)
Naloga: prerez obremenjen z M in Mt.
1. Iz Blok 1 → $M_{max}$ in $Mt$
2. Iz Blok 1.5 → $W = \pi d^3/32$, $Wt = \pi d^3/16 = 2W$
3. $\sigma = M/W$, $\tau = Mt/Wt$
4. Vstavi v VM ali Tresca

### Blok 3 + 3.5 (Mohr + porušitev)
Naloga: dan napetostni tenzor, preveri trdnost.
1. Iz tenzorja → $\sigma_1$, $\sigma_2$ (Mohr)
2. Vstavi v $\sigma_{ekv}$

### Blok 2 + 3 + 3.5 (Ekscentrično N+M + Mohr + VM)
Naloga: steber z N in M → napetostni tenzor → hipoteza.

---

## Materialni podatki

| Material | $\sigma_{dop}$ | Opomba |
|----------|----------------|--------|
| Jeklo S235 | 16 kN/cm² | za statično obremenitev |
| Jeklo — nateg | 16 kN/cm² | |
| Jeklo — strig | $16/\sqrt{3} \approx 9{,}2$ kN/cm² | VM pogoj |

---

## Pogosta napaka

- Zamenjati faktor **4** (Tresca) in **3** (VM) — zapomni si: **"Tresca 4, VM 3"**
- Za gredi: $Wt = 2W$ (polni krog) — ne $Wt = W$!
- Pozabiti predznak σ pri tlaku (steber pod tlačno silo)

---

## Povezave

- [[Koncept - Hipoteze Porusitve]] ← podrobna izpeljava
- [[Blok 3 - Napetostno Stanje]] ← predhodni korak (σ1, σ2)
- [[Blok 2 - Upogib]] ← vir σ
- [[Blok 5 - Torzija]] ← vir τ
- [[Vaje - Trdnost in dimenzioniranje]] ← N5 (M+Mt), N6 (M+Mt z uklonskim koeficientom)
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

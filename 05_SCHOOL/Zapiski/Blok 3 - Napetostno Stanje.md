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

## Intuicija

### Fizikalna slika — "Majhna kocka v materialu"

Predstavljaj si, da si mikroskopski opazovalec znotraj materiala. Okrog tebe je majhna kocka. Na vsaki ploskvi delujeta dve vrsti napetosti:
- **Normalna napetost $\sigma$** — pritiska pravokotno na ploskev (nateg ali tlak)
- **Strižna napetost $\tau$** — drsi vzdolž ploskve

Zdaj zavrti kocko za kot $\phi$. Napetosti se spremenijo — **iste fizikalne sile, drug koordinatni sistem**. Mohrova krožnica je "kompas za te rotacije" — vsakemu zasuku ustreza točka na krožnici.

> *Vizualizacija:* Mohrova krožnica je mapa napetostnih stanj. Obhodíš cel krog → vidiš vse možne kombinacije $(\sigma, \tau)$ pri vsakem kotu zasuka.

---

### Miselni eksperiment — "Stisni gumijasto kocko pod 45°"

Stisni gumijasto kocko od leve in desne ($\sigma_x < 0$). Pod kotom 45° je napetost čisto strižna. Zakaj? Ker na tisti ravnini se dve tlačni napetosti "razporedita" — ena potisne, druga potegne — in skupaj ustvarita strig.

**Deformiraj do ekstrema:**
- Enoosni nateg → zasukaj za 45° → dobíš $\tau_{max} = \sigma/2$. To je Mohrova krožnica v akciji.
- Dvoosno enako tlačno → $R = 0$ → krožnica je točka → zasukaj za katerikoli kot → napetosti se ne spremenijo (hidrostatično).

---

### Zakaj enačba izgleda tako?

$$\sigma_1 = \frac{\sigma_x + \sigma_y}{2} + R, \qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

**Zakaj srednja vrednost in radij?** Ker transformacija napetosti pri zasuku je matematično rotacija v ravnini $(\sigma, \tau)$. Vsaka rotacija opiše krog. Središče = povprečje normalnih napetosti (to je invarianta pri rotaciji).

**Invarianta $\sigma_1 + \sigma_2 = \sigma_x + \sigma_y$:** Seštevek normalnih napetosti se pri rotaciji ne spremeni. Je hiter preverjevalni filter.

> *Enote:* $[\sigma_{1,2}] = \text{MPa}$ ✓

---

### Mejni primeri (sanity check)

| Stanje | $\sigma_1$ | $\sigma_2$ | $\tau_{max}$ | $\phi_0$ |
|---|---|---|---|---|
| Enoosno ($\sigma_y=0$, $\tau=0$) | $\sigma$ | $0$ | $\sigma/2$ | $45°$ |
| Čisto strižno ($\sigma=0$) | $+\tau$ | $-\tau$ | $\tau$ | $45°$ |
| Dvoosno enako | $\sigma$ | $\sigma$ | $0$ | — |
| Hidrostatično | $-p$ | $-p$ | $0$ | — |

> ⚠️ **Čisto strižno:** $\sigma_{1,2} = \pm\tau$ pod 45°. Zato se krhki materiali pri torziji lomijo spiralno — natezna napetost pod 45° jih potrga!

---

### Veriga vzrokov → Blok 3.5

Ko imaš $\sigma_1$, $\sigma_2$:
- → [[Blok 3.5 - Hipoteze Porusitve|Blok 3.5]]: Von Mises ali Tresca → $\sigma_{ekv}$ → trdnostni pogoj

> **Povzetek:** $(\sigma, \tau)$ iz Blok 2+5 → tenzor → Mohr → $\sigma_1, \sigma_2$ → porušitev.

> **glej:** [[Blok 3.5 - Hipoteze Porusitve#Intuicija]]

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

## Primer iz izpita — Deformacijski tenzor → napetostni tenzor (jeklo)

$$\varepsilon_{ij} = \begin{pmatrix} 1 & -3 & 0 \\ -3 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \cdot 10^{-4}, \quad E = 210\,000\ \text{MPa}, \quad \nu = 0{,}3$$

$$\lambda = 121\,154\ \text{MPa}, \quad G = 80\,769\ \text{MPa}, \quad \varepsilon_v = 3 \cdot 10^{-4}$$

$$\sigma_{ij} = \begin{pmatrix} 52{,}5 & -48{,}5 & 0 \\ -48{,}5 & 68{,}7 & 0 \\ 0 & 0 & 36{,}4 \end{pmatrix}\ \text{MPa}$$

$$\sigma_1 = 109{,}7\ \text{MPa}, \quad \sigma_2 = 36{,}4\ \text{MPa}, \quad \sigma_3 = 11{,}4\ \text{MPa}$$

Kontrola: $52{,}5 + 68{,}7 + 36{,}4 = 157{,}6 = 109{,}7 + 36{,}4 + 11{,}4 = 157{,}5$ ✓

> **Primer:** [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]

---

## Primer iz izpita — 3D Hookov zakon (aluminijast kvader)

Kvader $100 \times 150 \times 200$ mm, $F_x = 15$ kN (nateg), pogoj $\Delta H = -0{,}002$ mm, $E = 70\,000$ MPa, $\nu = 0{,}3$:

$$\sigma_x = 0{,}5\ \text{MPa}, \quad \varepsilon_z = \Delta H / H = -10^{-5}$$

$$\varepsilon_z = \frac{1}{E}[\sigma_z - \nu(\sigma_x + \sigma_y)] \Rightarrow \sigma_z = -0{,}55\ \text{MPa}$$

$$F_z = |\sigma_z| \cdot A_{xy} = 0{,}55 \cdot 15\,000 = \boxed{8\,250\ \text{N}}$$

> ⚠️ Brez Poissonovega efekta ($\nu$) bi dobili $F_z = 10{,}5$ kN — **napaka 21%**!

> **Primer:** [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]]

---

## Primer — Kamniti zid pod tlakom + strigom

$\sigma_x = -2{,}5$ MPa (tlak), $\sigma_y = 0$, $\tau_{xy} = 0{,}8$ MPa → $\sigma_1 = +0{,}234$ MPa (**nateg**!), $\sigma_2 = -2{,}734$ MPa

> ⚠️ Kljub prevladujočemu tlaku se pojavi **nateg** — nevarno za krhke materiale (beton, kamen)!

---

## Pogosta napaka

- Napačen predznak $\tau_{xy}$ pri odčitavanju tenzorja
- Pozabiti preveriti invarianto $\sigma_1 + \sigma_2 = \sigma_x + \sigma_y$
- $\phi_0$ je kot zasuka v **fizičnem prostoru** = polovica kota na Mohrovi krožnici
- Za 3D problem: $\sigma_3 = 0$ (ravninsko stanje) — ne pozabiti pri VM!
- ⚠️ Zamenjava kota normale in kota ravnine — razlika 90°! V formulah nastopa $\phi$ kot NORMALE!
- ⚠️ Tenzorska konvencija: $\tau_{xy} = 2G \cdot \varepsilon_{xy}$ (tenzorska), enako kot $G \cdot \gamma_{xy}$ (inženirska) — ker $\gamma = 2\varepsilon$!

---

## Povezave

- [[Koncept - Napetostno stanje]] ← podrobna razlaga + Mohr
- [[Blok 3.5 - Hipoteze Porusitve]] ← naslednji korak (Tresca, Von Mises)
- [[Blok 2 - Upogib]] ← od kje pridejo σ in τ
- [[Blok 5 - Torzija]] ← torzijsko strižno stanje
- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← rešene naloge
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]] ← εij→σij→σ1,2,3
- [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]] ← 3D Hooke, Poissonov efekt
- [[Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine]] ← σ(φ), τ(φ) formule
- [[Naloga - Mehanika - Izpit Jul2018 - Cisto strizno stanje]] ← čist strig, φ0=45°
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]] ← 3D tenzor, razvrstitev
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

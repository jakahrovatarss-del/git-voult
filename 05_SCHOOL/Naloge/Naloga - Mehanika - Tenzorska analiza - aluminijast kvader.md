---
tags: [mehanika, tenzor, deformacije, Hooke, 3D, kvader, naloga]
predmet: Mehanika
datum: 2026-06-14
vir: IMG_1241.pdf, str. 44 (naloga), str. 45-46 (rešitev)
---

# Naloga: Aluminijast kvader — 3D Hookov zakon (Sila iz dane deformacije)

## Podatki

- Dimenzije kvadra: $a = 100\ \text{mm}$ (x), $b = 150\ \text{mm}$ (y), $H = 200\ \text{mm}$ (z — višina)
- Natezna sila v smeri x: $F_x = 15\ \text{kN}$
- Tlačna sila v smeri z: $F_z = ?$ (iščemo)
- Pogoj: višina se zmanjša za $\Delta H = -0{,}002\ \text{mm}$
- $E = 70\ \text{GPa} = 70\,000\ \text{MPa}$, $\nu = 0{,}3$

> ℹ️ Aluminij: $E = 70$ GPa (3× manj kot jeklo: 210 GPa)

---

## Korak 1 — Normalne napetosti iz sil

### Zakaj?

Za Hookov zakon potrebujemo napetosti (ne sile). Napetost = sila / ploščina prereza.

### Izračun

**Napetost od $F_x$** (nateg v x smeri, prerez v y-z ravnini):

$$\sigma_x = \frac{F_x}{A_{yz}} = \frac{15\,000\ \text{N}}{150\ \text{mm} \cdot 200\ \text{mm}} = \frac{15\,000}{30\,000} = \boxed{0{,}5\ \text{N/mm}^2 = 0{,}5\ \text{MPa}}$$

**V y smeri ni obtežbe:** $\sigma_y = 0$

**V z smeri iščemo $\sigma_z$** (tlačna napetost, prerez v x-y ravnini):

$$\sigma_z = \frac{-F_z}{A_{xy}} = \frac{-F_z}{100 \cdot 150}\ \text{N/mm}^2 \qquad \text{(neznano, negativno ker tlak)}$$

> **glej:** [[Koncept - Napetostno stanje#3D Napetostno stanje — Hookov zakon in Laméjeve konstante]]

---

## Korak 2 — Pogoj deformacije v z smeri

### Zakaj?

Višina se zmanjša za $\Delta H = 0{,}002$ mm → to je robni pogoj, ki nam da enačbo za $\sigma_z$.

### Izračun $\varepsilon_z$

$$\varepsilon_z = \frac{\Delta H}{H} = \frac{-0{,}002\ \text{mm}}{200\ \text{mm}} = -10^{-5}$$

(negativen predznak ker skrajšanje — tlak v z smeri)

---

## Korak 3 — Hookov zakon za $\varepsilon_z$

### Zakaj?

Deformacija $\varepsilon_z$ ni odvisna samo od $\sigma_z$, ampak tudi od $\sigma_x$ in $\sigma_y$ prek Poissonovega efekta!

### Enačba

$$\varepsilon_z = \frac{1}{E}\left[\sigma_z - \nu(\sigma_x + \sigma_y)\right]$$

Vstavimo $\varepsilon_z = -10^{-5}$, $E = 70\,000$ MPa, $\nu = 0{,}3$, $\sigma_x = 0{,}5$ MPa, $\sigma_y = 0$:

$$-10^{-5} = \frac{1}{70\,000}\left[\sigma_z - 0{,}3(0{,}5 + 0)\right]$$

$$-10^{-5} \cdot 70\,000 = \sigma_z - 0{,}15$$

$$-0{,}70 = \sigma_z - 0{,}15$$

$$\boxed{\sigma_z = -0{,}70 + 0{,}15 = -0{,}55\ \text{MPa} \quad \text{(tlak)}}$$

> 🔍 **Fizikalni pomen Poissonovega efekta:** Ko nategnemo kvader v x smeri ($\sigma_x = +0{,}5$ MPa), se kvader v z smeri nekoliko **raztegne** (Poissonov efekt). Ker moramo zagotoviti skrajšanje, mora tlačna sila $F_z$ biti nekoliko manjša, kot bi bila brez $F_x$.

> ⚠️ Brez $\nu$ bi dobili $\sigma_z = -0{,}70$ MPa — napaka za $0{,}15$ MPa = 21%!

> **glej:** [[Koncept - Napetostno stanje#Inverz — deformacije iz napetosti]]

---

## Korak 4 — Sila $F_z$

$$|\sigma_z| = \frac{F_z}{A_{xy}} \quad \Rightarrow \quad F_z = |\sigma_z| \cdot A_{xy}$$

$$F_z = 0{,}55\ \text{MPa} \cdot (100 \cdot 150)\ \text{mm}^2 = 0{,}55 \cdot 15\,000\ \text{N}$$

$$\boxed{F_z = 8\,250\ \text{N} = 8{,}25\ \text{kN} \quad \text{(tlak)}}$$

---

## Korak 5 — Napetostni tenzor in deformacijski tenzor

### Napetostni tenzor

$$\sigma_{ij} = \begin{pmatrix} 0{,}5 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -0{,}55 \end{pmatrix}\ \text{MPa}$$

(Diagonalen — ni strižnih napetosti)

### Deformacijski tenzor (izračunamo vse komponente)

$$\varepsilon_x = \frac{1}{E}[\sigma_x - \nu(\sigma_y + \sigma_z)] = \frac{1}{70\,000}[0{,}5 - 0{,}3(0 + (-0{,}55))]$$
$$= \frac{0{,}5 + 0{,}165}{70\,000} = \frac{0{,}665}{70\,000} = \boxed{9{,}5 \cdot 10^{-6}}$$

$$\varepsilon_y = \frac{1}{E}[\sigma_y - \nu(\sigma_x + \sigma_z)] = \frac{1}{70\,000}[0 - 0{,}3(0{,}5 + (-0{,}55))]$$
$$= \frac{-0{,}3 \cdot (-0{,}05)}{70\,000} = \frac{0{,}015}{70\,000} = \boxed{2{,}14 \cdot 10^{-7}}$$

$$\varepsilon_z = -10^{-5} \quad \text{(dano)}$$

$$\varepsilon_{ij} = \begin{pmatrix} 9{,}5 \cdot 10^{-6} & 0 & 0 \\ 0 & 2{,}14 \cdot 10^{-7} & 0 \\ 0 & 0 & -10^{-5} \end{pmatrix}$$

### Spremembe dimenzij

$$\Delta a = \varepsilon_x \cdot a = 9{,}5 \cdot 10^{-6} \cdot 100 = 9{,}5 \cdot 10^{-4}\ \text{mm} \quad \text{(razteg v x)}$$

$$\Delta b = \varepsilon_y \cdot b = 2{,}14 \cdot 10^{-7} \cdot 150 = 3{,}2 \cdot 10^{-5}\ \text{mm} \quad \text{(razteg v y)}$$

$$\Delta H = \varepsilon_z \cdot H = -10^{-5} \cdot 200 = -0{,}002\ \text{mm} \quad ✓ \text{(skrajšanje v z)}$$

---

## Povzetek

| Korak | Vsebina | Enačba | Rezultat |
|-------|---------|--------|---------|
| 1 | Napetost iz sile | $\sigma = F/A$ | $\sigma_x = 0{,}5$ MPa |
| 2 | Pogoj deformacije | $\varepsilon_z = \Delta H / H$ | $-10^{-5}$ |
| 3 | Hooke za $\varepsilon_z$ | $\varepsilon_z = [\sigma_z - \nu(\sigma_x+\sigma_y)]/E$ | $\sigma_z = -0{,}55$ MPa |
| 4 | Sila iz napetosti | $F_z = |\sigma_z| \cdot A$ | $\boxed{F_z = 8{,}25\ \text{kN}}$ |
| 5 | Tenzorja | iz Hooke-a | $\sigma_{ij}$, $\varepsilon_{ij}$ diagonalna |

---

## Napaka brez Poissonovega efekta

Če bi zanemarili $\nu$ (napaka!):
$$\varepsilon_z = \sigma_z / E \quad \Rightarrow \quad \sigma_z = \varepsilon_z \cdot E = -10^{-5} \cdot 70\,000 = -0{,}70\ \text{MPa}$$
$$F_z = 0{,}70 \cdot 15\,000 = 10\,500\ \text{N} = 10{,}5\ \text{kN}$$

Razlika: $10{,}5 - 8{,}25 = 2{,}25$ kN = **21% napaka** — zato $\nu$ ni zanemarljiv!

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]
- [[Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

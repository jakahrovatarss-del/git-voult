---
tags: [mehanika, napetosti, Tresca, VonMises, izpit, naloga, tenzor]
predmet: Mehanika
datum: 2026-06-14
vir: Izpit iz Mehanike BTF, Lesarstvo UN, 5. 2. 2019 / 3. 9. 2025, Naloga 3
---

# Naloga: Tresca in Von Mises — Izpit Feb 2019

## Podatki

$$\sigma_{ij} = \begin{pmatrix} -100 & -300 & 0 \\ -300 & 200 & 0 \\ 0 & 0 & 0 \end{pmatrix}\ \text{MPa}$$

- Dopustna napetost: $\sigma_{dop} = 610\ \text{MPa}$

**Naloga:** Izračunaj ekvivalentne napetosti po Trescu in Von Misesu. Ali je napetostno stanje v točki A prekoračeno? Katera hipoteza je bolj konzervativna?

---

## Korak 1 — Glavne napetosti

### Zakaj?

Tresca in Von Mises delata s **glavnimi napetostmi** $\sigma_1 \geq \sigma_2 \geq \sigma_3$.

### Poenostavitev

Ker $\tau_{xz} = \tau_{yz} = 0$: direktno $\sigma_z = 0$ je ena lastna vrednost.

Za 2D podmatriko:

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2} = \frac{-100 + 200}{2} = 50\ \text{MPa}$$

$$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \sqrt{\left(\frac{-100-200}{2}\right)^2 + (-300)^2}$$

$$= \sqrt{(-150)^2 + (-300)^2} = \sqrt{22\,500 + 90\,000} = \sqrt{112\,500} = \boxed{335{,}4\ \text{MPa}}$$

$$\sigma_I = 50 + 335{,}4 = +385{,}4\ \text{MPa}$$
$$\sigma_{II} = 50 - 335{,}4 = -285{,}4\ \text{MPa}$$

### Pravilna razvrstitev $\sigma_1 \geq \sigma_2 \geq \sigma_3$:

$$\boxed{\sigma_1 = +385{,}4\ \text{MPa}}, \quad \boxed{\sigma_2 = 0\ \text{MPa}}, \quad \boxed{\sigma_3 = -285{,}4\ \text{MPa}}$$

> ⚠️ **Pozor:** $\sigma_z = 0$ je **vmesna** vrednost med +385.4 in -285.4, zato je $\sigma_2 = 0$, ne $\sigma_3$!

**Kontrola ($I_1$ invarianta):**
$$\sigma_x + \sigma_y + \sigma_z = -100 + 200 + 0 = 100\ \text{MPa}$$
$$\sigma_1 + \sigma_2 + \sigma_3 = 385{,}4 + 0 + (-285{,}4) = 100\ \text{MPa} \quad ✓$$

> **glej:** [[Koncept - Napetostno stanje#Lastne vrednosti tenzorja — 3D glavne napetosti]]

---

## Korak 2 — Tresca

### Zakaj?

Tresca: porušitev pri max strižni napetosti → $\sigma_{ekv} = \sigma_{max} - \sigma_{min} = \sigma_1 - \sigma_3$.

$$\sigma_{ekv,T} = \sigma_1 - \sigma_3 = 385{,}4 - (-285{,}4) = \boxed{670{,}8\ \text{MPa}}$$

$$670{,}8\ \text{MPa} > 610\ \text{MPa} \quad \Rightarrow \quad \boxed{\textbf{PREKORAČENO po Trescu!}}$$

> **glej:** [[Koncept - Napetostno stanje#Tresca (hipoteza maksimalne strižne napetosti)]]

---

## Korak 3 — Von Mises

### Zakaj?

Von Mises: porušitev pri distorzijski energiji → geometrijska sredina razlik glavnih napetosti.

$$\sigma_{ekv,VM} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2\right]}$$

Vstavimo:
$$= \sqrt{\frac{1}{2}\left[(385{,}4 - 0)^2 + (0 - (-285{,}4))^2 + (-285{,}4 - 385{,}4)^2\right]}$$

$$= \sqrt{\frac{1}{2}\left[148\,533 + 81\,453 + 449\,972\right]}$$

$$= \sqrt{\frac{679\,958}{2}} = \sqrt{339\,979} = \boxed{583{,}1\ \text{MPa}}$$

$$583{,}1\ \text{MPa} < 610\ \text{MPa} \quad \Rightarrow \quad \boxed{\textbf{Varno po Von Misesu ✓}}$$

> **glej:** [[Koncept - Napetostno stanje#Von Mises (hipoteza specifične energije oblike)]]

---

## Korak 4 — Primerjava in zaključek

| Hipoteza | $\sigma_{ekv}$ | $\sigma_{dop}$ | Ocena |
|----------|---------------|----------------|-------|
| **Tresca** | **670,8 MPa** | 610 MPa | ❌ PREKORAČENO |
| **Von Mises** | **583,1 MPa** | 610 MPa | ✓ varno |

**Bolj konzervativna hipoteza: Tresca**, ker:
- Da višjo vrednost $\sigma_{ekv}$ (670,8 > 583,1 MPa)
- Pogosteje zavrne napetostno stanje
- Bolj varna za projektiranje

**Bolj natančna (realistična): Von Mises** — bliže eksperimentalnim rezultatom za duktilne materiale (jeklo, aluminij).

> 🔍 **Razmerje:** $\sigma_{ekv,T} / \sigma_{ekv,VM} = 670{,}8 / 583{,}1 = 1{,}15$ → Tresca je 15% strožja.

---

## Povzetek

| Korak | Vsebina | Rezultat |
|-------|---------|---------|
| 1 | Glavne napetosti | σ₁=385.4, σ₂=0, σ₃=−285.4 MPa |
| 2 | Tresca | σ_ekv=670.8 MPa → ❌ prekoračeno |
| 3 | Von Mises | σ_ekv=583.1 MPa → ✓ varno |
| 4 | Primerjava | Tresca bolj konzervativna |

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

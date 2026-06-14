---
tags: [mehanika, napetosti, Tresca, VonMises, hipoteze-porušitve, plastičnost, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — Hipoteze porušitve (Tresca in Von Mises)

## Namen

Določiti, **kdaj material poruši** (ali prekorači mejo tečenja), ko je obremenjen z večosnim napetostnim stanjem. Pogosta tema na izpitu: dana σ₁,₂,₃ → izračunaj σ_ekv → primerjaj z σ_dop.

---

![[hipoteze_porusitve.svg]]

---

## Tresca (hipoteza maksimalne strižne napetosti)

**Predpostavka:** Porušitev nastopi, ko maksimalna strižna napetost doseže vrednost pri enoosnem nategu.

$$\tau_{max} = \frac{\sigma_{max} - \sigma_{min}}{2} = \frac{\sigma_{dop}}{2}$$

$$\boxed{\sigma_{ekv,Tresca} = \sigma_{max} - \sigma_{min} = \sigma_1 - \sigma_3}$$

kjer je $\sigma_1 \geq \sigma_2 \geq \sigma_3$ (razvrstitev!).

**Pogoj varnosti:**

$$\sigma_{ekv,Tresca} \leq \sigma_{dop}$$

> **Posebni primeri:**
> - 2D, σ₃=0: $\sigma_{ekv} = \sigma_1 - \sigma_2$ (če oba enaka predznaka → $\sigma_{ekv} = \sigma_1$)
> - Čisto strižno: $\sigma_1 = +\tau$, $\sigma_2 = 0$, $\sigma_3 = -\tau$ → $\sigma_{ekv} = 2\tau$

---

## Von Mises (hipoteza specifične energije oblike)

**Predpostavka:** Porušitev nastopi, ko energija oblike (distorzijska) doseže kritično vrednost.

$$\boxed{\sigma_{ekv,VM} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2\right]}}$$

**Poenostavitev za 2D** ($\sigma_3 = 0$):

$$\sigma_{ekv,VM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$$

**Poenostavitev za kombinirani upogib + torzija** ($\sigma_x = \sigma$, $\tau_{xy} = \tau$, ostalo 0):

$$\boxed{\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2}}$$

> **Fizikalni pomen:** Von Mises meri energijo, ki gre v spremembo oblike (ne volumna). Eksperimentalno bližje resnici kot Tresca.

---

## Primerjava

| | Tresca | Von Mises |
|--|--------|-----------|
| Osnova | max strižna napetost | energija oblike |
| Vrednost σ_ekv | večja ali enaka | manjša ali enaka |
| Konzervativnost | **bolj konzervativna** (varnejša) | manj konzervativna |
| Natančnost | slabša | **boljša** (bliže eksperimentu) |
| Geometrija v σ₁-σ₂ | šestkotnik | elipsa (zunaj šestkotnika) |

> ⚠️ Tresca je vedno: $\sigma_{ekv,Tresca} \geq \sigma_{ekv,VM}$

**Katera je bolj konzervativna?** → Tresca, ker da višji σ_ekv → pogosteje zavrne.

---

## Algoritem (izpit)

```
1. Iz σij tenzorja izračunaj σ1 ≥ σ2 ≥ σ3 (lastne vrednosti)
2. Tresca: σ_ekv = σ1 − σ3
3. Von Mises: σ_ekv = √[½((σ1−σ2)²+(σ2−σ3)²+(σ3−σ1)²)]
4. Preveri: σ_ekv ≤ σ_dop?
5. Primerjaj obe vrednosti: Tresca > Von Mises → Tresca je strožja
```

---

## Rešen primer — Izpit Feb 2019 / Sep 2025

### Podatki

$$\sigma_{ij} = \begin{pmatrix} -100 & -300 & 0 \\ -300 & 200 & 0 \\ 0 & 0 & 0 \end{pmatrix}\ \text{MPa}, \qquad \sigma_{dop} = 610\ \text{MPa}$$

### Korak 1 — Glavne napetosti

$\sigma_3 = 0$ (ker $\tau_{xz} = \tau_{yz} = 0$)

Za 2D podmatriko:

$$\sigma_{sr} = \frac{-100 + 200}{2} = 50\ \text{MPa}$$

$$R = \sqrt{\left(\frac{-100-200}{2}\right)^2 + (-300)^2} = \sqrt{150^2 + 300^2} = \sqrt{22500 + 90000} = \sqrt{112500} = 335{,}4\ \text{MPa}$$

$$\sigma_1 = 50 + 335{,}4 = \boxed{+385{,}4\ \text{MPa}}$$

$$\sigma_2 = 50 - 335{,}4 = \boxed{-285{,}4\ \text{MPa}}$$

$$\sigma_3 = 0\ \text{MPa}$$

Razvrstitev: $\sigma_1 = +385{,}4 \geq \sigma_3 = 0 \geq \sigma_2 = -285{,}4$ MPa

### Korak 2 — Tresca

$$\sigma_{ekv,T} = \sigma_1 - \sigma_2 = 385{,}4 - (-285{,}4) = \boxed{670{,}8\ \text{MPa}}$$

$$670{,}8\ \text{MPa} > 610\ \text{MPa} \quad \Rightarrow \quad \textbf{PREKORAČENO!}$$

> **Zakaj σ_max − σ_min, ne σ1 − σ3?** Ker $\sigma_2 = -285{,}4$ MPa < $\sigma_3 = 0$ → pravilna razvrstitev je $\sigma_1 \geq \sigma_3 \geq \sigma_2$, torej $\sigma_{ekv} = \sigma_1 - \sigma_2$!

### Korak 3 — Von Mises

$$\sigma_{ekv,VM} = \sqrt{\frac{1}{2}\left[(385{,}4+285{,}4)^2 + (-285{,}4-0)^2 + (0-385{,}4)^2\right]}$$

$$= \sqrt{\frac{1}{2}\left[670{,}8^2 + 285{,}4^2 + 385{,}4^2\right]}$$

$$= \sqrt{\frac{1}{2}\left[449\,972 + 81\,453 + 148\,533\right]}$$

$$= \sqrt{\frac{679\,958}{2}} = \sqrt{339\,979} = \boxed{583{,}1\ \text{MPa}}$$

$$583{,}1\ \text{MPa} < 610\ \text{MPa} \quad \Rightarrow \quad \textbf{NI prekoračeno ✓}$$

### Zaključek

| Hipoteza | σ_ekv | σ_dop | Ocena |
|----------|-------|-------|-------|
| Tresca | 670,8 MPa | 610 MPa | ❌ PREKORAČENO |
| Von Mises | 583,1 MPa | 610 MPa | ✓ varno |

**Tresca je bolj konzervativna** — zavrne stanje, ki ga Von Mises sprejme. Za varno projektiranje izberemo Tresco.

> **Katera je bolj "varna"?** → Tresca, ker da višji σ_ekv in pogosteje zavrne. Von Mises je bliže eksperimentalnim rezultatom (manj konzervativna ≠ manj natančna).

> **glej:** [[Koncept - Napetostno stanje#Lastne vrednosti tenzorja — 3D glavne napetosti]]

---

## Kontrolni invariant

$$I_1 = \sigma_x + \sigma_y + \sigma_z = -100 + 200 + 0 = 100\ \text{MPa}$$
$$\sigma_1 + \sigma_2 + \sigma_3 = 385{,}4 + (-285{,}4) + 0 = 100\ \text{MPa} \quad ✓$$

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]]
- [[Koncept - Torzija]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

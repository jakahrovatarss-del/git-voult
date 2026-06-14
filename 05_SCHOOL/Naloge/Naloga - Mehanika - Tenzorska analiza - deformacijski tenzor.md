---
tags: [mehanika, tenzor, deformacije, napetosti, Lame, Hooke, naloga]
predmet: Mehanika
datum: 2026-06-14
vir: IMG_1241.pdf, str. 3 (naloga), str. 5 (rešitev)
---

# Naloga: Deformacijski tenzor → Napetostni tenzor → Glavne napetosti

## Podatki

$$\varepsilon_{ij} = \begin{pmatrix} 1 & -3 & 0 \\ -3 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} \cdot 10^{-4}$$

- $E = 2{,}1 \cdot 10^5\ \text{N/mm}^2 = 210\,000\ \text{MPa}$
- $\nu = 0{,}3$

**Naloga:** Izračunaj napetostni tenzor $\sigma_{ij}$ in določi **glavne normalne napetosti** $\sigma_1, \sigma_2, \sigma_3$.

---

![[napetostni_element_3d.svg]]

## Korak 1 — Laméjevi konstanti

### Zakaj?

Hookov zakon v tenzorski obliki $\sigma_{ij} = \lambda \varepsilon_v \delta_{ij} + 2G\varepsilon_{ij}$ zahteva konstanti $\lambda$ in $G$.

### Izpeljava

$$\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)} = \frac{210\,000 \cdot 0{,}3}{(1+0{,}3)(1-2\cdot0{,}3)}$$

$$= \frac{63\,000}{1{,}3 \cdot 0{,}4} = \frac{63\,000}{0{,}52} = \boxed{121\,154\ \text{MPa}}$$

$$G = \frac{E}{2(1+\nu)} = \frac{210\,000}{2 \cdot 1{,}3} = \frac{210\,000}{2{,}6} = \boxed{80\,769\ \text{MPa}}$$

> 🔍 **Fizikalni pomen:** $\lambda$ poveže volumsko dilatacijo z normalnimi napetostmi. $G$ je strižni modul — upor materiala na strižne deformacije.

> **glej:** [[Koncept - Napetostno stanje#3D Napetostno stanje — Hookov zakon in Laméjeve konstante]]

---

## Korak 2 — Volumska dilatacija $\varepsilon_v$

### Zakaj?

Člen $\lambda \varepsilon_v$ v Hookovem zakonu deluje na vse normalne napetosti enako — opisuje hidrostatični del napetostnega stanja.

### Izračun

$$\varepsilon_v = \varepsilon_x + \varepsilon_y + \varepsilon_z = (1 + 2 + 0) \cdot 10^{-4} = \boxed{3 \cdot 10^{-4}}$$

> ℹ️ $\varepsilon_v$ = sled deformacijskega tenzorja = vsota diagonalnih komponent.

> **glej:** [[Koncept - Napetostno stanje#Volumska dilatacija]]

---

## Korak 3 — Napetostni tenzor $\sigma_{ij}$

### Zakaj?

Iz Hookovega zakona $\sigma_{ij} = \lambda\varepsilon_v\delta_{ij} + 2G\varepsilon_{ij}$ izračunamo vsako komponento posebej.

### Izračun normalnih napetosti

$$\lambda\varepsilon_v = 121\,154 \cdot 3 \cdot 10^{-4} = 36{,}35\ \text{MPa}$$

$$\sigma_x = \lambda\varepsilon_v + 2G\varepsilon_x = 36{,}35 + 2 \cdot 80\,769 \cdot 1 \cdot 10^{-4}$$
$$= 36{,}35 + 16{,}15 = \boxed{52{,}49\ \text{MPa}}$$

$$\sigma_y = \lambda\varepsilon_v + 2G\varepsilon_y = 36{,}35 + 2 \cdot 80\,769 \cdot 2 \cdot 10^{-4}$$
$$= 36{,}35 + 32{,}31 = \boxed{68{,}65\ \text{MPa}}$$

$$\sigma_z = \lambda\varepsilon_v + 2G\varepsilon_z = 36{,}35 + 2 \cdot 80\,769 \cdot 0 = \boxed{36{,}35\ \text{MPa}}$$

### Izračun strižnih napetosti

> ⚠️ **Ključno:** Tenzorska komponenta $\varepsilon_{xy}$ je **polovica** tehničnega strižnega kota $\gamma_{xy}$. Formula: $\tau_{xy} = 2G \cdot \varepsilon_{xy}$ (ne $G \cdot \gamma_{xy}$ — to je isto!).

$$\tau_{xy} = 2G\varepsilon_{xy} = 2 \cdot 80\,769 \cdot (-3 \cdot 10^{-4}) = \boxed{-48{,}46\ \text{MPa}}$$

$$\tau_{xz} = 2G\varepsilon_{xz} = 0, \qquad \tau_{yz} = 2G\varepsilon_{yz} = 0$$

### Napetostni tenzor

$$\boxed{\sigma_{ij} = \begin{pmatrix} 52{,}49 & -48{,}46 & 0 \\ -48{,}46 & 68{,}65 & 0 \\ 0 & 0 & 36{,}35 \end{pmatrix}\ \text{MPa}}$$

> **glej:** [[Koncept - Napetostno stanje#Hookov zakon v 3D (tenzorska oblika)]]

---

## Korak 4 — Glavne napetosti (lastne vrednosti)

### Zakaj?

Glavne napetosti so lastne vrednosti tenzorja $\sigma_{ij}$ — smeri, v katerih delujejo samo normalne napetosti, brez strižnih. Na teh smereh so ekstremi normalnih napetosti.

### Poenostavitev: $\tau_{xz} = \tau_{yz} = 0$

Ker sta izvendiagonalni komponenti v $z$-smeri nič, se tenzor razpade:

**Direktno:** $\sigma_z = 36{,}35$ MPa je že **ena glavna napetost**.

Za preostali dve rešimo iz 2D podmatrike:

$$\det\begin{pmatrix} \sigma_x - \sigma & \tau_{xy} \\ \tau_{xy} & \sigma_y - \sigma \end{pmatrix} = 0$$

$$(\sigma_x - \sigma)(\sigma_y - \sigma) - \tau_{xy}^2 = 0$$

### Razvoj determinante

$$\sigma^2 - (\sigma_x + \sigma_y)\sigma + (\sigma_x\sigma_y - \tau_{xy}^2) = 0$$

Vstavim vrednosti:
- $\sigma_x + \sigma_y = 52{,}49 + 68{,}65 = 121{,}14$
- $\sigma_x\sigma_y = 52{,}49 \cdot 68{,}65 = 3603{,}4$
- $\tau_{xy}^2 = (-48{,}46)^2 = 2348{,}4$
- $\sigma_x\sigma_y - \tau_{xy}^2 = 3603{,}4 - 2348{,}4 = 1255{,}0$

$$\sigma^2 - 121{,}14\,\sigma + 1255{,}0 = 0$$

### Rešitev kvadratne enačbe

$$\sigma = \frac{121{,}14 \pm \sqrt{121{,}14^2 - 4 \cdot 1255{,}0}}{2} = \frac{121{,}14 \pm \sqrt{14\,674{,}9 - 5020{,}0}}{2}$$

$$= \frac{121{,}14 \pm \sqrt{9654{,}9}}{2} = \frac{121{,}14 \pm 98{,}26}{2}$$

$$\sigma_{I} = \frac{121{,}14 + 98{,}26}{2} = \frac{219{,}40}{2} = \boxed{109{,}7\ \text{MPa}}$$

$$\sigma_{III} = \frac{121{,}14 - 98{,}26}{2} = \frac{22{,}88}{2} = \boxed{11{,}44\ \text{MPa}}$$

> **glej:** [[Koncept - Napetostno stanje#Lastne vrednosti tenzorja — 3D glavne napetosti]]

---

## Korak 5 — Razvrstitev glavnih napetosti

$$\sigma_1 \geq \sigma_2 \geq \sigma_3$$

$$\boxed{\sigma_1 = 109{,}7\ \text{MPa}}, \quad \boxed{\sigma_2 = 36{,}35\ \text{MPa}}, \quad \boxed{\sigma_3 = 11{,}44\ \text{MPa}}$$

Vse tri so **pozitivne** (natezne) — telo je po vseh smereh natezno obremenjeno.

---

## Kontrola

**Preveritev invariante $I_1$** (sled je invarianta — neodvisna od koordinatnega sistema):

$$\sigma_x + \sigma_y + \sigma_z = 52{,}49 + 68{,}65 + 36{,}35 = 157{,}49\ \text{MPa}$$

$$\sigma_1 + \sigma_2 + \sigma_3 = 109{,}7 + 36{,}35 + 11{,}44 = 157{,}49\ \text{MPa}\ ✓$$

Vsoti se ujemata — izračun je pravilen!

---

## Povzetek

| Korak | Vsebina | Ključna enačba | Rezultat |
|-------|---------|----------------|---------|
| 1 | Laméjevi konstanti | $\lambda = E\nu/((1+\nu)(1-2\nu))$, $G = E/(2(1+\nu))$ | λ=121 154, G=80 769 MPa |
| 2 | Volumska dilatacija | $\varepsilon_v = \varepsilon_x+\varepsilon_y+\varepsilon_z$ | 3·10⁻⁴ |
| 3 | Napetostni tenzor | $\sigma_{ij} = \lambda\varepsilon_v\delta_{ij} + 2G\varepsilon_{ij}$ | σx=52.49, σy=68.65, σz=36.35, τxy=−48.46 MPa |
| 4 | Karakteristična enačba | $\det(\sigma_{ij}-\sigma\delta_{ij})=0$ | kvadratna enačba |
| 5 | Glavne napetosti | razvrsti σ1≥σ2≥σ3 | **109.7, 36.35, 11.44 MPa** |

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]]
- [[Koncept - Vztrajnostni moment]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

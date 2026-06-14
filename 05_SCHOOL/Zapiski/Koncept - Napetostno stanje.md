---
tags: [mehanika, napetostno-stanje, Mohr, tenzor, glavne-napetosti, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — Napetostno stanje in Mohrova krožnica

## Namen

Iz danega napetostnega stanja (σx, σy, τxy) izračunati **glavne napetosti** σ₁,₂, **maksimalno strižno napetost** τmax in **kot** θ zasuka na glavne smeri. **Pogosta tema na izpitu.**

---

## Definicija napetostnega stanja (2D)

Napetostno stanje v točki opisujemo z napetostnim tenzorjem:

$$\sigma_{ij} = \begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{xy} & \sigma_y \end{pmatrix}$$

- $\sigma_x$, $\sigma_y$ — normalne napetosti (+ nateg, − tlak)
- $\tau_{xy}$ — strižna napetost (simetrija: $\tau_{xy} = \tau_{yx}$)

> ℹ️ Na izpitu pogosto podano kot matrika $\sigma_{ij}$ v MPa ali kN/cm². Tridimenzionalni tenzor: tretja vrstica/stolpec za $z$-komponente — v 2D jih zanemarimo.

---

## Transformacijske enačbe

Za koordinatni sistem, zasukan za kot $\varphi$:

$$\sigma_{\varphi} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\varphi + \tau_{xy}\sin 2\varphi$$

$$\tau_{\varphi} = -\frac{\sigma_x - \sigma_y}{2}\sin 2\varphi + \tau_{xy}\cos 2\varphi$$

---

## Glavne napetosti σ₁,₂

Glavne napetosti so ekstremi normalnih napetosti (tam kjer $\tau = 0$):

$$\boxed{\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}}$$

**Definicija:** $\sigma_1 \geq \sigma_2$ (večja je σ₁)

### Polmer Mohrove krožnice:

$$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

Torej: $\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm R$

---

## Maksimalna strižna napetost

$$\boxed{\tau_{max} = R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}}$$

> 🔍 $\tau_{max}$ nastopi pri kotu $\varphi_{max} = \varphi_0 + 45°$ (45° od smeri glavnih napetosti)

---

## Kot do glavnih smeri

$$\tan 2\varphi_0 = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

$$\boxed{\varphi_0 = \frac{1}{2}\arctan\frac{2\tau_{xy}}{\sigma_x - \sigma_y}}$$

> ⚠️ **Preveritev:** vstavi $\varphi_0$ nazaj v transformacijsko enačbo za $\sigma$ → moraš dobiti σ₁ ali σ₂!

---

## Mohrova krožnica — grafična metoda

### Kako narisati:

1. Na x-osi: normalne napetosti $\sigma$ (+ desno)
2. Na y-osi: strižne napetosti $\tau$ (+ navzdol, konvencija!)
3. Vpiši točki: $A = (\sigma_x, \tau_{xy})$ in $B = (\sigma_y, -\tau_{xy})$
4. Sredina krožnice: $C = \left(\frac{\sigma_x+\sigma_y}{2},\ 0\right)$
5. Polmer: $R = |CA|$
6. Krožnica seka os $\sigma$ pri $\sigma_1$ in $\sigma_2$

```
        τ
        |     A(σx, τxy)
        |    /
  ------+---C--------+-- σ
  σ₂   |    \       σ₁
        |     B(σy,-τxy)
```

> **Kot 2φ₀ na krožnici** = kot od AB daljice do osi σ (merimo v smeri nasprotni urinih kazalcev za pozitiven φ₀)

---

## Algoritem (5 korakov)

### Korak 1 — Preberi napetostno stanje

Iz naloge razberito $\sigma_x$, $\sigma_y$, $\tau_{xy}$ (pozor na predznake!).

### Korak 2 — Izračunaj povprečno napetost in polmer

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2}, \qquad R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

### Korak 3 — Glavne napetosti

$$\sigma_1 = \sigma_{sr} + R, \qquad \sigma_2 = \sigma_{sr} - R$$

### Korak 4 — Kot θ

$$2\varphi_0 = \arctan\frac{2\tau_{xy}}{\sigma_x - \sigma_y}, \qquad \varphi_0 = \frac{2\varphi_0}{2}$$

### Korak 5 — Kontrola

Vstavi $\varphi_0$ v transformacijsko enačbo: $\sigma_{\varphi_0}$ mora biti $\sigma_1$ ali $\sigma_2$.

$$\sigma(\varphi_0) = \sigma_{sr} + \frac{\sigma_x-\sigma_y}{2}\cos 2\varphi_0 + \tau_{xy}\sin 2\varphi_0$$

> **glej:** [[Koncept - NTM Diagrami]]

---

## Primer — Iz izpita 9.9.2006

**Dano:** $\sigma_{ij} = \begin{pmatrix} -10 & 30 \\ 30 & -10 \end{pmatrix}$ MPa (2D)

Torej: $\sigma_x = -10$ MPa, $\sigma_y = -10$ MPa, $\tau_{xy} = 30$ MPa

**Korak 2:**
$$\sigma_{sr} = \frac{-10 + (-10)}{2} = -10\ \text{MPa}$$
$$R = \sqrt{\left(\frac{-10-(-10)}{2}\right)^2 + 30^2} = \sqrt{0 + 900} = 30\ \text{MPa}$$

**Korak 3:**
$$\sigma_1 = -10 + 30 = +20\ \text{MPa} \quad \text{(nateg)}$$
$$\sigma_2 = -10 - 30 = -40\ \text{MPa} \quad \text{(tlak)}$$

**Korak 4:**
$$\tan 2\varphi_0 = \frac{2 \cdot 30}{-10 - (-10)} = \frac{60}{0} = \infty \quad \Rightarrow \quad 2\varphi_0 = 90° \quad \Rightarrow \quad \varphi_0 = 45°$$

**Maksimalna strižna napetost:**
$$\tau_{max} = R = 30\ \text{MPa}$$

---

## Primer — Splošen primer

**Dano:** $\sigma_x = 50$ MPa, $\sigma_y = -10$ MPa, $\tau_{xy} = 30$ MPa

$$\sigma_{sr} = \frac{50 + (-10)}{2} = 20\ \text{MPa}$$
$$R = \sqrt{30^2 + 30^2} = \sqrt{900 + 900} = \sqrt{1800} = 42{,}43\ \text{MPa}$$
$$\sigma_1 = 20 + 42{,}43 = +62{,}43\ \text{MPa}$$
$$\sigma_2 = 20 - 42{,}43 = -22{,}43\ \text{MPa}$$
$$\tau_{max} = 42{,}43\ \text{MPa}$$
$$2\varphi_0 = \arctan\frac{60}{60} = \arctan 1 = 45° \quad \Rightarrow \quad \varphi_0 = 22{,}5°$$

---

## Posebni primeri

| Stanje | $\sigma_x$ | $\sigma_y$ | $\tau_{xy}$ | Rezultat |
|--------|-----------|-----------|------------|---------|
| Enoosno natezno | σ | 0 | 0 | σ₁=σ, σ₂=0, τmax=σ/2 |
| Čisto strižno | 0 | 0 | τ | σ₁=+τ, σ₂=−τ, φ₀=45° |
| Dvoosno enakomerno | σ | σ | 0 | σ₁=σ₂=σ, τmax=0 |
| Hidrostatično | p | p | 0 | σ₁=σ₂=p, R=0 |

---

## Kombinirane obremenitve → napetostno stanje

Pogosto je napetostno stanje kombinirano iz upogiba + torzije:

| Obremenitev | Napetost | Kjer nastopi |
|-------------|----------|-------------|
| Upogib $M$ | $\sigma_x = M/W$ | rob prereza (max) |
| Torzija $M_t$ | $\tau_{xy} = M_t/W_t$ | rob prereza |
| Nateg/tlak $N$ | $\sigma_x = N/A$ | po celem prerezu |
| Prečna sila $T$ | $\tau_{xy} = T \cdot S / (I \cdot b)$ | nevtralna os (max) |

Za dimenzioniranje pri kombiniranih obremenitvah:

$$\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop} \quad \text{(Von Mises)}$$

> **glej:** [[Koncept - Upogib#Korak 4 — Napetosti in predznak]]

---

## Pogosta napaka

> **Napaka:** Zamešanje $\tau_{xy}$ s $\sigma_y$ — tenzor ima $\tau$ na nediago­nalnih mestih!
> 
> **Napaka:** Kot $\varphi_0$ je zasuk v **fizičnem prostoru** — na Mohrovi krožnici je kota **2φ₀**!

---

## Rešene naloge

- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] — kombinirano σ iz M-diagrama
- Primer iz izpita 9.9.2006 — σij tenzor → σ1,2 (zgoraj)

---

## Povezave

- [[Koncept - NTM Diagrami]]
- [[Koncept - Upogib]]
- [[Koncept - Torzija]]
- [[Koncept - Vztrajnostni moment]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

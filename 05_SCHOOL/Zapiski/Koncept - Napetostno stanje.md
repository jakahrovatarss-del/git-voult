---
tags: [mehanika, napetostno-stanje, Mohr, tenzor, glavne-napetosti, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — Napetostno stanje in Mohrova krožnica

## Namen

Iz danega napetostnega stanja (σx, σy, τxy) izračunati **glavne napetosti** σ₁,₂, **maksimalno strižno napetost** τmax in **kot** θ zasuka na glavne smeri. **Pogosta tema na izpitu.**

---

![[mohrova_kroznica.svg]]
![[napetostni_element_3d.svg]]

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

> ⚠️ **Pozor:** $\varphi$ je kot **normale** na ravnino od osi x (ne ravnine same!). V formulah nastopa $2\varphi$.

> **Primer:** [[Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine]] — 4 primeri z izračunom σ_φ in τ_φ

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

---

## 3D Napetostno stanje — Hookov zakon in Laméjeve konstante

> ℹ️ Ta razdelek se nanaša na **tenzorsko analizo** — kadar je dano deformacijsko stanje εij in iščemo napetosti σij.

### Materialne konstante

Iz $E$ (Young) in $\nu$ (Poisson) izpeljemo dve Laméjevi konstanti:

$$\boxed{\lambda = \frac{E \nu}{(1+\nu)(1-2\nu)}}$$

$$\boxed{G = \frac{E}{2(1+\nu)}}$$

- $\lambda$ [MPa] — 1. Laméjeva konstanta (poveže volumsko dilatacijo z napetostjo)
- $G$ [MPa] — strižni modul

**Za jeklo** ($E = 210\,000$ MPa, $\nu = 0{,}3$):
$$\lambda = \frac{210000 \cdot 0{,}3}{1{,}3 \cdot 0{,}4} = 121\,154\ \text{MPa}, \qquad G = \frac{210000}{2 \cdot 1{,}3} = 80\,769\ \text{MPa}$$

> **glej:** [[Koncept - Torzija#Formule za prereze]]

### Volumska dilatacija

$$\boxed{\varepsilon_v = \varepsilon_x + \varepsilon_y + \varepsilon_z = \text{sled}(\varepsilon_{ij})}$$

> 🔍 Volumska dilatacija = relativna sprememba prostornine telesa. Sled tenzorja = vsota diagonalnih komponent.

### Hookov zakon v 3D (tenzorska oblika)

$$\boxed{\sigma_{ij} = \lambda \varepsilon_v \delta_{ij} + 2G\,\varepsilon_{ij}}$$

kjer je $\delta_{ij}$ Kroneckerjev delta ($\delta_{ii}=1$, $\delta_{ij}=0$ za $i\neq j$).

**Eksplicitno za vsako komponento:**

$$\sigma_x = \lambda\varepsilon_v + 2G\varepsilon_x, \quad \sigma_y = \lambda\varepsilon_v + 2G\varepsilon_y, \quad \sigma_z = \lambda\varepsilon_v + 2G\varepsilon_z$$

$$\tau_{xy} = 2G\varepsilon_{xy}, \quad \tau_{xz} = 2G\varepsilon_{xz}, \quad \tau_{yz} = 2G\varepsilon_{yz}$$

> ⚠️ **Pozor na faktor 2:** V inženirski notaciji je $\gamma_{xy} = 2\varepsilon_{xy}$ (tehnični strižni kot). Tenzorska komponenta $\varepsilon_{xy}$ je torej **polovica** tehničnega strižnega kota!

### Inverz — deformacije iz napetosti

$$\varepsilon_x = \frac{1}{E}[\sigma_x - \nu(\sigma_y + \sigma_z)]$$
$$\varepsilon_y = \frac{1}{E}[\sigma_y - \nu(\sigma_x + \sigma_z)]$$
$$\varepsilon_z = \frac{1}{E}[\sigma_z - \nu(\sigma_x + \sigma_y)]$$
$$\gamma_{xy} = \frac{\tau_{xy}}{G}, \quad \gamma_{xz} = \frac{\tau_{xz}}{G}, \quad \gamma_{yz} = \frac{\tau_{yz}}{G}$$

> 🔍 **Fizikalni pomen:** $\nu$ opisuje, koliko se material v prečni smeri skrči, ko ga nategnemo vzdolžno. Za jeklo $\nu \approx 0{,}3$ — 30% prečnega skrčka glede na vzdolžni nateg.

> ⚠️ **Ključna napaka:** Deformacija $\varepsilon_z$ je odvisna od **vseh treh** napetosti (Poissonov efekt). Zanemaritev $\nu$ pri kvaderju → 21% napaka!

> **Primer:** [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]] — F iz pogoja ΔH z upoštevanjem Poissona

---

## Lastne vrednosti tenzorja — 3D glavne napetosti

Ko imamo 3D napetostni tenzor:

$$\sigma_{ij} = \begin{pmatrix} \sigma_x & \tau_{xy} & \tau_{xz} \\ \tau_{xy} & \sigma_y & \tau_{yz} \\ \tau_{xz} & \tau_{yz} & \sigma_z \end{pmatrix}$$

Glavne napetosti $\sigma_1, \sigma_2, \sigma_3$ so lastne vrednosti tega tenzorja:

$$\det(\sigma_{ij} - \sigma \delta_{ij}) = 0$$

### Karakteristična enačba:

$$\sigma^3 - I_1 \sigma^2 + I_2 \sigma - I_3 = 0$$

kjer so **invariante tenzorja napetosti**:

$$I_1 = \sigma_x + \sigma_y + \sigma_z \quad \text{(sled)}$$

$$I_2 = \sigma_x\sigma_y + \sigma_y\sigma_z + \sigma_x\sigma_z - \tau_{xy}^2 - \tau_{yz}^2 - \tau_{xz}^2$$

$$I_3 = \det(\sigma_{ij}) \quad \text{(determinanta)}$$

### Poenostavitev — kadar je $\tau_{xz} = \tau_{yz} = 0$:

Tenzor se razpade na 2D podmatriko + σz:

- Ena glavna napetost: $\sigma_2 = \sigma_z$ (direktno)
- Preostali dve iz 2D enačbe:

$$(\sigma_x - \sigma)(\sigma_y - \sigma) - \tau_{xy}^2 = 0$$

$$\sigma^2 - (\sigma_x + \sigma_y)\sigma + (\sigma_x \sigma_y - \tau_{xy}^2) = 0$$

$$\boxed{\sigma_{1,3} = \frac{(\sigma_x+\sigma_y) \pm \sqrt{(\sigma_x+\sigma_y)^2 - 4(\sigma_x\sigma_y - \tau_{xy}^2)}}{2}}$$

Razvrstimo: $\sigma_1 \geq \sigma_2 \geq \sigma_3$.

---

## Algoritem — od deformacijskega tenzorja do glavnih napetosti

```
KORAK 0: Preberi εij in materialne konstante E, ν

KORAK 1: Izračunaj λ in G
   λ = Eν / ((1+ν)(1-2ν))
   G = E / (2(1+ν))

KORAK 2: Volumska dilatacija
   εv = εx + εy + εz

KORAK 3: Napetostni tenzor
   σx = λεv + 2G·εx
   σy = λεv + 2G·εy
   σz = λεv + 2G·εz
   τxy = 2G·εxy  (pozor: εxy = γxy/2!)

KORAK 4: Zapiši σij matriko

KORAK 5: Glavne napetosti
   Če τxz=τyz=0: σ2=σz, reši kvadratno enačbo za σ1,σ3
   Splošno: karakteristična kubična enačba

KORAK 6: Razvrsti σ1 ≥ σ2 ≥ σ3
```

> **Primer:** [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]

---

## Rešene naloge

- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] — kombinirano σ iz M-diagrama
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]] — εij → σij → σ1,2,3 (IMG_1241 str. 3-5)
- [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]] — 3D Hooke, F iz εz
- [[Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine]] — σφ, τφ na zasučeni ravnini
- [[Naloga - Mehanika - Izpit Jul2018 - Cisto strizno stanje]] — σx=σy=0, τxy=50 MPa → φ₀=45° vedno
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]] — 3D tenzor → glavne napetosti → Tresca/Von Mises
- Primer iz izpita 9.9.2006 — σij tenzor → σ1,2 (2D, zgoraj)

---

## Povezave

- [[Koncept - NTM Diagrami]]
- [[Koncept - Upogib]]
- [[Koncept - Torzija]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]]
- [[Naloga - Mehanika - Tenzorska analiza - nagnjene ravnine]]
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]]
- [[Naloga - Mehanika - Izpit Jul2018 - Cisto strizno stanje]]
- [[Koncept - Hipoteze Porusitve]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

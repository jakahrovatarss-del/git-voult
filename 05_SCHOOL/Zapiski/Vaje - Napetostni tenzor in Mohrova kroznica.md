---
tags: [mehanika, napetostno-stanje, Mohr, tenzor, Tresca, VonMises, izpit, vaje]
predmet: Mehanika
datum: 2026-06-15
---

# Vaje — Napetostni tenzor in Mohrova krožnica (vse vrste za izpit)

**Predmet:** Mehanika (LE007) · **Tema:** Napetostno stanje, Mohrova krožnica, ekvivalentne napetosti  
**Namen:** Obvladati vse tipe nalog ki se pojavijo na izpitu BTF Lesarstvo UN

---

## Splošni postopek (6 korakov)

> Nauči se to zaporedje — na izpitu ga sledi mehanično.

### KORAK 0 — Prepoznaj tip naloge

| Tip | Dano | Iščemo |
|-----|------|--------|
| **2D direktno** | σx, σy, τxy | σ1,2, τmax, φ0, Mohrova krož. |
| **3D tenzor** | matrika σij | karakterist. enačba → σ1,2,3 → Tresca/VM |
| **Kombinirano** | M, Mt, F, prerez | σ in τ → napetostno stanje → σekv |
| **Deformacijski** | εij, E, ν | Laméjevi → σij → σ1,2,3 |

### KORAK 1 — Preberi σx, σy, τxy

$$\sigma_{ij} = \begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{xy} & \sigma_y \end{pmatrix}$$

> ⚠️ Pozor: $\tau$ je na **ne-diagonalnih** mestih tenzorja!

### KORAK 2 — Središče in polmer

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2}, \qquad R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

### KORAK 3 — Glavne napetosti

$$\boxed{\sigma_{1,2} = \sigma_{sr} \pm R}$$

### KORAK 4 — Kot do glavnih smeri

$$\tan 2\varphi_0 = \frac{2\tau_{xy}}{\sigma_x - \sigma_y} \implies \varphi_0 = \frac{1}{2}\arctan\frac{2\tau_{xy}}{\sigma_x-\sigma_y}$$

> $\varphi_0$ = zasuk v **fizičnem prostoru**; na Mohrovi krožnici je **$2\varphi_0$**!

### KORAK 5 — Ekvivalentne napetosti

$$\sigma_{ekv,\text{Tresca}} = \max(|\sigma_1-\sigma_2|,\ |\sigma_2-\sigma_3|,\ |\sigma_3-\sigma_1|)$$

$$\sigma_{ekv,\text{VM}} = \sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\right]}$$

> ⚠️ **Tresca > Von Mises** vedno → Tresca je bolj konzervativna (varnejša)!

### KORAK 6 — Kontrola

$$I_1 = \sigma_x+\sigma_y+\sigma_z = \sigma_1+\sigma_2+\sigma_3 \quad \checkmark \text{ (sled je invarianta)}$$

---

## NALOGA 1 — 2D Mohrova krožnica (osnovna)

![[mohr_naloga1.svg]]

### Podatki

$$\sigma_{ij} = \begin{pmatrix} 80 & 40 \\ 40 & -20 \end{pmatrix}\ \text{MPa}$$

Torej: $\sigma_x = 80\ \text{MPa}$, $\sigma_y = -20\ \text{MPa}$, $\tau_{xy} = 40\ \text{MPa}$

### KORAK 2 — Središče in polmer

$$\sigma_{sr} = \frac{80 + (-20)}{2} = \frac{60}{2} = \boxed{30\ \text{MPa}}$$

$$R = \sqrt{\left(\frac{80-(-20)}{2}\right)^2 + 40^2} = \sqrt{50^2 + 40^2} = \sqrt{2500 + 1600} = \sqrt{4100} = \boxed{64{,}03\ \text{MPa}}$$

### KORAK 3 — Glavne napetosti

$$\sigma_1 = 30 + 64{,}03 = \boxed{+94{,}03\ \text{MPa}} \quad \text{(nateg)}$$

$$\sigma_2 = 30 - 64{,}03 = \boxed{-34{,}03\ \text{MPa}} \quad \text{(tlak)}$$

$$\tau_{max} = R = \boxed{64{,}03\ \text{MPa}}$$

### KORAK 4 — Kot do glavnih smeri

$$\tan 2\varphi_0 = \frac{2 \cdot 40}{80 - (-20)} = \frac{80}{100} = 0{,}8$$

$$2\varphi_0 = \arctan 0{,}8 = 38{,}66° \implies \boxed{\varphi_0 = 19{,}33°}$$

### KORAK 5 — Mohrova krožnica (koraki risanja)

1. Nariši os $\sigma$ (vodoravno) in os $\tau$ (navpično, $\tau^+$ navzdol po konvenciji)
2. Vnesi točki:
   - $A = (\sigma_x,\ \tau_{xy}) = (80,\ 40)$ → na Mohrovi krožnici desno spodaj
   - $B = (\sigma_y,\ {-}\tau_{xy}) = (-20,\ {-}40)$ → levo zgoraj
3. Središče $C = (30,\ 0)$
4. Nariši krožnico s polmerom $R = 64{,}03$ MPa
5. Presečišči z osjo $\sigma$: $\sigma_1 = 94{,}03$, $\sigma_2 = -34{,}03$ MPa
6. Kot $2\varphi_0 = 38{,}66°$ od daljice AB do osi $\sigma$

### Kontrola

$$I_1 = \sigma_x + \sigma_y = 80 + (-20) = 60 = \sigma_1 + \sigma_2 = 94{,}03 + (-34{,}03) = 60\ \checkmark$$

> **Tipična napaka:** Zamešati točki A in B (A je vedno x-ploskev z $+\tau_{xy}$, B je y-ploskev z $-\tau_{xy}$).

> **glej:** [[Koncept - Napetostno stanje#Mohrova krožnica — grafična metoda]]

---

## NALOGA 2 — 3D tenzor, ravninsko stanje (tip Jul. 2018, Feb. 2019)

![[mohr_naloga2.svg]]

### Podatki

$$\sigma_{ij} = \begin{pmatrix} -100 & -300 & 0 \\ -300 & 200 & 0 \\ 0 & 0 & 0 \end{pmatrix}\ \text{MPa}$$

### KORAK 1 — Prepoznaj poenostavitev

Ker $\tau_{xz} = \tau_{yz} = 0$ in $\sigma_z = 0$: **ravninsko napetostno stanje** (plane stress).

Direktno: ena glavna napetost je $\sigma_z = 0$ MPa.

Za preostali dve rešimo iz 2D podmatrike $\begin{pmatrix} -100 & -300 \\ -300 & 200 \end{pmatrix}$.

### KORAK 2 — Karakteristična enačba (kvadratna)

$$(\sigma_x - \sigma)(\sigma_y - \sigma) - \tau_{xy}^2 = 0$$

$$\sigma^2 - (\sigma_x + \sigma_y)\,\sigma + (\sigma_x\sigma_y - \tau_{xy}^2) = 0$$

Vstavim:
- $\sigma_x + \sigma_y = -100 + 200 = 100$
- $\sigma_x\sigma_y = (-100)(200) = -20\,000$
- $\tau_{xy}^2 = (-300)^2 = 90\,000$
- $\sigma_x\sigma_y - \tau_{xy}^2 = -20\,000 - 90\,000 = -110\,000$

$$\boxed{\sigma^2 - 100\,\sigma - 110\,000 = 0}$$

### KORAK 3 — Rešitev kvadratne enačbe

$$\sigma = \frac{100 \pm \sqrt{100^2 + 4 \cdot 110\,000}}{2} = \frac{100 \pm \sqrt{10\,000 + 440\,000}}{2} = \frac{100 \pm \sqrt{450\,000}}{2}$$

$$\sqrt{450\,000} = 150\sqrt{20} = 150 \cdot 4{,}4721 = 670{,}82\ \text{MPa}$$

$$\sigma' = \frac{100 + 670{,}82}{2} = \frac{770{,}82}{2} = \boxed{385{,}4\ \text{MPa}}$$

$$\sigma'' = \frac{100 - 670{,}82}{2} = \frac{-570{,}82}{2} = \boxed{-285{,}4\ \text{MPa}}$$

### KORAK 4 — Razvrstitev vseh treh

$$\sigma_1 \geq \sigma_2 \geq \sigma_3$$

$$\boxed{\sigma_1 = +385{,}4\ \text{MPa}}, \quad \boxed{\sigma_2 = 0\ \text{MPa}}, \quad \boxed{\sigma_3 = -285{,}4\ \text{MPa}}$$

### KORAK 5 — Ekvivalentne napetosti

**Tresca (bolj konzervativna):**

$$\sigma_{ekv} = \max(|\sigma_1-\sigma_2|,\ |\sigma_2-\sigma_3|,\ |\sigma_1-\sigma_3|)$$

$$= \max(|385{,}4-0|,\ |0-(-285{,}4)|,\ |385{,}4-(-285{,}4)|)$$

$$= \max(385{,}4;\ 285{,}4;\ 670{,}8) = \boxed{670{,}8\ \text{MPa}}$$

**Von Mises (manj konzervativna):**

$$\sigma_{ekv} = \sqrt{\frac{1}{2}\left[(385{,}4-0)^2+(0-(-285{,}4))^2+(385{,}4-(-285{,}4))^2\right]}$$

$$= \sqrt{\frac{1}{2}\left[148\,533 + 81\,453 + 449\,822\right]} = \sqrt{\frac{679\,808}{2}} = \sqrt{339\,904} = \boxed{583{,}0\ \text{MPa}}$$

### Primerjava

| Hipoteza | $\sigma_{ekv}$ | Razlika |
|----------|---------------|---------|
| Tresca | 670,8 MPa | +15,1% |
| Von Mises | 583,0 MPa | — (osnova) |

> **Ključna opazka:** Tresca je merodajna, ker je $\sigma_2 = 0$ (sredi med $\sigma_1$ in $\sigma_3$) — razlika med $\sigma_1$ in $\sigma_3$ je odločilna.

### Kontrola

$$I_1 = \sigma_x+\sigma_y+\sigma_z = -100+200+0 = 100\ \text{MPa}$$
$$\sigma_1+\sigma_2+\sigma_3 = 385{,}4+0+(-285{,}4) = 100\ \text{MPa}\ \checkmark$$

> **Pogosta napaka:** Pozabiti $\sigma_2 = \sigma_z = 0$ pri razvrstivti. Brez tega Tresca pride napačno!

> **glej:** [[Koncept - Napetostno stanje#Lastne vrednosti tenzorja — 3D glavne napetosti]]

---

## NALOGA 3 — Kombinirano: upogib + torzija → ekvivalentne napetosti

![[mohr_naloga3.svg]]

### Podatki

Okrogla jeklenka greda:
- Premer: $d = 80\ \text{mm}$
- Upogibni moment: $M = 8\ \text{kNm} = 8 \times 10^6\ \text{N·mm}$
- Torzijski moment: $M_t = 4\ \text{kNm} = 4 \times 10^6\ \text{N·mm}$
- Material: jeklo, $\sigma_{dop} = 200\ \text{MPa}$

**Naloga:** Preveri varnost prereza (Tresca in Von Mises).

### KORAK 1 — Odpornostna momenta prereza

$$W = \frac{\pi d^3}{32} = \frac{\pi \cdot 80^3}{32} = \frac{\pi \cdot 512\,000}{32} = \boxed{50\,265\ \text{mm}^3}$$

$$W_t = \frac{\pi d^3}{16} = 2W = \boxed{100\,531\ \text{mm}^3}$$

> 💡 **Trik:** $W_t = 2W$ vedno za okrogle prereze!

### KORAK 2 — Napetosti na kritičnem vlaknu

Kritično vlakno = rob prereza (največji $\sigma$ od upogiba, in hkrati maksimalni $\tau$ od torzije).

$$\sigma_x = \sigma = \frac{M}{W} = \frac{8 \times 10^6}{50\,265} = \boxed{159{,}15\ \text{MPa}}$$

$$\tau_{xy} = \tau = \frac{M_t}{W_t} = \frac{4 \times 10^6}{100\,531} = \boxed{39{,}79\ \text{MPa}}$$

Napetostno stanje:

$$\sigma_{ij} = \begin{pmatrix} 159{,}15 & 39{,}79 \\ 39{,}79 & 0 \end{pmatrix}\ \text{MPa}$$

### KORAK 3 — Mohrova krožnica

$$\sigma_{sr} = \frac{159{,}15 + 0}{2} = 79{,}58\ \text{MPa}$$

$$R = \sqrt{79{,}58^2 + 39{,}79^2} = \sqrt{6332 + 1583} = \sqrt{7915} = \boxed{88{,}97\ \text{MPa}}$$

$$\sigma_1 = 79{,}58 + 88{,}97 = \boxed{+168{,}55\ \text{MPa}}$$

$$\sigma_2 = 79{,}58 - 88{,}97 = \boxed{-9{,}39\ \text{MPa}}$$

$$\sigma_3 = 0\ \text{MPa} \quad \text{(ravninsko stanje)}$$

### KORAK 4 — Ekvivalentne napetosti

**Von Mises (alternativna formula za kombinirano):**

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} = \sqrt{159{,}15^2 + 3 \cdot 39{,}79^2} = \sqrt{25\,329 + 4\,752} = \sqrt{30\,081} = \boxed{173{,}4\ \text{MPa}}$$

**Tresca (alternativna formula za kombinirano):**

$$\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} = \sqrt{159{,}15^2 + 4 \cdot 39{,}79^2} = \sqrt{25\,329 + 6\,336} = \sqrt{31\,665} = \boxed{177{,}9\ \text{MPa}}$$

### KORAK 5 — Preverjanje varnosti

| Hipoteza | $\sigma_{ekv}$ | $\sigma_{dop}$ | Varno? |
|----------|---------------|----------------|--------|
| Von Mises | 173,4 MPa | 200 MPa | ✓ DA (varnostni faktor 1,15) |
| Tresca | 177,9 MPa | 200 MPa | ✓ DA (varnostni faktor 1,12) |

> **Zaključek:** Prerez je varen po obeh hipotezah. Tresca je kritičnejša.

> **Alternativna pot (skozi σ1, σ2, σ3 — preveritev):**
> $$\sigma_{ekv,VM} = \sqrt{\frac{1}{2}[(168{,}55-(-9{,}39))^2+(-9{,}39-0)^2+(168{,}55-0)^2]}$$
> $$= \sqrt{\frac{1}{2}[31\,658 + 88 + 28\,409]} = \sqrt{30\,077} = 173{,}4\ \text{MPa}\ \checkmark$$

> **Tipična napaka:** Prerez samo pri $M$ brez $M_t$ (ali obratno) — kombinirano stanje zahteva obe napetosti!

> **glej:** [[Koncept - Napetostno stanje#Kombinirane obremenitve → napetostno stanje]]

---

## NALOGA 4 — Deformacijski tenzor → napetostni tenzor → glavne napetosti

![[mohr_naloga4.svg]]

### Podatki

$$\varepsilon_{ij} = \begin{pmatrix} 2 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 0{,}5 \end{pmatrix} \cdot 10^{-4}$$

Materialne konstante: $E = 210\,000\ \text{MPa}$, $\nu = 0{,}3$

**Naloga:** Izračunaj napetostni tenzor $\sigma_{ij}$ in glavne napetosti $\sigma_1, \sigma_2, \sigma_3$.

### KORAK 1 — Laméjevi konstanti

$$\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)} = \frac{210\,000 \cdot 0{,}3}{1{,}3 \cdot 0{,}4} = \frac{63\,000}{0{,}52} = \boxed{121\,154\ \text{MPa}}$$

$$G = \frac{E}{2(1+\nu)} = \frac{210\,000}{2{,}6} = \boxed{80\,769\ \text{MPa}}$$

> 💡 **Trik:** λ in G sta za jeklo vedno enaki vrednosti — zapomni si jih!

### KORAK 2 — Volumska dilatacija

$$\varepsilon_v = \varepsilon_x + \varepsilon_y + \varepsilon_z = (2 + (-1) + 0{,}5) \cdot 10^{-4} = \boxed{1{,}5 \cdot 10^{-4}}$$

$$\lambda\varepsilon_v = 121\,154 \cdot 1{,}5 \cdot 10^{-4} = \boxed{18{,}17\ \text{MPa}}$$

### KORAK 3 — Napetostni tenzor (Hookov zakon)

Splošna formula: $\sigma_{ij} = \lambda\varepsilon_v\delta_{ij} + 2G\varepsilon_{ij}$

**Normalne napetosti** (diagonala):

$$\sigma_x = \lambda\varepsilon_v + 2G\varepsilon_x = 18{,}17 + 2 \cdot 80\,769 \cdot 2 \cdot 10^{-4} = 18{,}17 + 32{,}31 = \boxed{50{,}48\ \text{MPa}}$$

$$\sigma_y = \lambda\varepsilon_v + 2G\varepsilon_y = 18{,}17 + 2 \cdot 80\,769 \cdot (-1) \cdot 10^{-4} = 18{,}17 - 16{,}15 = \boxed{2{,}02\ \text{MPa}}$$

$$\sigma_z = \lambda\varepsilon_v + 2G\varepsilon_z = 18{,}17 + 2 \cdot 80\,769 \cdot 0{,}5 \cdot 10^{-4} = 18{,}17 + 8{,}08 = \boxed{26{,}25\ \text{MPa}}$$

**Strižna napetost** (izvendiagonalna):

> ⚠️ **Ključno:** $\tau_{xy} = 2G\varepsilon_{xy}$ — tenzorska komponenta $\varepsilon_{xy}$ je **polovica** tehničnega $\gamma_{xy}$!

$$\tau_{xy} = 2G\varepsilon_{xy} = 2 \cdot 80\,769 \cdot 1 \cdot 10^{-4} = \boxed{+16{,}15\ \text{MPa}}$$

$$\tau_{xz} = 0, \quad \tau_{yz} = 0$$

**Napetostni tenzor:**

$$\boxed{\sigma_{ij} = \begin{pmatrix} 50{,}48 & 16{,}15 & 0 \\ 16{,}15 & 2{,}02 & 0 \\ 0 & 0 & 26{,}25 \end{pmatrix}\ \text{MPa}}$$

### KORAK 4 — Glavne napetosti

Ker $\tau_{xz} = \tau_{yz} = 0$: direktno $\sigma_z = 26{,}25\ \text{MPa}$ je ena glavna napetost.

Za preostali dve: kvadratna enačba iz 2D podmatrike:

$$\sigma^2 - (\sigma_x+\sigma_y)\sigma + (\sigma_x\sigma_y - \tau_{xy}^2) = 0$$

Vrednosti:
- $\sigma_x+\sigma_y = 50{,}48 + 2{,}02 = 52{,}50$
- $\sigma_x\sigma_y = 50{,}48 \cdot 2{,}02 = 101{,}97$
- $\tau_{xy}^2 = 16{,}15^2 = 260{,}82$

$$\sigma^2 - 52{,}50\,\sigma + (101{,}97 - 260{,}82) = 0$$

$$\boxed{\sigma^2 - 52{,}50\,\sigma - 158{,}85 = 0}$$

$$D = 52{,}50^2 + 4 \cdot 158{,}85 = 2756{,}25 + 635{,}40 = 3391{,}65$$

$$\sqrt{D} = 58{,}24$$

$$\sigma' = \frac{52{,}50 + 58{,}24}{2} = \frac{110{,}74}{2} = \boxed{55{,}37\ \text{MPa}}$$

$$\sigma'' = \frac{52{,}50 - 58{,}24}{2} = \frac{-5{,}74}{2} = \boxed{-2{,}87\ \text{MPa}}$$

### KORAK 5 — Razvrstitev

$$\boxed{\sigma_1 = 55{,}37\ \text{MPa}}, \quad \boxed{\sigma_2 = 26{,}25\ \text{MPa}}, \quad \boxed{\sigma_3 = -2{,}87\ \text{MPa}}$$

### Kontrola

$$I_1 = \sigma_x+\sigma_y+\sigma_z = 50{,}48+2{,}02+26{,}25 = 78{,}75\ \text{MPa}$$

$$\sigma_1+\sigma_2+\sigma_3 = 55{,}37+26{,}25+(-2{,}87) = 78{,}75\ \text{MPa}\ \checkmark$$

> **Ključna napaka:** Faktor 2 pri $\tau_{xy} = 2G\varepsilon_{xy}$ — ne $G\varepsilon_{xy}$!

> **Razlaga:** $\varepsilon_{xy}$ (tenzorska) = $\gamma_{xy}/2$ (tehnična). $\tau_{xy} = G\gamma_{xy} = G \cdot 2\varepsilon_{xy} = 2G\varepsilon_{xy}$. Obe obliki dajo isti rezultat.

> **glej:** [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]] | [[Koncept - Napetostno stanje#Algoritem — od deformacijskega tenzorja do glavnih napetosti]]

---

## NALOGA 5 — Čisto strižno stanje + dimenzioniranje (Tresca vs Von Mises)

![[mohr_naloga5.svg]]

### Podatki

Okrogla jeklenka greda, samo torzija:
- Premer: $d = 60\ \text{mm}$
- Torzijski moment: $M_t = 2\ \text{kNm} = 2 \times 10^6\ \text{N·mm}$
- Material A: $\sigma_{dop} = 100\ \text{MPa}$ (jeklo S235)
- Material B: $\sigma_{dop} = 90\ \text{MPa}$ (jeklo S355, drugačna varnostna faktorja)

**Naloga:** (a) Izračunaj ekvivalentni napetosti po Tresca in Von Mises. (b) Ali greda varno prenese obremenitev? (c) Razloži razliko med hipotezama.

### KORAK 1 — Torzijska strižna napetost

$$W_t = \frac{\pi d^3}{16} = \frac{\pi \cdot 60^3}{16} = \frac{\pi \cdot 216\,000}{16} = \boxed{42\,412\ \text{mm}^3}$$

$$\tau = \frac{M_t}{W_t} = \frac{2 \times 10^6}{42\,412} = \boxed{47{,}16\ \text{MPa}}$$

### KORAK 2 — Napetostno stanje (čisto strižno)

$$\sigma_{ij} = \begin{pmatrix} 0 & 47{,}16 \\ 47{,}16 & 0 \end{pmatrix}\ \text{MPa}, \quad \sigma_z = 0$$

### KORAK 3 — Mohrova krožnica

$$\sigma_{sr} = \frac{0 + 0}{2} = 0, \qquad R = \sqrt{0^2 + 47{,}16^2} = 47{,}16\ \text{MPa}$$

$$\sigma_1 = +47{,}16\ \text{MPa}, \quad \sigma_2 = 0, \quad \sigma_3 = -47{,}16\ \text{MPa}$$

> 💡 **Posebnost čistega strižnega stanja:** Vedno $\sigma_1 = +\tau$, $\sigma_3 = -\tau$, in zasuk $\varphi_0 = 45°$!

Mohrova krožnica je centrirana v izhodišču — $\sigma_{sr} = 0$.

### KORAK 4 — Ekvivalentne napetosti

**Tresca:**

$$\sigma_{ekv,T} = \max(|\sigma_1-\sigma_2|,\ |\sigma_2-\sigma_3|,\ |\sigma_1-\sigma_3|)$$
$$= \max(47{,}16;\ 47{,}16;\ 94{,}32) = 94{,}32\ \text{MPa}$$

Ali direktno: $\sigma_{ekv,T} = 2\tau_{max} = 2 \cdot 47{,}16 = \boxed{94{,}32\ \text{MPa}}$

Preveritev z alternativno formulo:
$$\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} = \sqrt{0 + 4 \cdot 47{,}16^2} = 2 \cdot 47{,}16 = 94{,}32\ \text{MPa}\ \checkmark$$

**Von Mises:**

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} = \sqrt{0 + 3 \cdot 47{,}16^2} = 47{,}16\sqrt{3} = 47{,}16 \cdot 1{,}7321 = \boxed{81{,}65\ \text{MPa}}$$

### KORAK 5 — Dimenzioniranje

| Hipoteza | $\sigma_{ekv}$ | Mat. A ($\sigma_{dop}=100$) | Mat. B ($\sigma_{dop}=90$) |
|----------|---------------|---------------------------|---------------------------|
| Von Mises | 81,65 MPa | ✓ varno (k=1,22) | ✓ varno (k=1,10) |
| Tresca | 94,32 MPa | ✓ varno (k=1,06) | ✗ **NE varno!** (94,32 > 90) |

> **Zaključek:** Za Material B je napoved odvisna od hipoteze! Tresca (bolj konzervativna) zahteva večji prerez ali boljši material.

### KORAK 6 — Razlaga razlike med hipotezama

| | Tresca | Von Mises |
|--|--------|-----------|
| **Fizikalni pomen** | Max strižna napetost | Energija distorzije |
| **Čisto strižno** | $\sigma_{ekv} = 2\tau$ | $\sigma_{ekv} = \tau\sqrt{3}$ |
| **Razmerje** | 2 | 1,732 |
| **% razlika** | +15,5% | osnova |
| **Konzervativnost** | bolj konzervativna | manj konzervativna |
| **Raba** | konstrukcijsko jeklo, les | duktilni materiali (aluminij) |

> ⚠️ **Na izpitu:** Če ni rečeno katera hipoteza, izračunaj **obe** in komentiraj razliko!

> **Zobacz:** [[Koncept - Napetostno stanje#Kombinirane obremenitve → napetostno stanje]] | [[Koncept - Hipoteze Porusitve]]

---

## Povzetek — kaj moraš znati za vsak tip

| Tip naloge | Ključni korak | Posebnost | Pogosta napaka |
|------------|--------------|-----------|----------------|
| 2D Mohr | $\sigma_{sr}$, $R$, točki A in B | $\tau^+$ navzdol po konvenciji | Zamešanje točk A in B |
| 3D tenzor | Kvadratna enačba + $\sigma_z$ direktno | Razvrstitev σ1≥σ2≥σ3! | Pozabiti σ2=σz pri ravninskem stanju |
| Upogib+torzija | $W = \pi d^3/32$, $W_t = 2W$ | Obe napetosti na istem vlaknu | Napaka W vs Wt |
| Deformacijski tenzor | $\lambda$, $G$; faktor 2 pri $\tau$ | $\tau = 2G\varepsilon_{xy}$ | $\varepsilon_{xy}$ je pol $\gamma_{xy}$! |
| Čisto strižno | $\sigma_1=+\tau$, $\sigma_3=-\tau$, $\varphi_0=45°$ | Tresca = 2τ; VM = τ√3 | Enačba samo za čist strig |

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]]
- [[Naloga - Mehanika - Izpit Jul2018 - Cisto strizno stanje]]
- [[Koncept - Upogib]]
- [[Koncept - Torzija]]
- [[Koncept - Hipoteze Porusitve]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

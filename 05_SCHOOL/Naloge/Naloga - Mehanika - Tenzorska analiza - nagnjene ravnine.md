---
tags: [mehanika, tenzor, napetosti, nagnjene-ravnine, transformacija, naloga]
predmet: Mehanika
datum: 2026-06-14
vir: IMG_1241.pdf, str. 28, 46
---

# Naloga: Napetosti na nagnjenih ravninah

## Namen

Za dano napetostno stanje ($\sigma_x$, $\sigma_y$, $\tau_{xy}$) izračunati **normalno napetost $\sigma_n$** in **strižno napetost $\tau_n$** na ravnini, ki je nagnjena za kot $\varphi$ od koordinatne x-osi.

---

![[nagnjene_ravnine.svg]]

## Formulozem

### Transformacijske enačbe:

$$\boxed{\sigma_\varphi = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\varphi + \tau_{xy}\sin 2\varphi}$$

$$\boxed{\tau_\varphi = -\frac{\sigma_x - \sigma_y}{2}\sin 2\varphi + \tau_{xy}\cos 2\varphi}$$

> ⚠️ Kot $\varphi$ je kot **normale** na ravnino od osi x (ne kot ravnine same!). Pozor: na formulah nastopa $2\varphi$!

---

## Primer 1 — Splošno napetostno stanje (stena, ravninsko strižno)

### Podatki

Stena $4 \times 3$ m se nagne za kot $\alpha = 0{,}01°$.

Kotni premik v radianih:
$$\gamma_{xy} = \alpha \cdot \frac{\pi}{180°} = 0{,}01 \cdot \frac{\pi}{180} = 1{,}745 \cdot 10^{-4}\ \text{rad}$$

Ker je samo strižna deformacija ($\varepsilon_x = \varepsilon_y = 0$), je deformacijski tenzor:

$$\varepsilon_{ij} = \begin{pmatrix} 0 & \gamma_{xy}/2 \\ \gamma_{xy}/2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0{,}872 \\ 0{,}872 & 0 \end{pmatrix} \cdot 10^{-4}$$

### Glavne deformacije

Za čisto strižno stanje ($\varepsilon_x = \varepsilon_y = 0$):

$$\varepsilon_{1,2} = \pm\frac{\gamma_{xy}}{2} = \pm 0{,}872 \cdot 10^{-4}$$

Glavne deformacije nastopijo pri $\varphi = 45°$ (kot pri napetostih!).

> **glej:** [[Koncept - Napetostno stanje#Posebni primeri]]

---

## Primer 2 — Napetosti na nagnjeni ravnini pod kotom 60°

### Podatki (iz izpita, IMG_1241 str. 28)

Napetostno stanje v točki (npr. iz kombiniranega upogiba + normalne sile):

$$\sigma_x = 0\ \text{MPa}, \qquad \sigma_y = 0\ \text{MPa}, \qquad \tau_{xy} = \tau\ \text{MPa}$$

Ravnina pod kotom $\varphi = 60°$ od normale (oz. ravnina je 30° od osi x).

### Izračun

$$\sigma_{60°} = \frac{0+0}{2} + \frac{0-0}{2}\cos 120° + \tau\sin 120°$$
$$= \tau \cdot \sin 120° = \tau \cdot \frac{\sqrt{3}}{2} = 0{,}866\tau$$

$$\tau_{60°} = -\frac{0-0}{2}\sin 120° + \tau\cos 120°$$
$$= \tau \cdot (-0{,}5) = -0{,}5\tau$$

---

## Primer 3 — Polna naloga z danim $\sigma_x, \sigma_y, \tau_{xy}$

### Podatki

$$\sigma_x = 50\ \text{MPa}, \quad \sigma_y = -10\ \text{MPa}, \quad \tau_{xy} = 30\ \text{MPa}$$

Vprašanje: izračunaj $\sigma_n$ in $\tau_n$ na ravnini z normalo pod kotom $\varphi = 30°$.

### Korak 1 — Povprečna napetost in amplituda

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2} = \frac{50 + (-10)}{2} = 20\ \text{MPa}$$

$$\frac{\sigma_x - \sigma_y}{2} = \frac{50 - (-10)}{2} = 30\ \text{MPa}$$

### Korak 2 — Trigonometrija za $2\varphi = 60°$

$$\cos 60° = 0{,}5, \qquad \sin 60° = 0{,}866$$

### Korak 3 — Napetosti na ravnini

$$\sigma_{30°} = 20 + 30 \cdot 0{,}5 + 30 \cdot 0{,}866 = 20 + 15 + 25{,}98 = \boxed{60{,}98\ \text{MPa}}$$

$$\tau_{30°} = -30 \cdot 0{,}866 + 30 \cdot 0{,}5 = -25{,}98 + 15 = \boxed{-10{,}98\ \text{MPa}}$$

### Preveritev (Mohrova krožnica)

Polmer: $R = \sqrt{30^2 + 30^2} = 42{,}43$ MPa

Rezultanta napetostnega vektorja: $p = \sqrt{\sigma_n^2 + \tau_n^2} = \sqrt{60{,}98^2 + 10{,}98^2} = \sqrt{3718 + 121} = 61{,}96$ MPa

Na Mohrovi krožnici: točka leži na krožnici s središčem (20, 0) in polmerom 42,43 MPa. ✓

> **glej:** [[Koncept - Napetostno stanje#Mohrova krožnica — grafična metoda]]

---

## Primer 4 — Ravninska deformacija: stena pod obtežbo (IMG_1241 str. 27)

### Podatki

Napetostni tenzor kamnitega zidu (tlak od lastne teže + torzija):
$$\sigma_x = -2{,}5\ \text{MPa}, \quad \sigma_y = 0, \quad \tau_{xy} = 0{,}8\ \text{MPa}$$

Material: $\tau_{dop,nateg} = 1{,}2$ MPa, $\tau_{dop,tlak} = -120$ MPa

### Glavne napetosti

$$\sigma_{sr} = \frac{-2{,}5 + 0}{2} = -1{,}25\ \text{MPa}$$

$$R = \sqrt{\left(\frac{-2{,}5-0}{2}\right)^2 + 0{,}8^2} = \sqrt{1{,}5625 + 0{,}64} = \sqrt{2{,}2025} = 1{,}484\ \text{MPa}$$

$$\sigma_1 = -1{,}25 + 1{,}484 = +0{,}234\ \text{MPa} \quad \text{(nateg!)}$$
$$\sigma_2 = -1{,}25 - 1{,}484 = -2{,}734\ \text{MPa} \quad \text{(tlak)}$$

### Preverjanje dopustnosti

$$\sigma_1 = +0{,}234\ \text{MPa} \leq \tau_{dop,nateg} = 1{,}2\ \text{MPa} \quad ✓$$
$$\sigma_2 = -2{,}734\ \text{MPa} > \tau_{dop,tlak} = -120\ \text{MPa} \quad ✓$$

**Napetostno stanje je v mejah dopustnega.**

---

## Algoritem — Napetosti na nagnjeni ravnini

```
1. Preberi σx, σy, τxy
2. Določi kot φ (kot NORMALE na ravnino od osi x)
3. σφ = (σx+σy)/2 + (σx-σy)/2·cos(2φ) + τxy·sin(2φ)
4. τφ = -(σx-σy)/2·sin(2φ) + τxy·cos(2φ)
5. Kontrola: σφ² + τφ² = rezultanta² (preveri z Mohrovo krožnico)
```

---

## Pogosta napaka

> **Napaka:** Zmeda med kotom ravnine in kotom normale.
> - Normala na ravnino (φ) in ravnina sama sta pravokotni → razlika 90°
> - V formulah nastopa $2\varphi$ (kot normale, ne ravnine)

> **Napaka:** Predznak $\tau_{xy}$ — pozoren bodi na smer strižne napetosti v tenzorju!

---

## Povzetek formul

| Iskano | Formula |
|--------|---------|
| Normalna napetost na ravnini z normalo φ | $\sigma_\varphi = \sigma_{sr} + \frac{\sigma_x-\sigma_y}{2}\cos 2\varphi + \tau_{xy}\sin 2\varphi$ |
| Strižna napetost | $\tau_\varphi = -\frac{\sigma_x-\sigma_y}{2}\sin 2\varphi + \tau_{xy}\cos 2\varphi$ |
| Glavne napetosti (max/min σ) | $\sigma_{1,2} = \sigma_{sr} \pm R$ |
| Kot do glavnih smeri | $\varphi_0 = \frac{1}{2}\arctan\frac{2\tau_{xy}}{\sigma_x-\sigma_y}$ |
| Max strižna napetost | $\tau_{max} = R$ pri $\varphi = \varphi_0 + 45°$ |

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]
- [[Naloga - Mehanika - Tenzorska analiza - aluminijast kvader]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

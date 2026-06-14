---
tags: [mehanika, napetosti, Mohr, čisto-strižno, tenzor, naloga, izpit]
predmet: Mehanika
datum: 2026-06-14
vir: Izpit iz Mehanike BTF, Lesarstvo UN, 5. jul. 2018 / 20. avg. 2025, Naloga 3
---

# Naloga: Čisto strižno stanje — Izpit Jul 2018

## Podatki

$$\sigma_{ij} = \begin{pmatrix} 0 & 50 \\ 50 & 0 \end{pmatrix}\ \text{MPa}$$

- $\sigma_x = 0\ \text{MPa}$, $\sigma_y = 0\ \text{MPa}$, $\tau_{xy} = 50\ \text{MPa}$

**Naloga:** Izračunaj glavne napetosti. Določi kote normal na ploskve z glavnimi napetostmi. Nariši Mohrovo krožnico in na njej označi dana stanja.

---

## Korak 1 — Glavne napetosti

### Zakaj posebni primer?

Ko $\sigma_x = \sigma_y = 0$, je to **čisto strižno stanje** — posebni primer, ki ima elegantno rešitev.

$$\sigma_{sr} = \frac{\sigma_x + \sigma_y}{2} = \frac{0 + 0}{2} = 0\ \text{MPa}$$

$$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \sqrt{0^2 + 50^2} = \boxed{50\ \text{MPa}}$$

$$\boxed{\sigma_1 = +50\ \text{MPa}}, \qquad \boxed{\sigma_2 = -50\ \text{MPa}}$$

> 🔍 **Lastnost:** Čisto strižno stanje → $|\sigma_1| = |\sigma_2| = \tau_{xy}$. Mohrova krožnica je centrirana v izhodišču!

> **glej:** [[Koncept - Napetostno stanje#Mohrova krožnica — grafična metoda]]

---

## Korak 2 — Koti na glavne smeri

$$\varphi_0 = \frac{1}{2}\arctan\frac{2\tau_{xy}}{\sigma_x - \sigma_y} = \frac{1}{2}\arctan\frac{2 \cdot 50}{0 - 0} = \frac{1}{2}\arctan(\infty) = \frac{1}{2} \cdot 90° = \boxed{45°}$$

**Razlaga:** Glavne napetosti delujejo pod kotom **45°** glede na os x (in y).

$$\varphi_0 = 45° \quad \Rightarrow \quad \sigma(\varphi_0) = \sigma_1 = +50\ \text{MPa}$$
$$\varphi_0 + 90° = 135° \quad \Rightarrow \quad \sigma(\varphi_0+90°) = \sigma_2 = -50\ \text{MPa}$$

> ⚠️ To je splošna lastnost: pri čistem strigu ($\sigma_x=\sigma_y=0$) so **vedno** glavne smeri pri 45°!

> **glej:** [[Koncept - Napetostno stanje#Kot do glavnih smeri]]

---

## Korak 3 — Mohrova krožnica

**Lastnosti Mohrove krožnice za čisto strižno stanje:**

- Središče: $C = (0, 0)$ — krožnica gre skozi izhodišče
- Polmer: $R = \tau_{xy} = 50\ \text{MPa}$
- Točka A = $(\sigma_x, \tau_{xy}) = (0, +50)$
- Točka B = $(\sigma_y, -\tau_{xy}) = (0, -50)$
- Preseki z $\sigma$-osjo: $\sigma_1 = +50$ MPa, $\sigma_2 = -50$ MPa
- Max strižna napetost: $\tau_{max} = R = 50$ MPa (pri $\varphi = 0°$ → izhodiščno stanje je že $\tau_{max}$!)

```
        τ↑
        |
   A(0,+50)
        |
−50 ----+---- +50    σ→
   σ₂   |    σ₁
        |
   B(0,−50)
        |
```

> 🔍 **Opomba:** Točki A in B sta na y-osi → to je značilno za čisto strižno stanje. Hkrati je to kar τmax!

---

## Korak 4 — Preveritev transformacijske enačbe

Preverimo pri $\varphi = 45°$:

$$\sigma_{45°} = 0 + 0 \cdot \cos 90° + 50 \cdot \sin 90° = 0 + 0 + 50 = \boxed{+50\ \text{MPa}} = \sigma_1 \quad ✓$$

$$\tau_{45°} = -0 \cdot \sin 90° + 50 \cdot \cos 90° = 0 + 0 = \boxed{0\ \text{MPa}} \quad ✓$$

(Na ravninah z glavnimi napetostmi je strižna napetost res 0.)

> **glej:** [[Koncept - Napetostno stanje#Transformacijske enačbe]]

---

## Posebnost: Torzija daje čisto strižno stanje

> 🔍 Torzija v točkah na robu prereza ustvari natanko čisto strižno stanje: $\sigma_x = \sigma_y = 0$, $\tau_{xy} = \tau_{max}$.
> → Posledica: na ravninah pod 45° nastopijo čisti nateg in tlak s $|\sigma_{1,2}| = \tau$.
> → Krhki materiali (liti) se lomijo pod 45° pri torziji — spiral fracture!

---

## Povzetek

| Iskano | Vrednost |
|--------|---------|
| $\sigma_1$ | $+50$ MPa |
| $\sigma_2$ | $-50$ MPa |
| $\varphi_0$ (kot normale na $\sigma_1$ ploskev) | $45°$ |
| $\tau_{max}$ | $50$ MPa (pri $\varphi = 0°$) |
| Mohrova krožnica | R=50 MPa, C=(0,0) |

---

## Povezave

- [[Koncept - Napetostno stanje]]
- [[Koncept - Torzija]]
- [[Naloga - Mehanika - Tenzorska analiza - deformacijski tenzor]]
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

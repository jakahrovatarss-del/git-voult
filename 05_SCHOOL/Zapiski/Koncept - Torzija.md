---
tags: [mehanika, torzija, strižna-napetost, zasuk, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — Torzija

## Namen

Izračunati strižne napetosti $\tau$ in zasuk $\varphi$ v palici, obremenjeni s torzijskim momentom $M_t$ (vijačenjem). Velja za krožne (polne in votlé) prereze.

---

![[torzija_palica.svg]]

## Osnovna enačba torzije

$$\boxed{\tau = \frac{M_t}{W_t}}$$

kjer je $W_t$ **torzijski odpornostni moment**.

Splošna porazdelitev po prerezu:

$$\tau(r) = \frac{M_t \cdot r}{I_p}$$

- $r$ = razdalja od osi palice
- $I_p$ = polarni vztrajnostni moment

> 🔍 **Fizikalni pomen:** Strižna napetost linearno narašča od osi (τ=0) do roba prereza (τ=max). Analogno z upogibom!

---

## Formule za prereze

### Polni krog (premer $d$)

$$I_p = \frac{\pi d^4}{32} \qquad W_t = \frac{\pi d^3}{16} \qquad e = \frac{d}{2}$$

> 💡 **Trik:** $W_t = \frac{\pi d^3}{16} = 2 \cdot \frac{\pi d^3}{32} = 2W$ — torzijski odpornostni moment je **dvakrat upogibni** za polni krog!

$$\tau_{max} = \frac{M_t}{W_t} = \frac{M_t \cdot 16}{\pi d^3} = \frac{M_t \cdot d/2}{I_p}$$

### Votli krog (zunanji $D$, notranji $d$)

$$I_p = \frac{\pi(D^4 - d^4)}{32} \qquad W_t = \frac{\pi(D^4 - d^4)}{16D}$$

### Primerjava s polnim:

| Prerez | $I_p$ | $W_t$ | $\tau_{max}$ |
|--------|--------|--------|--------------|
| Polni d | $\pi d^4/32$ | $\pi d^3/16$ | $16M_t/\pi d^3$ |
| Votli D,d | $\pi(D^4-d^4)/32$ | $\pi(D^4-d^4)/16D$ | $16M_t D/\pi(D^4-d^4)$ |

> ⚠️ $W_t = I_p / r_{max}$ — analogno z upogibom ($W_x = I_x / e$)!

---

## Zasuk palice (kot zasuka)

$$\boxed{\varphi = \frac{M_t \cdot L}{G \cdot I_p}}$$

- $\varphi$ [rad] = zasuk prostega konca glede na vpetje
- $G$ = strižni modul (za jeklo: $G \approx 80$ GPa $= 8 \cdot 10^4$ kN/cm²)
- $L$ = dolžina palice
- $I_p$ = polarni vztrajnostni moment

> 🔍 Zveza: $G = E / (2(1+\nu))$. Za jeklo: $E = 210$ GPa, $\nu = 0{,}3$ → $G \approx 80{,}8$ GPa.

---

## Dimenzioniranje palice na torzijo

**Pogoj:** $\tau_{max} \leq \tau_{dop}$

$$\frac{M_t}{W_t} \leq \tau_{dop} \quad \Rightarrow \quad W_t \geq \frac{M_t}{\tau_{dop}}$$

Za **polno palico:**
$$\frac{\pi d^3}{16} \geq \frac{M_t}{\tau_{dop}} \quad \Rightarrow \quad d \geq \sqrt[3]{\frac{16 M_t}{\pi \tau_{dop}}}$$

---

## Algoritem

```
1. Določi torzijski moment M_t (pozor: M_t ≠ upogibni moment M!)
2. Izračunaj W_t za dani prerez (po formulah zgoraj)
3. τ_max = M_t / W_t
4. Preveri pogoj: τ_max ≤ τ_dop
5. Zasuk: φ = M_t · L / (G · I_p)
```

> **Enote:** $M_t$ [kNm ali Ncm], $W_t$ [cm³], $\tau$ [kN/cm² ali MPa]

---

## Primer — Polna jeklena gred

**Podatki:** $M_t = 500$ Nm, $d = 4$ cm, $G = 80$ GPa $= 8000$ kN/cm², $L = 1{,}5$ m

**Korak 1:** $M_t = 500$ Nm $= 50$ kNcm

**Korak 2:**
$$W_t = \frac{\pi \cdot 4^3}{16} = \frac{64\pi}{16} = 4\pi = 12{,}57\ \text{cm}^3$$
$$I_p = \frac{\pi \cdot 4^4}{32} = \frac{256\pi}{32} = 8\pi = 25{,}13\ \text{cm}^4$$

**Korak 3:**
$$\tau_{max} = \frac{50}{12{,}57} = 3{,}98\ \text{kN/cm}^2 = 39{,}8\ \text{MPa}$$

**Korak 5 — zasuk:**
$$\varphi = \frac{50\ \text{kNcm} \cdot 150\ \text{cm}}{8000\ \text{kN/cm}^2 \cdot 25{,}13\ \text{cm}^4} = \frac{7500}{201040} = 0{,}0373\ \text{rad} = 2{,}14°$$

> **glej:** [[Koncept - Napetostno stanje]]

---

## Bredt-Bathoova formula (tanke votline)

Za tankostenske zaprte prereze (škatlasti profil, cevi):

$$\tau = \frac{M_t}{2 \cdot A_m \cdot t}$$

- $A_m$ = ploščina, ki jo obkroži srednja linija prereza
- $t$ = debelina stene

> Za pravokotno cev $B \times H$ z debelino $t$:
> $A_m = (B-t)(H-t) \approx B \cdot H$ (za majhen $t$)

---

## Napetostno stanje pri torziji

Torzija povzroča **čisto strižno** napetostno stanje:

$$\sigma_{ij} = \begin{pmatrix} 0 & \tau \\ \tau & 0 \end{pmatrix}$$

Iz tega: $\sigma_1 = +\tau$, $\sigma_2 = -\tau$, pod kotom 45° od osi.

> 🔍 Torzija: vlakna v nategu pod 45° in v tlaku pod −45° → zato jeklene gredi razpokajo pod 45° pri prekoračitvi!

> **glej:** [[Koncept - Napetostno stanje#Posebni primeri]]

---

## Kombinirano: upogib + torzija

Ko delujeta hkrati:

$$\sigma = \frac{M}{W_x}, \qquad \tau = \frac{M_t}{W_t}$$

**Dimenzioniranje po Von Mises:**

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop}$$

**Dimenzioniranje po Tresca:**

$$\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} \leq \sigma_{dop}$$

> 💡 **Trik "Tresca 4, VM 3"** — edina razlika je faktor pred $\tau^2$!

> **Rešen primer z obema:** [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 3 — Kombinirano: upogib + torzija → ekvivalentne napetosti]]

**Ekvivalentni moment (za krožne prereze):**

$$M_{ekv} = \sqrt{M^2 + 0{,}75 \cdot M_t^2} \quad \text{(iz Von Mises)}$$

ali s faktorjem $\alpha$ (odvisno od napetostnega kriterija):

$$M_{ekv} = \frac{1}{2}\left(M + \sqrt{M^2 + M_t^2}\right) \quad \text{(Tresca)}$$

---

## Pogosta napaka

> **Napaka:** Zamenjava $M$ (upogibni) z $M_t$ (torzijski). Na shemi: upogibni $M$ je v ravnini obtežbe, torzijski $M_t$ je **vzdolž osi** palice!

> **Napaka:** Enota $G$ — za jeklo $G = 80$ GPa $= 80\ 000$ MPa $= 8 \cdot 10^4$ kN/cm²

---

## Rešene naloge

- Primer iz izpita Statike 1 (7.1.2001): $G = 750$ N, $R = 5$ cm, $L = 40$ cm
- [[Naloga - Mehanika - Izpit Feb2019 - Torzija Bredt skatlast]] — škatlast prerez 10×15 cm, $M_t = F \cdot a$, Bredt formula

---

## Povezave

- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← kombinirano M+Mt, čist strig
- [[Koncept - Napetostno stanje]]

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Izpit Feb2019 - Torzija Bredt skatlast]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

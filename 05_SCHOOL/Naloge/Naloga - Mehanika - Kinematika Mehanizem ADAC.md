---
tags: [mehanika, kinematika, mehanizem, pol-hitrosti, relativna-hitrost, izpit]
predmet: Mehanika
datum: 2026-06-18
vir: "Izpit 17. 4. 2015 — naloga 2"
status: rešeno
---

# Naloga — Kinematika mehanizma AD–AC–EB (Izpit 17. 4. 2015)

## Namen

Za dano lego štiričlenskega mehanizma (vrtljiva gred AD, palica AC z vmesnim členkom B, odvodna palica EB) določi hitrost točke C in kotno hitrost palice AC.

---

## Dano

![[kinematika_mehanizem_adac.svg|697]]

| Oznaka | Vrednost |
|--------|---------|
| Dolžina AD (gred) | 2 m |
| Dolžina AB (del palice) | 3 m |
| Dolžina BC (del palice) | 1 m → skupaj AC = 4 m |
| Kotna hitrost gredi AD | $\omega = 2\pi\ \text{rad/s}$ (protiurna) |
| Lega | AD **navpično**, AC **vodoravno** |
| Palica EB | oklepa s podlago **60°** |
| D, E | nepremični členki (NI — nepremično ležišče) |

**Koordinatni sistem** (D = izhodišče):

| Točka | Koordinate |
|-------|-----------|
| D | (0, 0) — fiksna os vrtenja |
| A | (0, 2) — vrh gredi AD |
| B | (3, 2) — vmesni členek na AC |
| C | (4, 2) — konec palice AC |
| E | fiksna os palice EB |

**Iskano:** $\omega_{AC}$, $v_C$

---

## KORAK 1 — Hitrost točke A

A se vrti okrog fiksnega D z $\omega = 2\pi\ \text{rad/s}$. AD je navpično → $v_A$ je vodoravna:

$$v_A = \omega \cdot AD = 2\pi \cdot 2 = 4\pi\ \text{m/s} \quad \text{(vodoravno desno)}$$

$$\vec{v}_A = (4\pi,\ 0)\ \text{m/s}$$

---

## KORAK 2 — Pogoj iz palice EB

E je fiksna os → B se mora gibati **pravokotno na EB**.

EB oklepa s podlago 60° → smer EB: $(\cos 60°, \sin 60°) = (\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})$

Smer $v_B$ (pravokotno na EB): $(\tfrac{\sqrt{3}}{2}, -\tfrac{1}{2})$ ← ker $v_{Bx} > 0$

$$\frac{v_{Bx}}{v_{By}} = -\sqrt{3}$$

---

## KORAK 3 — Kotna hitrost $\omega_{AC}$

Hitrost B iz palice AC (AC je vodoravna, $r_{AB} = (3, 0)$):

$$\vec{v}_B = \vec{v}_A + \omega_{AC}\,\hat{k} \times \vec{r}_{AB} = (4\pi,\ 0) + \omega_{AC}\,\hat{k} \times 3\hat{\imath}$$

$$\hat{k} \times 3\hat{\imath} = 3\hat{\jmath} \quad \Rightarrow \quad \vec{v}_B = (4\pi,\ 3\omega_{AC})$$

Vstavimo pogoj $v_{Bx}/v_{By} = -\sqrt{3}$:

$$\frac{4\pi}{3\omega_{AC}} = -\sqrt{3} \quad \Rightarrow \quad \omega_{AC} = -\frac{4\pi}{3\sqrt{3}} = -\frac{4\pi\sqrt{3}}{9}\ \text{rad/s}$$

$$\boxed{\omega_{AC} = \frac{4\pi\sqrt{3}}{9} \approx 2{,}42\ \text{rad/s} \quad \text{(urna smer — ↻)}}$$

> 💡 Negativni predznak = urna smer (CW), ker smo definirali CCW kot pozitivno.

---

## KORAK 4 — Hitrost točke C

$$\vec{v}_C = \vec{v}_A + \omega_{AC}\,\hat{k} \times \vec{r}_{AC} = (4\pi,\ 0) + \omega_{AC} \cdot 4\hat{\jmath}$$

$$v_{Cx} = 4\pi \approx 12{,}57\ \text{m/s}$$

$$v_{Cy} = 4\omega_{AC} = 4 \cdot \left(-\frac{4\pi\sqrt{3}}{9}\right) = -\frac{16\pi\sqrt{3}}{9} \approx -9{,}67\ \text{m/s}$$

$$|v_C| = \sqrt{v_{Cx}^2 + v_{Cy}^2} = \pi\sqrt{16 + \frac{768}{81}} = \frac{\pi}{9}\sqrt{2064} = \frac{4\pi\sqrt{129}}{9}$$

$$\boxed{v_C = \frac{4\pi\sqrt{129}}{9} \approx 15{,}86\ \text{m/s} \quad \text{pod kotom } -37{,}6° \text{ od vodoravnice}}$$

---

## KORAK 5 — Preveritev z metodo pola hitrosti

Pol hitrosti P palice AC leži na:
- **navpičnici** skozi A (ker $v_A$ je vodoravna → $\perp v_A$ je navpična) → $P_x = 0$
- **pravokotnici** na $v_B$ skozi B: linija pod 60° skozi $(3, 2)$

Enačba pravokotnice na $v_B$ skozi B (nagib = $\tan 60° = \sqrt{3}$):

$$y - 2 = \sqrt{3}(x - 3) \quad \text{pri } x=0: \quad y = 2 - 3\sqrt{3}$$

$$P = \left(0,\ 2 - 3\sqrt{3}\right) \approx (0,\ {-3{,}20})$$

**Razdalje od P:**

$$PA = 3\sqrt{3} \approx 5{,}20\ \text{m}, \qquad PC = \sqrt{4^2 + (3\sqrt{3})^2} = \sqrt{16+27} = \sqrt{43} \approx 6{,}56\ \text{m}$$

**Preveritev $\omega_{AC}$:**

$$\omega_{AC} = \frac{v_A}{PA} = \frac{4\pi}{3\sqrt{3}} = \frac{4\pi\sqrt{3}}{9} \approx 2{,}42\ \text{rad/s} \quad \checkmark$$

**Preveritev $v_C$:**

$$v_C = \omega_{AC} \cdot PC = \frac{4\pi\sqrt{3}}{9} \cdot \sqrt{43} = \frac{4\pi\sqrt{129}}{9} \approx 15{,}86\ \text{m/s} \quad \checkmark$$

---

## Povzetek

| Veličina | Exakten izraz | Numerično |
|----------|--------------|-----------|
| $v_A$ | $4\pi$ m/s | ≈ 12,57 m/s |
| $\omega_{AC}$ | $4\pi\sqrt{3}/9$ rad/s (↻) | ≈ **2,42 rad/s** |
| $v_{Cx}$ | $4\pi$ m/s | ≈ 12,57 m/s |
| $v_{Cy}$ | $-16\pi\sqrt{3}/9$ m/s | ≈ −9,67 m/s |
| $v_C$ | $4\pi\sqrt{129}/9$ m/s | ≈ **15,86 m/s** |
| Kot $v_C$ | $\arctan(-16\sqrt{3}/36)$ | ≈ −37,6° |
| Pol P | $(0,\ 2-3\sqrt{3})$ m | ≈ $(0,\ {-3,20})$ |

**Pogoste napake:**
- ⚠️ Smer $v_A$: ⊥ na AD (navpično) → $v_A$ je **vodoravna**, ne navpična
- ⚠️ Pogoj EB: $v_B$ je ⊥ na EB (ne vzdolž EB!)
- ⚠️ Predznak $v_{By}$: ker $v_{Bx} > 0$ in razmerje $= -\sqrt{3}$, je $v_{By} < 0$
- ⚠️ $\omega_{AC} < 0$ → urna smer (CW), ne protiurna

---

## Flashcards

Q: Kako določiš smer hitrosti točke, ki se vrti okrog fiksne osi?
A: v ⊥ polmer od osi do točke. Velikost: v = ω·r.

Q: Kakšen je pogoj za hitrost točke na palici z enim fiksnim koncem?
A: Hitrost te točke mora biti ⊥ na palico (togo telo).

Q: Kako iz pola hitrosti P izračunaš hitrost točke C?
A: vC = ωAC · |PC|, smer: ⊥ na linijo P→C.

Q: Kje leži pol hitrosti palice AC v tej nalogi?
A: Na presečišču: navpičnice skozi A (ker vA je vodoravna) IN pravokotnice na vB skozi B. P = (0, 2−3√3) ≈ 3,20 m pod D.

---

## Povezave

- [[Blok 6 - Kinematika]] — relativna hitrost, pol hitrosti
- [[Koncept - Kinematika Mehanizmi]] — metoda pola hitrosti
- [[Cheat Sheet - Mehanika FORMULE]] — Blok 6: vB = vA + ω×rAB
- [[Cheat Sheet - Mehanika Celotna]] — TIP K Kinematika
- [[Poglavje - Kinematika in Dinamika]] — sorodni primeri

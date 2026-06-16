---
tags: [mehanika, uklon, euler, stabilnost, vitkost, omega, Tetmajer, koncept]
predmet: Mehanika
datum: 2026-06-11
---

# Koncept: Euler Uklon (Uklonska stabilnost)

## Namen

Uklon (buckling) nastopi, ko tlačno obremenjena **vitka palica** izgubi stabilnost in se bočno ukloni — brez da bi material prekoračil dopustno napetost. Nevarnost je, da se palica poruši pri napetostih, ki so daleč pod mejo tečenja.

> **Razlika od upogiba:** pri upogibu gre za napetosti v prerezu; pri uklonu gre za **izgubo ravnotežja celotne palice** — forma odpove, ne material.

---

## Korak 1 — Določitev statičnega sistema (vpetje)

Preden kar koli izračunamo, moramo vedeti **kako je palica vpeta** — to določi uklonsko dolžino.

### 4 Eulerovi primeri (uklonski primeri)

| Primer | Vpetje | $\beta$ | $l_u = \beta L$ | Opis |
|--------|--------|---------|-----------------|------|
| 1 | obe strani členkasto | **1,0** | $L$ | prostoležeča palica |
| 2 | spodaj vpeta, zgoraj členkasta | **0,7** | $0{,}7L$ | |
| 3 | obe strani vpeti | **0,5** | $0{,}5L$ | dvojno vpetje — najtrše |
| 4 | spodaj vpeta, zgoraj **prosta** (konzola) | **2,0** | $2L$ | konzola — najnevarnejše |

> **Pravilo za spomin:** konzola (primer 4) je dvakrat daljša od enako dolge prostoležeče (primer 1) — zato $\beta = 2$.

$$\boxed{l_u = \beta \cdot L}$$

---

## Korak 2 — Izračun minimalnega vztrajnostnega momenta

Uklon nastopi vedno okoli **šibke osi** (osi z **najmanjšim** $I$).

Za pravokoten prerez $b \times h$ (kjer $b < h$):

$$I_{min} = \frac{h \cdot b^3}{12} \qquad \text{(šibka os = manjša dimenzija kubično)}$$

> ⚠️ **Paziti na os!** Uklon nastopi v smeri najmanjše togosti. Če ima prerez $b=2{,}5$ cm in $h=20$ cm, je $I_{min}$ glede na os skozi 20 cm dimenzijo.

Za sestavljene prereze (I, T, U):
$$I_{min} = \min(I_y, I_z)$$

→ Podrobno v [[Koncept - Vztrajnostni moment]]

---

## Korak 3 — Preveri ali velja Euler (vitkost)

Eulerjeva formula velja **samo za vitke palice** ($\lambda > \lambda_e$). Za kratke/debelostenske palice (porušitev po materialu) se uporablja Tetmajer ali ω metoda.

### Korak 3a — Vztrajnostni polmer

$$i = \sqrt{\frac{I_{min}}{A}}$$

### Korak 3b — Vitkost

$$\lambda = \frac{l_u}{i}$$

### Korak 3c — Meja Eulerja $\lambda_e$

$$\lambda_e = \pi \sqrt{\frac{E}{\sigma_{dop}}}$$

| Material | E [kN/cm²] | $\sigma_{dop}$ [kN/cm²] | $\lambda_e$ |
|----------|-----------|------------------------|-------------|
| Les (iglavci) | 1000 | 1,0 | $\approx 100$ |
| Jeklo (S235) | 21000 | 16 | $\approx 114$ |

**Odločitev:**
- $\lambda > \lambda_e$ → Eulerjeva formula ✓
- $\lambda \leq \lambda_e$ → Tetmajer ali ω postopek

---

## Korak 4 — Eulerjeva kritična sila

$$\boxed{F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2}}$$

| Simbol | Pomen | Enota |
|--------|-------|-------|
| $E$ | modul elastičnosti | kN/cm² |
| $I_{min}$ | minimalni vztrajnostni moment | cm⁴ |
| $l_u$ | uklonska dolžina ($= \beta L$) | cm |

> **Enote:** $l_u$ mora biti v **cm** ko je $E$ v kN/cm² in $I$ v cm⁴ → $F_k$ dobimo v **kN**.

---

## Korak 5 — Dopustna sila in varnost

### Metoda 1: Euler (neposredno)

$$F_{dop} = \frac{F_k}{\nu}$$

Varnostni faktor $\nu$: za les tipično $\nu = 3$, za jeklo $\nu = 2{,}5$–$3$.

### Metoda 2: ω postopek (natančnejši, upošteva nepopolnosti)

$$\boxed{F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega(\lambda)}}$$

$\omega$ se odčita iz **ω tabel** (odvisno od materiala in $\lambda$):

| $\lambda$ | $\omega$ (les, iglavci) |
|-----------|------------------------|
| 60 | 1,42 |
| 80 | 1,76 |
| 100 | 2,44 |
| 115 | 3,43 |
| 120 | 4,007 |
| 150 | 6,28 |

> **Razlika Euler vs. ω:** Pri nizkih $\lambda$ je ω konzervativnejši (upošteva nepopolnosti). Pri visokih $\lambda$ ($> 120$) sta praktično enaka. Za naloge na izpitu je bolj pogosta Euler metoda, razen ko je $\lambda < \lambda_e$.

---

## Korak 6 — Ravnotežje (ko sila ni vzdolž palice)

Ko naloga vključuje okvir ali triangulacijo, palica tipično ni obremenjena neposredno — najprej izračunamo **notranjo silo N** iz ravnotežja.

**Primer — diagonalna palica (45°), vodoravna sila S:**

$$\sum F_x = 0: \quad N_1 \cdot \frac{1}{\sqrt{2}} = S \quad \Rightarrow \quad N_1 = S\sqrt{2}$$

$$\text{Pogoj: } N_1 \leq F_{dop} \quad \Rightarrow \quad S_{dop} = \frac{F_{dop}}{\sqrt{2}}$$

**Primer — trikotni okvir, navpična sila F na osi:**

$$\sum M_A = 0 \quad \Rightarrow \quad N_{palice} = 3F \quad \text{(iz ravnotežja)}$$

---

## Primerjava metod

| | Euler | ω postopek |
|--|-------|------------|
| Kdaj | $\lambda > \lambda_e$ | vedno (bolj splošen) |
| Izhod | $F_k$, potem $F_{dop} = F_k/\nu$ | $F_{dop}$ direktno iz tabele |
| Upošteva nepopolnosti | ne | da |
| Konzervativnost | srednje | višja pri nizkem $\lambda$ |

---

## Vizualni prikaz — 4 Eulerovi primeri

![[uklon_lesena_deska.svg|585]]

---

## Dopustne napetosti in moduli

| Material | E [kN/cm²] | $\sigma_{dop,tlak}$ [kN/cm²] | $\sigma_{dop,upogib}$ [kN/cm²] |
|----------|-----------|------------------------------|-------------------------------|
| Les (iglavci) | 1000 | ~0,8 | ~1,0 |
| Jeklo (S235) | 21000 | 16 | 16 |

---

## Primeri nalog

- [[Naloga - Mehanika - Uklon lesene deske]] — konzola ($\beta=2$), $2{,}5\times 20$ cm, $L=3{,}5$ m → $F_k = 0{,}524$ kN
- [[Naloga - Mehanika - Uklon leseni steber F_max]] — T-rama, členk. ($\beta=1$), $12\times 12$ cm, $L=4$ m → $F_{max} = 11{,}84$ kN
- [[Naloga - Mehanika - Uklon palica S_dop]] — jeklo, I-profil, triangularna konstr., $\beta=1$ → $S_{dop} = 23{,}4$ kN

## Povezave

- [[Koncept - Vztrajnostni moment]] — izračun $I_{min}$, šibka os, Steiner
- [[Koncept - Upogib]] — paralelna tema: upogib vs. uklon
- [[Izpit - Mehanika - Upogib]] — pregled vseh tipov nalog
- [[Mehanika Hub]]
- [[STATIKA]]
- [[Mehanika Hub]]

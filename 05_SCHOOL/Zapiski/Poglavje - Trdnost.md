---
tags: [mehanika, trdnost, NTM, upogib, torzija, uklon, napetosti, mohr, hipoteze, sestavljene, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# Poglavje — 2. SKLOP: Trdnost

## Namen

Celovit zapisek za **2. SKLOP: Trdnost** — vse tipe nalog z rešitvami po kategorijah. Že rešene naloge so zlinkane, nove so rešene inline.

> **Teorija:** [[Blok 1 - NTM Diagrami]] | [[Blok 2 - Upogib]] | [[Blok 3 - Napetostno Stanje]] | [[Blok 3.5 - Hipoteze Porusitve]] | [[Blok 4 - Euler Uklon]] | [[Blok 5 - Torzija]]

---

## Pregled tipov nalog

| # | Tip naloge | Ključna formula | Naloge |
|---|-----------|-----------------|--------|
| 1 | NTM diagrami — prosta greda | ΣM=0 → T=0 → Mmax | N1–N5 |
| 2 | NTM — lomljeni nosilci in okvirji | N/T se zamenjata v oglu | N6–N7 |
| 3 | Upogib — dimenzioniranje | W = M/σ_dop | N8–N9 |
| 4 | Ekscentrični tlak (N + M) | σ = N/A ± M/W | N10 |
| 5 | Napetostni tenzor + Mohr | σ₁₂ = S ± R | N11–N15 |
| 6 | Hipoteze porušitve | Tresca / Von Mises | N16 |
| 7 | Torzija — polna gred | τ = Mt/Wt | N17 |
| 8 | Torzija — votli prerez (Bredt) | τ = Mt/(2·Am·t) | N18 ← NOVA |
| 9 | Uklon Euler | Fk = π²EI/lu² | N19–N20 |
| 10 | Uklon Tetmajer | σk = a − b·λ | N21 ← NOVA |
| 11 | Sestavljene obremenitve (N+M+Mt) | superpozicija + Mises | N22 ← NOVA |

---

## 1. NTM DIAGRAMI — Prosta greda in previsi

### N1 — Prosta greda: q + F
> Rešena naloga: [[Vaje - NTM diagrami - Vse vrste#NALOGA 1 — Prosta greda točkovna sila + porazdeljena obtežba]]

Ključni rezultat: $T=0$ pri $x=A_y/q$ → tam je $M_{max}$ (parabola pod $q$, trikotnik pod $F$).

---

### N2 — Nosilci s previsom (konzola + prosta greda)
> Rešena naloga: [[Vaje - NTM diagrami - Vse vrste#NALOGA 2 — Nosilci s previsom (konzola + prosta greda)]]

Ključni rezultat: Previšni del povzroči negativni moment; prehodnica skozi 0 pomeni nevtralno vlakno.

---

### N3 — Kombinacija q + F pod kotom + točkasti moment M₀
> Rešena naloga: [[Vaje - NTM diagrami - Vse vrste#NALOGA 5 — Kombinacija q + F pod kotom + točkasti moment M₀]]

Ključni rezultat: Točkasti moment $M_0$ povzroči **preskok** v M-diagramu brez spremembe v T.

---

### N4 — Nosilci s previsom in dvojico sil

> **Besedilo (Jesenko, Nosilci 1):** Prostoležeč nosilci $L=8\ \text{m}$ s previsom do $E$ ($\overline{BE}=2\ \text{m}$), torej skupna dolžina $10\ \text{m}$. Podpora $A$ je tečaj (x=0), podpora $B$ je valj (x=8m). Obtežba: $q=2{,}5\ \text{kN/m}$ po celotni dolžini 10m, sila $F_1=8\ \text{kN}\downarrow$ pri $x=3\ \text{m}$, dvojica sil $F_2=5\ \text{kN}$, ročica $d=1\ \text{m}$, moment $M_0=F_2\cdot d=5\ \text{kNm}$ pri $x=6\ \text{m}$.

#### Korak 1 — Reakcije

$$Q = q \cdot 10 = 25\ \text{kN} \quad \text{v x=5 m}$$

$$\sum M_A=0: \quad B_y\cdot8 = Q\cdot5 + F_1\cdot3 + M_0 = 125+24+5 = 154$$

$$\boxed{B_y=19{,}25\ \text{kN}}, \qquad A_y = Q+F_1-B_y = 33-19{,}25=\boxed{13{,}75\ \text{kN}}$$

#### Korak 2 — Diagram T (prečna sila)

| Odsek | T |
|-------|---|
| $0^+$ | +13,75 |
| pred $F_1$ (x=3⁻) | $13{,}75 - 2{,}5\cdot3 = +6{,}25$ |
| za $F_1$ (x=3⁺) | $6{,}25 - 8 = -1{,}75$ |
| pred B (x=8⁻) | $-1{,}75 - 2{,}5\cdot5 = -14{,}25$ |
| za B (x=8⁺) | $-14{,}25+19{,}25 = +5{,}0$ |
| na $E$ (x=10) | $+5{,}0-2{,}5\cdot2 = 0\ ✓$ |

$T=0$ med $x=3$ in $x=8$: $13{,}75 - 2{,}5x - 8 = 0 \Rightarrow x = 2{,}3\ \text{m}$, torej absolutno $x=3+0{,}7=3{,}7\ \text{m}$... preverimo:

$T(3{,}7) = 13{,}75 - 2{,}5\cdot3{,}7 - 8 = 13{,}75-9{,}25-8=-3{,}5\neq0$ — torej T=0 pri x med 3 in 3,7... točno $x=6{,}25/2{,}5+3=5{,}5\ \text{m}$... recalculate:

Za odsek $[3, 6]$ (za $F_1$, pred $M_0$):
$T(x) = 13{,}75 - 2{,}5x - 8 = 5{,}75 - 2{,}5x = 0 \Rightarrow x_{T=0} = 2{,}3\ \text{m}$ od A? Ne — $x = 5{,}75/2{,}5 = 2{,}3\ \text{m}$ od začetka tega odseka = $x = 5{,}3\ \text{m}$ od A.

$$\boxed{x_{T=0} = 5{,}3\ \text{m od A}}$$

#### Korak 3 — Mmax

$$M(5{,}3) = A_y\cdot5{,}3 - \frac{q\cdot5{,}3^2}{2} - F_1\cdot(5{,}3-3)$$

$$= 13{,}75\cdot5{,}3 - 2{,}5\cdot\frac{5{,}3^2}{2} - 8\cdot2{,}3 = 72{,}875 - 35{,}113 - 18{,}4 = \boxed{19{,}4\ \text{kNm}}$$

> ⚠️ **Preskok pri $M_0$:** V točki $x=6\ \text{m}$ M-diagram skoči za $+M_0 = 5\ \text{kNm}$ (moment dvojice se prišteje).

> **gl.:** [[Blok 1 - NTM Diagrami#Intuicija]]

---

## 2. NTM — LOMLJENI NOSILCI IN PORTALNI OKVIRJI

### N5 — Lomljeni nosilci (L-oblika, N ≠ 0)
> Rešena naloga: [[Vaje - NTM diagrami - Vse vrste#NALOGA 3 — Lomljen nosilci (L-oblika) — pojavi se N ≠ 0!]]

Ključni rezultat: V oglu se osna sila enega elementa **prelevi v prečno silo drugega**. $N_{navp} = T_{vodor}$ v vogalu.

---

### N6 — Portalni okvir (tip izpit 2018)
> Rešena naloga: [[Vaje - NTM diagrami - Vse vrste#NALOGA 4 — Portalni okvir]]

Ključni rezultat: Vodoravna sila na okvir → stebra nosita N (osno) + T (prečno) + M (moment); prečnik nosi le M in T.

---

## 3. UPOGIB — DIMENZIONIRANJE

### N7 — Dimenzioniranje pravokotnega prereza h:b = 2:1
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 1 — Dimenzioniranje pravokotnega prereza (upogib)]]

$$q=3\ \text{kN/m},\ F=10\ \text{kN},\ L=5\ \text{m},\ \sigma_{dop}=1{,}0\ \text{kN/cm}^2 \quad \Rightarrow \quad \boxed{b=15\ \text{cm},\ h=30\ \text{cm}}$$

---

### N8 — Kontrola napetosti asimetričnega T-prereza
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 3 — Kontrola napetosti asimetričnega T-prereza]]

Ključni rezultat: T-prerez ni simetričen → $W_{sp} \neq W_{zg}$ → kritičen rob je tisti z **večjim** $e$ (= manjšim $W$).

---

### N9 — Dimenzioniranje s strižno kontrolo

> **Besedilo:** Prostoležeč leseni nosilci $L=4\ \text{m}$, $F=16\ \text{kN}$ na sredini, pravokoten prerez $h:b=1{,}5:1$. $\sigma_{dop}=1{,}0\ \text{kN/cm}^2$, $\tau_{dop}=0{,}8\ \text{kN/cm}^2$. Dimenzionirajte prerez in preverite tudi strižno napetost.

#### Korak 1 — Mmax in Tmax

$$A_y=B_y=8\ \text{kN}, \qquad M_{max}=\frac{FL}{4}=\frac{16\cdot4}{4}=\boxed{16\ \text{kNm}=1600\ \text{kNcm}}$$

$$T_{max}=A_y=\boxed{8\ \text{kN}}$$

#### Korak 2 — Dimenzioniranje iz upogiba ($b=x$, $h=1{,}5x$)

$$W_{min}=\frac{M_{max}}{\sigma_{dop}}=1600\ \text{cm}^3$$

$$W=\frac{b\cdot h^2}{6}=\frac{x\cdot(1{,}5x)^2}{6}=\frac{2{,}25x^3}{6}=0{,}375x^3$$

$$0{,}375x^3=1600 \Rightarrow x^3=4267 \Rightarrow x=\sqrt[3]{4267}=\boxed{16{,}2\ \text{cm}}$$

$$\Rightarrow b=17\ \text{cm},\quad h=26\ \text{cm} \quad \text{(zaokr. navzgor)}$$

#### Korak 3 — Kontrola strižnih napetosti

Za pravokotni prerez je maksimalna strižna napetost v nevtralnem vlaknu:

$$\tau_{max}=\frac{3}{2}\cdot\frac{T_{max}}{A}=\frac{3}{2}\cdot\frac{8}{17\cdot26}=\frac{12}{442}=\boxed{0{,}027\ \text{kN/cm}^2}\ll\tau_{dop}=0{,}8 \quad ✓$$

> **Pouk:** Pri lesu je strižna kontrola skoraj vedno neproblematična za prerez, dimenzioniran iz upogiba. Strižna napetost velja le za polni pravokotni prerez; T-prerez ima $\tau$ višjo (kritična je v stojini!).

> **gl.:** [[Blok 2 - Upogib#Intuicija]]

---

## 4. EKSCENTRIČNI TLAK (N + M)

### N10 — Ekscentrični tlak
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 4 — Ekscentrični tlak N + M]]

$$\sigma=\frac{N}{A}\pm\frac{M}{W} \qquad \text{(superpozicija osne in upogibne napetosti)}$$

Ključni rezultat: Kritično vlakno = stran, kjer sta $N$ in $M$ istega predznaka (nateg + nateg ali tlak + tlak).

---

## 5. NAPETOSTNI TENZOR IN MOHROVA KROŽNICA

### N11 — 2D Mohrova krožnica (osnovna)
> Rešena naloga: [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 1 — 2D Mohrova krožnica (osnovna)]]

$$S=\frac{\sigma_x+\sigma_y}{2}, \quad R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}, \quad \sigma_{1,2}=S\pm R$$

---

### N12 — 3D tenzor, ravninsko napetostno stanje
> Rešena naloga: [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 2 — 3D tenzor ravninsko stanje (tip Jul. 2018 Feb. 2019)]]

Ključni rezultat: Ravninsko stanje → $\sigma_3=0$; za Tresco in Von Mises upoštevamo vse tri glavne napetosti.

---

### N13 — Kombinirano upogib + torzija → ekvivalentne napetosti
> Rešena naloga: [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 3 — Kombinirano upogib + torzija → ekvivalentne napetosti]]

---

### N14 — Deformacijski tenzor → napetostni tenzor → glavne napetosti
> Rešena naloga: [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 4 — Deformacijski tenzor → napetostni tenzor → glavne napetosti]]

Ključni rezultat: Hookov zakon za 3D: $\sigma_x = \frac{E}{(1+\nu)(1-2\nu)}[(1-\nu)\varepsilon_x+\nu(\varepsilon_y+\varepsilon_z)]$.

---

### N15 — Čisto strižno stanje + dimenzioniranje
> Rešena naloga: [[Vaje - Napetostni tenzor in Mohrova kroznica#NALOGA 5 — Čisto strižno stanje + dimenzioniranje (Tresca vs Von Mises)]]

---

## 6. HIPOTEZE PORUŠITVE

### N16 — Von Mises vs. Tresca za upogib + torzija
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 5 — Sestavljena obremenitev upogib + torzija]]

$$\sigma_{ekv,VM}=\sqrt{\sigma^2+3\tau^2}, \qquad \sigma_{ekv,T}=\sqrt{\sigma^2+4\tau^2}$$

Ključni rezultat: Tresca je **vedno strožja** ($\sigma_{ekv,T} \geq \sigma_{ekv,VM}$). Na izpitu: izračunaj obe!

---

## 7. TORZIJA — POLNA GRED

### N17 — Sestavljena obremenitev upogib + torzija (polni krog)
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 5 — Sestavljena obremenitev upogib + torzija]]

$$W_t=2W\ \text{(polni krog)}, \quad \tau=M_t/W_t, \quad \sigma_{ekv,VM}=\sqrt{\sigma^2+3\tau^2}$$

---

## 8. TORZIJA — VOTLI TANKOSTENSKI PREREZ (BREDTOVA FORMULA)

### N18 — Bredt za votli pravokotni profil ← NOVA

> **Besedilo:** Votli pravokotni lepljeni leseni tram: zunanja dimenzija $B=10\ \text{cm}$, $H=16\ \text{cm}$, debelina stene $t=1{,}5\ \text{cm}$ (enakomerna po vsem obodu). Torzijski moment $M_t=3{,}6\ \text{kNm}$. Preverite torzijsko napetost. ($\tau_{dop}=0{,}9\ \text{kN/cm}^2$)

#### Korak 1 — Ploščina oklepe srednja linija $A_m$

Srednja linija poteka po sredini stene:

$$B_m = B - t = 10 - 1{,}5 = 8{,}5\ \text{cm}, \qquad H_m = H - t = 16 - 1{,}5 = 14{,}5\ \text{cm}$$

$$A_m = B_m \cdot H_m = 8{,}5 \cdot 14{,}5 = \boxed{123{,}25\ \text{cm}^2}$$

> ⚠️ **BREDTOVA PAST:** $A_m$ je ploščina, ki jo **oklepa** srednja linija stene — **ni** zunanja ploščina profila ($10 \times 16 = 160\ \text{cm}^2$) in **ni** notranja ploščina luknje!

#### Korak 2 — Bredtova formula

$$\tau = \frac{M_t}{2 \cdot A_m \cdot t} = \frac{360\ \text{kNcm}}{2 \cdot 123{,}25 \cdot 1{,}5} = \frac{360}{369{,}75} = \boxed{0{,}974\ \text{kN/cm}^2}$$

#### Korak 3 — Kontrola

$$\tau = 0{,}974\ \text{kN/cm}^2 > \tau_{dop} = 0{,}9\ \text{kN/cm}^2 \quad \Rightarrow \quad \textbf{❌ PREKORAČENO za 8\%}$$

> **Korekcija:** Potrebujemo $A_m \geq M_t/(2\tau_{dop}\cdot t) = 360/(2\cdot0{,}9\cdot1{,}5) = 133{,}3\ \text{cm}^2$ → povečajte dimenzije na npr. $B=11\ \text{cm}$, $H=17\ \text{cm}$ ($A_m = 9{,}5\cdot15{,}5=147{,}3$ ✓).

> ⚠️ **Bredt velja samo za:**  
> - Tankostenske zaprte profile ($t \ll B, H$)
> - Enakomerna ali znana debelina stene
> - Ni razrezov (zaprt obod!)

> **gl.:** [[Blok 5 - Torzija#Intuicija]]

---

## 9. UKLON EULER

### N19 — Euler uklon konzole
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 2 — Euler uklon konzole (kvadraten prerez)]]

$$\beta=2\ \text{(konzola)},\quad l_u=2L,\quad F_k=\frac{\pi^2 E I_{min}}{l_u^2},\quad \nu=F_k/F\geq\nu_{zaht}$$

---

### N20 — Euler uklon po šibki osi
> Rešena naloga: [[Vaje - Trdnost in dimenzioniranje#NALOGA 6 — Euler uklon prostoležeče palice (šibka os)]]

$$I_{min}=\frac{h\cdot b^3}{12}\ \text{(za }b<h\text{)},\quad \lambda=l_u/i_{min},\quad \lambda_E=\pi\sqrt{E/\sigma_{dop}}$$

---

## 10. UKLON TETMAJER — SREDNJE VITKE PALICE

### N21 — Tetmajer za les ← NOVA

> **Besedilo:** Leseni steber (smreka, iglavci) kvadratnega prereza $a=10\ \text{cm}$, dolžina $L=2{,}5\ \text{m}$, prostoležeč ($\beta=1$). Tlačna sila $F=25\ \text{kN}$. Preverite uklon — Euler ali Tetmajer? ($E=1000\ \text{kN/cm}^2$, $\sigma_{dop}=1{,}2\ \text{kN/cm}^2$, $\nu_{zaht}=3$)
>
> **Tetmajerjevi koeficienti za les (smreka/bor iglavci):** $a_T=2{,}93\ \text{kN/cm}^2$, $b_T=0{,}0194\ \text{kN/cm}^2$

#### Korak 1 — Geometrija prereza

$$A=a^2=100\ \text{cm}^2, \qquad I=\frac{a^4}{12}=\frac{10000}{12}=833{,}3\ \text{cm}^4$$

$$i=\sqrt{I/A}=\sqrt{8{,}33}=\boxed{2{,}887\ \text{cm}} \quad \text{(za kvadrat: }i=a/\sqrt{12}\text{)}$$

#### Korak 2 — Vitkost $\lambda$

$$l_u=\beta\cdot L=1\cdot250=250\ \text{cm}$$

$$\lambda=\frac{l_u}{i}=\frac{250}{2{,}887}=\boxed{86{,}6}$$

#### Korak 3 — Katerio območje? (Euler ali Tetmajer)

Meja Eulerjevega območja:

$$\lambda_E=\pi\sqrt{\frac{E}{\sigma_{dop}}}=\pi\sqrt{\frac{1000}{1{,}2}}=\pi\cdot28{,}87=\boxed{90{,}7}$$

| $\lambda$ | $\lambda_E$ | Območje |
|-----------|-------------|---------|
| 86,6 | 90,7 | $\lambda < \lambda_E$ → **TETMAJER!** |

> **Razlika:** Euler velja le za $\lambda > \lambda_E$ (zelo vitke palice). Za $\lambda_P < \lambda < \lambda_E$ (srednje vitke) napetost linearno pada — **Tetmajer**.

#### Korak 4 — Tetmajerjeva kritična napetost

$$\sigma_k = a_T - b_T \cdot \lambda = 2{,}93 - 0{,}0194 \cdot 86{,}6 = 2{,}93 - 1{,}680 = \boxed{1{,}250\ \text{kN/cm}^2}$$

#### Korak 5 — Kritična sila in varnostni faktor

$$F_k = \sigma_k \cdot A = 1{,}250 \cdot 100 = \boxed{125\ \text{kN}}$$

$$\nu = \frac{F_k}{F} = \frac{125}{25} = \boxed{5{,}0} \geq \nu_{zaht}=3 \quad \Rightarrow \quad \textbf{✓ VARNO}$$

#### Korak 6 — Primerjava: kaj bi dobili z Eulerjevo napako?

$$F_{k,Euler}=\frac{\pi^2\cdot1000\cdot833{,}3}{250^2}=\frac{8{,}225\cdot10^6}{62500}=\boxed{131{,}6\ \text{kN}}$$

Euler bi dal $\nu=5{,}26$ — rahlo **nekonservativna** ocena za to območje. Tetmajer je zanesljivejši!

> **Območja uklona:**
> ```
> λ < λP (~60 za les):  zdrs materiala (σ_dop neposredno)
> λP < λ < λE (~90):   Tetmajer  (linearna σk–λ)
> λ > λE:              Euler     (parabolična σk–λ, Fk = π²EI/lu²)
> ```

> **gl.:** [[Blok 4 - Euler Uklon#Intuicija]]

---

## 11. SESTAVLJENE OBREMENITVE — "REZKAR" (N + M + Mt)

### N22 — Rezkar: osna + upogib + torzija ← NOVA

> **Besedilo (tip izpit BTF):** Konzolni rezkar jeklene gredi: premer $d=3\ \text{cm}$, konzolna dolžina $L=20\ \text{cm}$. Na prostem koncu hkrati delujejo:
> - Osna tlačna sila $F_N=3\ \text{kN}$ (pritisk v les, vzdolž osi)
> - Prečna sila $F_\perp=2\ \text{kN}$ (odpor materiala, pravokotno na os)
> - Torzijski moment $M_t=1{,}2\ \text{kNm}=120\ \text{kNcm}$ (vrtenje)
>
> Preverite trdnost po Von Misesu. ($\sigma_{dop}=15\ \text{kN/cm}^2$)

#### Korak 1 — Geometrija prereza

$$A=\frac{\pi d^2}{4}=\frac{\pi\cdot9}{4}=7{,}07\ \text{cm}^2$$

$$W=\frac{\pi d^3}{32}=\frac{\pi\cdot27}{32}=2{,}65\ \text{cm}^3, \qquad W_t=2W=5{,}30\ \text{cm}^3$$

#### Korak 2 — Moment od prečne sile (upogib)

$$M_{max}=F_\perp\cdot L=2\cdot20=\boxed{40\ \text{kNcm}}$$

#### Korak 3 — Napetosti na kritičnem vlaknu

Kritično vlakno = spodnji rob (upogib + osna tlak — oba tlačna):

**Upogibna napetost:**

$$\sigma_M=\frac{M_{max}}{W}=\frac{40}{2{,}65}=\boxed{15{,}09\ \text{kN/cm}^2}\ \text{(nateg/tlak)}$$

**Osna napetost (tlak):**

$$\sigma_N=\frac{F_N}{A}=\frac{3}{7{,}07}=\boxed{0{,}42\ \text{kN/cm}^2}\ \text{(tlak, negativen)}$$

**Skupna normalna napetost na kritičnem vlaknu:**

$$\sigma=\sigma_M+\sigma_N=15{,}09+0{,}42=\boxed{15{,}51\ \text{kN/cm}^2}$$

> ⚠️ **Superpozicija:** $\sigma_M$ je nateg na spodnji strani, $\sigma_N$ je tlak — **odštejemo**? Odvisno od smeri!
> Ker $F_\perp$ povzroči nateg na eni in tlak na drugi strani ter $F_N$ povzroči enakomerni tlak:
> - Spodnji rob (nateg od upogiba, tlak od osi): $\sigma = +15{,}09 - 0{,}42 = +14{,}67\ \text{kN/cm}^2$
> - Zgornji rob (tlak od upogiba, tlak od osi): $\sigma = -15{,}09 - 0{,}42 = -15{,}51\ \text{kN/cm}^2$ ← **kritičen!**

$$\sigma_{krit}=\boxed{15{,}51\ \text{kN/cm}^2}\ \text{(tlak)}$$

**Torzijska strižna napetost:**

$$\tau=\frac{M_t}{W_t}=\frac{120}{5{,}30}=\boxed{22{,}64\ \text{kN/cm}^2}$$

#### Korak 4 — Von Mises ekvivalentna napetost

$$\sigma_{ekv}=\sqrt{\sigma_{krit}^2+3\tau^2}=\sqrt{15{,}51^2+3\cdot22{,}64^2}=\sqrt{240{,}6+1538{,}0}=\sqrt{1778{,}6}=\boxed{42{,}2\ \text{kN/cm}^2}$$

$$\sigma_{ekv}=42{,}2\ \text{kN/cm}^2 \gg \sigma_{dop}=15{,}0\ \text{kN/cm}^2 \quad \Rightarrow \quad \textbf{❌ DALEČ PREKORAČENO!}$$

#### Korak 5 — Dimenzioniranje: koliko d potrebujemo?

Pogoj: $\sigma_{ekv} \leq \sigma_{dop}$

Ker $\tau$ dominira (torzija), povečajmo $d$. Za d=5cm:

$$W=\frac{\pi\cdot125}{32}=12{,}27\ \text{cm}^3,\quad W_t=24{,}54\ \text{cm}^3,\quad A=19{,}63\ \text{cm}^2$$

$$\sigma_M=40/12{,}27=3{,}26,\quad \sigma_N=3/19{,}63=0{,}15,\quad \sigma=3{,}41\ \text{kN/cm}^2$$

$$\tau=120/24{,}54=4{,}89\ \text{kN/cm}^2$$

$$\sigma_{ekv}=\sqrt{3{,}41^2+3\cdot4{,}89^2}=\sqrt{11{,}6+71{,}8}=\sqrt{83{,}4}=9{,}13\ \text{kN/cm}^2<15 \quad ✓$$

$$\boxed{d_{min}\approx 5\ \text{cm}}$$

> **Pouk:** Torzija je tista, ki "ubije" rezkar — njen doprinos je $3\tau^2$ v Von Misesu. Povečanje premera zmanjša $\tau \propto 1/d^3$, kar ima kubični učinek!

> **gl.:** [[Blok 5 - Torzija#Intuicija]] | [[Blok 3.5 - Hipoteze Porusitve#Intuicija]]

---

## Povzetek izpitnih formul

### NTM diagrami

$$T(x)=\int q\,dx+\sum F_i \qquad M(x)=\int T\,dx$$

Skok v T: točkovna sila $F$ → Skok v M: točkovni moment $M_0$

### Upogib — dimenzioniranje

$$W_{min}=\frac{M_{max}}{\sigma_{dop}}, \quad \text{za } h=2b:\ W=\frac{2b^3}{3} \Rightarrow b=\sqrt[3]{\frac{3W_{min}}{2}}$$

### Napetostni tenzor

$$S=\frac{\sigma_x+\sigma_y}{2},\quad R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2},\quad \sigma_{1,2}=S\pm R$$

### Hipoteze porušitve

$$\sigma_{ekv,VM}=\sqrt{\sigma^2+3\tau^2} \leq \sigma_{dop}, \qquad \sigma_{ekv,T}=\sqrt{\sigma^2+4\tau^2} \leq \sigma_{dop}$$

### Torzija

$$\tau=\frac{M_t}{W_t}\ \text{(polna gred)}, \qquad \tau=\frac{M_t}{2A_m t}\ \text{(Bredt, votel prerez)}$$

### Uklon

$$F_k=\frac{\pi^2 E I_{min}}{l_u^2}\ \text{(Euler, }\lambda>\lambda_E\text{)}, \qquad \sigma_k=a_T-b_T\lambda\ \text{(Tetmajer, }\lambda<\lambda_E\text{)}$$

$$\lambda=\frac{l_u}{i_{min}},\quad i_{min}=\sqrt{\frac{I_{min}}{A}},\quad \lambda_E=\pi\sqrt{\frac{E}{\sigma_{dop}}}$$

---

## Hierarhija zahtevnosti

```
OSNOVNE:
  ├── NTM diagrami (prosta greda, q + F)
  ├── Upogib dimenzioniranje (W = M/σ)
  └── Euler uklon (Fk, λ, ν)

SREDNJE:
  ├── Portalni okvir / L-nosilci (N↔T v oglu)
  ├── Mohrova krožnica (σ1, σ2 grafično)
  ├── Tetmajer (λ < λE, linearna enačba)
  └── Bredt za votli prerez (Am, ne A!)

NAPREDNE:
  ├── Deformacijski → napetostni tenzor (Hookov zakon 3D)
  ├── Ekscentrični tlak N + M (superpozicija)
  └── Rezkar N + M + Mt → Von Mises (dominira τ!)
```

---

## Povezave

- [[Blok 1 - NTM Diagrami]] ← teorija NTM, postopek
- [[Blok 1.5 - Geometrijske Karakteristike]] ← W, I, Steiner
- [[Blok 2 - Upogib]] ← σ = M/W, dimenzioniranje
- [[Blok 3 - Napetostno Stanje]] ← tenzor, Mohr
- [[Blok 3.5 - Hipoteze Porusitve]] ← Tresca, Von Mises
- [[Blok 4 - Euler Uklon]] ← Fk, λ, β, Tetmajer
- [[Blok 5 - Torzija]] ← τ, Wt, Bredt
- [[Vaje - NTM diagrami - Vse vrste]] ← rešene NTM naloge
- [[Vaje - Trdnost in dimenzioniranje]] ← rešene trdnostne naloge
- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← rešene tenzorske naloge
- [[Poglavje - Statika]] ← predhodno poglavje
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

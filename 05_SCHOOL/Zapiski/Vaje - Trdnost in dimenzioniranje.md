---
tags: [mehanika, trdnost, upogib, uklon, dimenzioniranje, tresca, von-mises, izpit]
predmet: Mehanika
datum: 2026-06-15
---

# Vaje — Trdnost in dimenzioniranje

## Namen

Celovite rešene naloge za poglavje **NALOGA 3 — Trdnost in dimenzioniranje**. Vsaka naloga pokriva drug tip izpitnega vprašanja, z izpeljavo korak za korakom od branja naloge do zaključka.

---

## Kazalo nalog

| Naloga | Tip | Ključna tehnika |
|--------|-----|-----------------|
| [[#NALOGA 1 — Dimenzioniranje pravokotnega prereza (upogib)\|NALOGA 1]] | Upogib, dimenzioniranje b:h=1:2 | M-diagram, W iz pogoja σ≤σdop |
| [[#NALOGA 2 — Euler uklon konzole (kvadraten prerez)\|NALOGA 2]] | Euler uklon, konzola β=2 | lu, Imin, vitkost λ, Fk |
| [[#NALOGA 3 — Kontrola napetosti asimetričnega T-prereza\|NALOGA 3]] | T-prerez, Steiner | W_sp ≠ W_zg, kritičen rob |
| [[#NALOGA 4 — Ekscentrični tlak N + M\|NALOGA 4]] | N + M superponiranje | Nateg v tlačno obremenjenem prerezu! |
| [[#NALOGA 5 — Sestavljena obremenitev upogib + torzija\|NALOGA 5]] | M + Mt, Von Mises, Tresca | σekv = √(σ²+3τ²) vs √(σ²+4τ²) |
| [[#NALOGA 6 — Euler uklon prostoležeče palice\|NALOGA 6]] | Euler, β=1, šibka os | Imin, λ > λe kontrola |

---

## NALOGA 1 — Dimenzioniranje pravokotnega prereza (upogib)

![[trdnost_n1.svg|697]]

> **Besedilo naloge:** Navpičen leseni nosilci (iglavci) dolžine $L = 5\ \text{m}$ leži na dveh prostoležečih podporah. Po celotni dolžini ga obremenjuje enakomerna porazdeljena obtežba $q = 3\ \text{kN/m}$, na sredini razpona pa deluje dodatna točkovna sila $F = 10\ \text{kN}$. Dimenzioniraje pravokoten prerez iz lesa pri dopustni napetosti $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$ ob pogoju $h : b = 2 : 1$.

**Podatki:**
- Prostoležeč leseni nosilci, $L = 5\ \text{m}$
- Enakomerna porazdeljena obremenitev: $q = 3\ \text{kN/m}$
- Točkovna sila na sredini: $F = 10\ \text{kN}$
- Material: les (iglavci), $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$
- Razmerje prereza: $b : h = 1 : 2$ (b = x, h = 2x)

---

### Korak 1 — Reakcije

Ker je obtežba simetrična (F na sredini):

$$A_y = B_y = \frac{q \cdot L + F}{2} = \frac{3 \cdot 5 + 10}{2} = \frac{25}{2} = \boxed{12{,}5\ \text{kN}}$$

> **glej:** [[Koncept - Statično ravnotežje#Reakcije]]

---

### Korak 2 — M-diagram in Mmax

Za $x \in [0,\ 2{,}5]\ \text{m}$:

$$M(x) = A_y \cdot x - \frac{q \cdot x^2}{2} = 12{,}5x - 1{,}5x^2$$

$$\frac{dM}{dx} = 12{,}5 - 3x = 0 \quad \Rightarrow \quad x = 4{,}17\ \text{m}$$

Ker je $x = 4{,}17\ \text{m}$ **zunaj** regije $[0; 2{,}5]$, je M v tem delu monotono naraščujoč → Mmax pri $x = 2{,}5\ \text{m}$ (pod silo F):

$$\boxed{M_{max} = 12{,}5 \cdot 2{,}5 - 1{,}5 \cdot 2{,}5^2 = 31{,}25 - 9{,}375 = 21{,}875\ \text{kNm}}$$

Pretvorba enot: $M_{max} = 2187{,}5\ \text{kNcm}$

> **Napaka:** Ne pozabi, da M-diagram za $q$ ni linearen, ampak paraboličen!

> **glej:** [[Koncept - Upogib#M-diagram]]

---

### Korak 3 — Odpornostni moment W

Pogoj trdnosti: $\sigma = M/W \leq \sigma_{dop}$

$$W_{min} = \frac{M_{max}}{\sigma_{dop}} = \frac{2187{,}5\ \text{kNcm}}{1{,}0\ \text{kN/cm}^2} = \boxed{2187{,}5\ \text{cm}^3}$$

Za pravokoten prerez z $b = x$, $h = 2x$:

$$W = \frac{b \cdot h^2}{6} = \frac{x \cdot (2x)^2}{6} = \frac{4x^3}{6} = \frac{2x^3}{3}$$

> **💡 Zlato pravilo h:b:** Ko je h=2b, se W podvoji v primerjavi s kvadratnim prerezom — višji tram je bistveno bolj učinkovit pri upogibu!

---

### Korak 4 — Izračun dimenzij

$$\frac{2x^3}{3} = 2187{,}5 \quad \Rightarrow \quad x^3 = 3281{,}25 \quad \Rightarrow \quad x = \sqrt[3]{3281{,}25} = 14{,}84\ \text{cm}$$

$$\boxed{b = 15\ \text{cm}, \qquad h = 30\ \text{cm}}$$

(zaokroženo navzgor na celo število)

---

### Korak 5 — Kontrola

$$W_{dej} = \frac{2 \cdot 15^3}{3} = \frac{6750}{3} = 2250\ \text{cm}^3$$

$$\sigma = \frac{M_{max}}{W_{dej}} = \frac{2187{,}5}{2250} = \boxed{0{,}972\ \text{kN/cm}^2} < 1{,}0\ \text{kN/cm}^2 \quad ✓$$

| Veličina | Vrednost |
|----------|----------|
| $b$ | 15 cm |
| $h$ | 30 cm |
| $W_{dej}$ | 2250 cm³ |
| $\sigma_{max}$ | 0,972 kN/cm² |
| $\sigma_{dop}$ | 1,0 kN/cm² |
| Izkoriščenost | 97,2% ✓ |

---

## NALOGA 2 — Euler uklon konzole (kvadraten prerez)

![[trdnost_n2.svg]]

> **Besedilo naloge:** Lesen steber (iglavci) kvadratnega prereza $a \times a$ in dolžine $L = 4\ \text{m}$ je vpet spodaj kot konzola — spodaj togo vpet, zgoraj prost. Na prostem koncu deluje navpična tlačna sila $F = 30\ \text{kN}$. Dimenzioniraje prerez pri zahtevanem varnostnem faktorju $\nu = 3$ in preverite, ali je steber v Eulerjevem uklonskem območju. ($E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$)

**Podatki:**
- Lesen steber, $L = 4\ \text{m} = 400\ \text{cm}$
- Vpetje: **spodaj vpet – zgoraj prost** (konzola, $\beta = 2$)
- Sila: $F = 30\ \text{kN}$ (navpično, na prostem koncu)
- Kvadraten prerez: $a \times a$
- Material: $E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$
- Zahtevana varnost: $\nu = 3$

---

### Korak 1 — Uklonska dolžina lu

Konzola (Eulerjeva oblika 4 — najnevarnejša):

$$l_u = \beta \cdot L = 2 \cdot 400\ \text{cm} = \boxed{800\ \text{cm}}$$

> **Zakaj β=2?** Konzola se upogne, kot bi bila prosta palica dvakratne dolžine — navidezno se podaljša, ker nimamo podpore zgoraj.

> **glej:** [[Koncept - Euler Uklon#Eulerove oblike vpetja]]

---

### Korak 2 — Minimalna kritična sila Fk

$$F_k = \nu \cdot F_{dej} = 3 \cdot 30 = \boxed{90\ \text{kN}}$$

---

### Korak 3 — Dimenzioniranje iz Eulerjeve formule

Za kvadraten prerez: $I_{min} = a^4/12$

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2} \quad \Rightarrow \quad 90 = \frac{\pi^2 \cdot 1000 \cdot (a^4/12)}{800^2}$$

$$a^4 = \frac{90 \cdot 800^2 \cdot 12}{\pi^2 \cdot 1000} = \frac{90 \cdot 640\,000 \cdot 12}{9{,}8696 \cdot 1000} = \frac{691\,200\,000}{9869{,}6} = 70\,030\ \text{cm}^4$$

$$a = \sqrt[4]{70\,030} = 16{,}27\ \text{cm} \quad \Rightarrow \quad \boxed{a = 17\ \text{cm}}$$

---

### Korak 4 — Preveritev Eulerjevega območja (vitkost)

$$i = \frac{a}{\sqrt{12}} = \frac{17}{3{,}464} = 4{,}91\ \text{cm}$$

$$\lambda = \frac{l_u}{i} = \frac{800}{4{,}91} = 163$$

$$\lambda_e = \pi \sqrt{\frac{E}{\sigma_{dop}}} = \pi \sqrt{\frac{1000}{1{,}2}} = \pi \cdot 28{,}87 = 90{,}7$$

$$\lambda = 163 > \lambda_e = 90{,}7 \quad \Rightarrow \quad \textbf{Eulerova formula velja ✓}$$

> **Fizikalni pomen:** Ker je λ>λe, steber odpove z elastičnim uklonom (ne z materialno trdnostjo). Obratno bi bila merodajna ω metoda.

> **glej:** [[Koncept - Euler Uklon#Vitkost λ in meja λe]]

---

### Korak 5 — Kontrola čistega tlaka

$$A = 17^2 = 289\ \text{cm}^2$$

$$\sigma_{tlak} = \frac{F}{A} = \frac{30}{289} = 0{,}104\ \text{kN/cm}^2 \ll 1{,}2\ \text{kN/cm}^2 \quad ✓$$

> **Ključen zaključek:** Steber bi zdržal **12×** večjo silo po kriteriju trdnosti, a odpove z uklonom pri $F=30\ \text{kN}$. **Uklon nadzoruje dimenzioniranje!**

| Veličina | Vrednost |
|----------|----------|
| $a$ | 17 cm |
| $l_u$ | 800 cm |
| $\lambda$ | 163 |
| $\lambda_e$ | 90,7 |
| $F_k$ | 90 kN |
| $\sigma_{tlak}$ | 0,104 kN/cm² ✓ |

---

## NALOGA 3 — Kontrola napetosti asimetričnega T-prereza

![[trdnost_n3.svg]]

> **Besedilo naloge:** Jekleni varjenec T-prereza (pasnica $12\ \text{cm} \times 2\ \text{cm}$ zgoraj, stojina $2\ \text{cm} \times 12\ \text{cm}$ spodaj) leži kot prostoležeč nosilci razpona $L = 4\ \text{m}$. Na sredini razpona deluje točkovna sila $F = 25\ \text{kN}$. Izračunajte napetosti na zgornji in spodnji vlakni prerezu in preverite, ali je prerez zadosten. ($\sigma_{dop} = 16\ \text{kN/cm}^2$)

**Podatki:**

T-prerez iz jekla (varjenec):
- Pasnica (flange): $12\ \text{cm} \times 2\ \text{cm}$ (zgoraj)
- Stojina (web): $2\ \text{cm} \times 12\ \text{cm}$ (spodaj)
- Skupna višina: $H = 14\ \text{cm}$

Sistem: prostoležeč nosilci, $L = 4\ \text{m}$, točkovna sila $F = 25\ \text{kN}$ na sredini

$\sigma_{dop} = 16\ \text{kN/cm}^2$

---

### Korak 1 — Ploščine in težiščne razdalje

| Del | $A_i\ \text{[cm}^2]$ | $y_i$ od spodaj [cm] | $A_i \cdot y_i$ |
|-----|------|------|----------|
| Stojina (2×12) | 24 | 6,0 | 144 |
| Pasnica (12×2) | 24 | 13,0 | 312 |
| **Skupaj** | **48** | | **456** |

$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i} = \frac{456}{48} = \boxed{9{,}5\ \text{cm od spodaj}}$$

$$e_{sp} = 9{,}5\ \text{cm} \qquad e_{zg} = 14 - 9{,}5 = 4{,}5\ \text{cm}$$

> **Opomba:** Težišče T-prereza je bliže pasnici! Ker je spodnji rob dlje od težišča ($e_{sp} > e_{zg}$), bo spodnji rob bolj obremenjen.

> **glej:** [[Koncept - Upogib#Steiner za sestavljene prereze]]

---

### Korak 2 — Vztrajnostni moment (Steiner)

**Stojina** (os lastnega těžišča pri $y = 6$ cm):

$$I_{stoj} = \frac{2 \cdot 12^3}{12} + 24 \cdot (6 - 9{,}5)^2 = 288 + 24 \cdot 12{,}25 = 288 + 294 = 582\ \text{cm}^4$$

**Pasnica** (os lastnega těžišča pri $y = 13$ cm):

$$I_{pas} = \frac{12 \cdot 2^3}{12} + 24 \cdot (13 - 9{,}5)^2 = 8 + 24 \cdot 12{,}25 = 8 + 294 = 302\ \text{cm}^4$$

$$\boxed{J = I_{stoj} + I_{pas} = 582 + 302 = 884\ \text{cm}^4}$$

---

### Korak 3 — Odpornostna momenta

Ker sta $e_{sp} \neq e_{zg}$, sta **oba W različna** — to je bistvo asimetričnega prereza!

$$W_{sp} = \frac{J}{e_{sp}} = \frac{884}{9{,}5} = 93{,}05\ \text{cm}^3 \quad \leftarrow \textbf{manjši → kritičen!}$$

$$W_{zg} = \frac{J}{e_{zg}} = \frac{884}{4{,}5} = 196{,}4\ \text{cm}^3$$

---

### Korak 4 — Obremenitev in napetosti

Prostoležeč + F na sredini:

$$M_{max} = \frac{F \cdot L}{4} = \frac{25 \cdot 4}{4} = 25\ \text{kNm} = 2500\ \text{kNcm}$$

$$\sigma_{sp} = \frac{M_{max}}{W_{sp}} = \frac{2500}{93{,}05} = \boxed{26{,}9\ \text{kN/cm}^2} \quad \Rightarrow \quad 26{,}9 > 16 \quad \textbf{❌ PREKORAČENO!}$$

$$\sigma_{zg} = \frac{M_{max}}{W_{zg}} = \frac{2500}{196{,}4} = \boxed{12{,}7\ \text{kN/cm}^2} \quad \Rightarrow \quad 12{,}7 < 16 \quad ✓$$

---

### Korak 5 — Zaključek

| Rob | $W\ [\text{cm}^3]$ | $\sigma\ [\text{kN/cm}^2]$ | $\sigma_{dop}$ | Ocena |
|-----|-----|------|------|-------|
| Spodnji (nateg) | 93,05 | 26,9 | 16 | ❌ PREKORAČENO |
| Zgornji (tlak) | 196,4 | 12,7 | 16 | ✓ varno |

**Prerez ni zadosten!** Kritičen je spodnji rob (natazan rob), ker je dlje od težišča. Za varno delovanje bi potrebovali vsaj:

$$W_{min} = \frac{M_{max}}{\sigma_{dop}} = \frac{2500}{16} = 156{,}3\ \text{cm}^3 > 93{,}05\ \text{cm}^3$$

> **Rešitev:** Povečaj stojino ali dodaj manjšo spodnjo pasnico (kanal/U prerez).

> **Pogosta napaka:** Vzeti samo en W (kot pri simetričnem prerezu). Pri asimetričnih profilih **vedno preveri oba robova!**

---

## NALOGA 4 — Ekscentrični tlak N + M

![[trdnost_n4.svg]]

> **Besedilo naloge:** Kratki jekleni steber kvadratnega prereza $10\ \text{cm} \times 10\ \text{cm}$ je obremenjen z navpično tlačno silo $F = 200\ \text{kN}$, ki deluje na odmiku $e = 3\ \text{cm}$ od geometrijske osi stebra. Izračunajte napetostno porazdelitev po prerezu, ugotovite, ali se na kateri strani pojavi nateg, in preverite trdnostni pogoj. ($\sigma_{dop} = 16\ \text{kN/cm}^2$)

**Podatki:**
- Kratki jekleni steber: kvadraten prerez $10\ \text{cm} \times 10\ \text{cm}$
- Navpična sila: $F = 200\ \text{kN}$, deluje na odmiku $e = 3\ \text{cm}$ od osi stebra
- $\sigma_{dop,tlak} = 16\ \text{kN/cm}^2$, $\sigma_{dop,nat} = 16\ \text{kN/cm}^2$

---

### Korak 1 — Razstavi silo na N in M

Ekscentrična sila je **ekvivalentna** centrični sili + momentu:

$$N = -F = -200\ \text{kN} \quad \text{(tlak)}$$

$$M = F \cdot e = 200 \cdot 3 = 600\ \text{kNcm}$$

> **Fizikalni pomen:** Sila, ki ne deluje skozi težišče, povzroča hkrati tlak (N) in upogib (M). Superpozicija!

> **glej:** [[Koncept - Upogib#Ekscentrična obremenitev]]

---

### Korak 2 — Lastnosti prereza

$$A = 10 \times 10 = 100\ \text{cm}^2$$

$$W = \frac{b \cdot h^2}{6} = \frac{10 \cdot 10^2}{6} = \frac{1000}{6} = 166{,}7\ \text{cm}^3$$

---

### Korak 3 — Napetosti od N in M

**Normalna sila** (enakomerna po prerezu):

$$\sigma_N = \frac{N}{A} = \frac{-200}{100} = -2{,}0\ \text{kN/cm}^2 \quad \text{(tlak)}$$

**Upogibni moment** (linearna porazdelitev, max na robovih):

$$\sigma_M = \pm\frac{M}{W} = \pm\frac{600}{166{,}7} = \pm 3{,}6\ \text{kN/cm}^2$$

---

### Korak 4 — Superponiranje napetosti

$$\sigma_{max} = \sigma_N - \sigma_M = -2{,}0 - 3{,}6 = \boxed{-5{,}6\ \text{kN/cm}^2} \quad \text{(tlak, na strani sile)}$$

$$\sigma_{min} = \sigma_N + \sigma_M = -2{,}0 + 3{,}6 = \boxed{+1{,}6\ \text{kN/cm}^2} \quad \textbf{(nateg! — na nasprotni strani)}$$

> **⚠️ KLJUČNO:** Kljub temu, da je sila **tlačna**, se na nasprotni strani prerezu pojavi **nateg**! To je pogosto presenečenje na izpitu!

---

### Korak 5 — Nevtralna os

Napetost je nič pri:

$$\sigma = \sigma_N + \frac{M \cdot y}{J} = 0 \quad \Rightarrow \quad y_0 = -\frac{\sigma_N \cdot J}{M}$$

$$J = \frac{10^4}{12} = 833{,}3\ \text{cm}^4 \qquad y_0 = -\frac{(-2{,}0) \cdot 833{,}3}{600} = \frac{1666{,}6}{600} = +2{,}78\ \text{cm}$$

Nevtralna os je $2{,}78\ \text{cm}$ od težišča v smeri natega — **ni skozi težišče!**

---

### Korak 6 — Kontrola

| Napetost | Vrednost | $\sigma_{dop}$ | Ocena |
|----------|----------|----------------|-------|
| $\sigma_{max}$ (tlak) | −5,6 kN/cm² | 16 kN/cm² | ✓ |
| $\sigma_{min}$ (nateg) | +1,6 kN/cm² | 16 kN/cm² | ✓ |

Steber je varen. Kritičen je tlačni rob (strani sile).

---

## NALOGA 5 — Sestavljena obremenitev upogib + torzija

![[trdnost_n5.svg]]

> **Besedilo naloge:** Jeklena gred polnega krožnega prereza premera $d = 50\ \text{mm}$ je hkrati obremenjena z upogibnim momentom $M = 1{,}5\ \text{kNm}$ in torzijskim momentom $M_t = 1{,}2\ \text{kNm}$. Preverite trdnost gredi po hipotezah Von Mises in Tresca. Katero hipotezo bi izbrali za projektiranje? ($\sigma_{dop} = 150\ \text{MPa}$)

**Podatki:**
- Jeklena gred, polni krog: $d = 50\ \text{mm} = 5\ \text{cm}$
- Upogibni moment: $M = 1{,}5\ \text{kNm} = 150\ \text{kNcm}$
- Torzijski moment: $M_t = 1{,}2\ \text{kNm} = 120\ \text{kNcm}$
- $\sigma_{dop} = 15\ \text{kN/cm}^2 = 150\ \text{MPa}$

---

### Korak 1 — Odpornostni momenta za polni krog

$$W = \frac{\pi d^3}{32} = \frac{\pi \cdot 5^3}{32} = \frac{125\pi}{32} = 12{,}27\ \text{cm}^3$$

$$W_t = \frac{\pi d^3}{16} = 2W = 24{,}54\ \text{cm}^3$$

> **💡 Trik:** $W_t = 2W$ za polni krog — torzijski odpornostni moment je natanko **dvakrat** upogibni!

> **glej:** [[Koncept - Torzija#Polni krog]]

---

### Korak 2 — Napetosti na kritičnem vlaknu

$$\sigma = \frac{M}{W} = \frac{150}{12{,}27} = 12{,}22\ \text{kN/cm}^2 = \mathbf{122{,}2\ \text{MPa}}$$

$$\tau = \frac{M_t}{W_t} = \frac{120}{24{,}54} = 4{,}89\ \text{kN/cm}^2 = \mathbf{48{,}9\ \text{MPa}}$$

> **Napetostno stanje na kritičnem vlaknu** (spodnji rob pri upogibu):
> $$\sigma_{ij} = \begin{pmatrix} \sigma & \tau \\ \tau & 0 \end{pmatrix} = \begin{pmatrix} 12{,}22 & 4{,}89 \\ 4{,}89 & 0 \end{pmatrix}\ \text{kN/cm}^2$$

---

### Korak 3 — Ekvivalentna napetost po Von Mises

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} = \sqrt{12{,}22^2 + 3 \cdot 4{,}89^2}$$

$$= \sqrt{149{,}3 + 71{,}7} = \sqrt{221{,}0} = \boxed{14{,}87\ \text{kN/cm}^2 = 148{,}7\ \text{MPa}}$$

---

### Korak 4 — Ekvivalentna napetost po Tresca

$$\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} = \sqrt{12{,}22^2 + 4 \cdot 4{,}89^2}$$

$$= \sqrt{149{,}3 + 95{,}7} = \sqrt{245{,}0} = \boxed{15{,}65\ \text{kN/cm}^2 = 156{,}5\ \text{MPa}}$$

> **💡 Trik "Tresca 4, VM 3":** Razlika med hipotezama je **samo** v faktorju (4 ali 3) pred $\tau^2$!

---

### Korak 5 — Primerjava in zaključek

| Hipoteza | $\sigma_{ekv}$ [MPa] | $\sigma_{dop}$ [MPa] | Ocena |
|----------|------|------|-------|
| Von Mises | 148,7 | 150 | ✓ varno (komaj!) |
| Tresca | 156,5 | 150 | ❌ PREKORAČENO! |

**Zaključek:** Gred je po Von Misesu varna, a po Trescu presega dopustno napetost za 4,3%.

- Ker Tresca ni zadovoljen → **inženirsko: gred ni dovolj dimenzionirana!**
- Tresca je vedno bolj konzervativna: $\sigma_{ekv,T} \geq \sigma_{ekv,VM}$

> **Na izpitu:** Če ni podana hipoteza, izračunaj **obe** in navedi, katera je strožja. Tresca je varna izbira.

> **glej:** [[Koncept - Napetostno stanje#Hipotezi porušitve — Tresca in Von Mises]]

---

## NALOGA 6 — Euler uklon prostoležeče palice (šibka os)

![[trdnost_n6.svg]]

> **Besedilo naloge:** Lesen steber pravokotnega prereza ($b = 10\ \text{cm}$, $h = 15\ \text{cm}$) in dolžine $L = 4\ \text{m}$ je podprt na obeh koncih prostoležeče ($\beta = 1$). Na steber deluje osna tlačna sila $F = 20\ \text{kN}$. Preverite varnost pred uklonom in izračunajte dejanski varnostni faktor. Upoštevajte uklon po šibki osi. ($E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$, $\nu_{zaht} = 3$)

**Podatki:**
- Lesen steber, pravokoten prerez: $b = 10\ \text{cm}$, $h = 15\ \text{cm}$
- Vpetje: **zgoraj in spodaj prostoležeče** ($\beta = 1$, Eulerova oblika 1)
- Dolžina: $L = 4\ \text{m} = 400\ \text{cm}$
- Tlačna sila: $F = 20\ \text{kN}$
- $E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$, $\nu = 3$

---

### Korak 1 — Imin (šibka os)

Uklon nastopi vedno po **šibki osi** (os z manjšim I):

$$I_{min} = \frac{h \cdot b^3}{12} = \frac{15 \cdot 10^3}{12} = \frac{15000}{12} = \boxed{1250\ \text{cm}^4}$$

$$I_{max} = \frac{b \cdot h^3}{12} = \frac{10 \cdot 15^3}{12} = \frac{33750}{12} = 2812{,}5\ \text{cm}^4$$

> **Zakaj Imin?** Steber se bo uklonili v smeri najmanjšega odpora. Bolj tanka dimenzija (b=10cm) pomeni večjo nevarnost uklona v tej ravnini!

> **glej:** [[Koncept - Euler Uklon#Imin — uklon po šibki osi]]

---

### Korak 2 — Uklonska dolžina in vitkost

$$l_u = \beta \cdot L = 1 \cdot 400 = 400\ \text{cm}$$

$$A = b \cdot h = 10 \cdot 15 = 150\ \text{cm}^2$$

$$i = \sqrt{\frac{I_{min}}{A}} = \sqrt{\frac{1250}{150}} = \sqrt{8{,}33} = 2{,}887\ \text{cm} \quad \text{(vztrajnostni polmer)}$$

$$\lambda = \frac{l_u}{i} = \frac{400}{2{,}887} = \boxed{138{,}6}$$

---

### Korak 3 — Kontrola Eulerjevega območja

$$\lambda_e = \pi \sqrt{\frac{E}{\sigma_{dop}}} = \pi \sqrt{\frac{1000}{1{,}2}} = \pi \cdot 28{,}87 = \boxed{90{,}7}$$

$$\lambda = 138{,}6 > \lambda_e = 90{,}7 \quad \Rightarrow \quad \textbf{Eulerova formula velja ✓}$$

Ker je λ > λe, je steber v **elastičnem območju uklona** — Euler direktno.

> **Če bi λ < λe:** Uporabimo ω-metodo (tabele za les ali jeklo). Za les: ω odčitamo iz tabele po λ.

> **glej:** [[Koncept - Euler Uklon#ω metoda vs Euler]]

---

### Korak 4 — Kritična sila

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2} = \frac{9{,}8696 \cdot 1000 \cdot 1250}{400^2} = \frac{12\,337\,000}{160\,000} = \boxed{77{,}1\ \text{kN}}$$

---

### Korak 5 — Dopustna sila in kontrola

$$F_{dop} = \frac{F_k}{\nu} = \frac{77{,}1}{3} = 25{,}7\ \text{kN}$$

$$F_{dej} = 20\ \text{kN} < F_{dop} = 25{,}7\ \text{kN} \quad \Rightarrow \quad ✓\ \text{VARNO}$$

Varnostni faktor dejansko dosežen: $\nu_{dej} = 77{,}1/20 = 3{,}86 > 3$

---

### Korak 6 — Kontrola čistega tlaka (za celost)

$$\sigma_{tlak} = \frac{F}{A} = \frac{20}{150} = 0{,}133\ \text{kN/cm}^2 \ll 1{,}2\ \text{kN/cm}^2 \quad ✓$$

> Steber je dimenzioniran z uklonom (λ>λe). Materialna trdnost je daleč od meje.

| Veličina | Vrednost |
|----------|----------|
| $I_{min}$ (šibka os) | 1250 cm⁴ |
| $\lambda$ | 138,6 |
| $\lambda_e$ | 90,7 |
| $F_k$ (Euler) | 77,1 kN |
| $F_{dop}$ | 25,7 kN |
| $F_{dej}$ | 20 kN ✓ |
| $\nu_{dej}$ | 3,86 ✓ |

---

## Povzetek formul — izpit na hitro

### Upogib (dimenzioniranje)

| Prerez | $W$ | Dimenzioniranje |
|--------|-----|----------------|
| Krog d | $\pi d^3/32$ | $d \geq \sqrt[3]{32M/\pi\sigma_{dop}}$ |
| Pravokotnik b×h | $bh^2/6$ | $W \geq M/\sigma_{dop}$, nato reši za b ali h |
| h=2b | $2b^3/3$ | $b \geq \sqrt[3]{3M/2\sigma_{dop}}$ |
| Asimetričen | $J/e_{sp}$ in $J/e_{zg}$ | Preveri oba robova! |

### Euler uklon

$$\boxed{F_k = \frac{\pi^2 E I_{min}}{l_u^2}} \qquad l_u = \beta L$$

| Vpetje | β | Skica |
|--------|---|-------|
| Prostoležeč–prostoležeč | 1 | standardno |
| Vpet–prostoležeč | 0,7 | |
| Vpet–vpet | 0,5 | najvarnejše |
| Vpet–prost (konzola) | **2** | **najnevarnejše!** |

$$\lambda = \frac{l_u}{i}, \quad i = \sqrt{I_{min}/A}, \quad \lambda_e = \pi\sqrt{E/\sigma_{dop}}$$

- $\lambda > \lambda_e$: Euler formula velja
- $\lambda < \lambda_e$: ω metoda (tabele)

### Ekscentrični N + M

$$\sigma = \frac{N}{A} \pm \frac{M}{W} \quad \leftarrow \text{superponiranje}$$

### Sestavljena obremenitev M + Mt

| Hipoteza | Formula |
|----------|---------|
| Von Mises | $\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$ |
| Tresca | $\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$ |

> **Trik "Tresca 4, VM 3"** — pomni za izpit!

---

## Povezave

- [[Koncept - Upogib]] ← W, M-diagram, dimenzioniranje, Steiner
- [[Koncept - Euler Uklon]] ← lu, λ, Fk, ω metoda, β tabela
- [[Koncept - Torzija]] ← Wt=2W, φ, kombinirano M+Mt
- [[Koncept - Napetostno stanje]] ← tenzor, glavne napetosti, Tresca, VM, hitre formule
- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← naloge 3 in 5 (M+Mt, čist strig)
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

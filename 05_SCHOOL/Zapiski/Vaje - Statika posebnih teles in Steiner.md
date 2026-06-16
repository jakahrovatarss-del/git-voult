---
tags: [mehanika, statika, škripec, valji, steiner, sestavljen-prerez, reakcije, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Vaje — Statika posebnih teles in Steiner

## Namen

Celovite rešene naloge za poglavje **NALOGA 4 — Statika posebnih teles** (BTF izpitni tipi). Pokriva: škripce/dvigala, valje v kupu, nagnjene konstrukcije in vzporednoosni izrek (Steiner). Vsaka naloga z izpeljavo korak za korakom.

---

## Kazalo nalog

| Naloga                                                                          | Tip                               | Ključna tehnika           |
| ------------------------------------------------------------------------------- | --------------------------------- | ------------------------- |
| [[#NALOGA 1 — Dvigalo s škripcem (konzolni L-nosilci)\|NALOGA 1]]               | Škripec, reakcije v vpetju        | S = G, ΣM okrog B         |
| [[#NALOGA 2 — Škripec z nagnjeno vrvjo\|NALOGA 2]]                              | Škripec + kot vrvi                | Razstavi S na Sx, Sy      |
| [[#NALOGA 3 — Valji v kupu (3+2+1)\|NALOGA 3]]                                  | Valji, geometrija 60°, ravnovesje | N1 iz sin60°, F iz stika  |
| [[#NALOGA 4 — Nagnjena konstrukcija z obremenitvijo pod kotom\|NALOGA 4]]       | Kos α, reakcije                   | Fx=Fcosα, Fy=Fsinα        |
| [[#NALOGA 5 — Steiner za T-prerez (BTF primer)\|NALOGA 5]]                      | Steiner, sestavljen prerez        | yT, J, Wsp≠Wzg            |
| [[#NALOGA 6 — Kombinirana naloga: nagnjeni steber + Steiner + uklon\|NALOGA 6]] | Vse skupaj: statika→Steiner→Euler | Celotna veriga BTF izpita |

---

## NALOGA 1 — Dvigalo s škripcem (konzolni L-nosilci)

![[statika_n1.svg|697]]

> **Besedilo naloge:** Kovinsko dvigalo (nosilci v obliki obrnjene črke L) je togo vpeto v tleh v točki B. Na koncu konzolnega dela (točka A) je pritrjen škripec. Dviguje se tovor mase $m = 20\ \text{kg}$. Višina stebra je $H = 5\ \text{m}$, vodoravna ročica je $a = 2\ \text{m}$. Izračunajte reakcije v vpetju B. ($g = 10\ \text{m/s}^2$)

**Podatki:**
- Tovor: $m = 20\ \text{kg}$, $G = m \cdot g = 200\ \text{N} = 0{,}2\ \text{kN}$
- Geometrija: $H = 5\ \text{m}$, $a = 2\ \text{m}$
- Škripec v točki A

---

### Korak 1 — Sila v vrvi (škripec)

Škripec **samo** spreminja smer sile — ne spreminja njene velikosti!

$$S = G = m \cdot g = 20 \cdot 10 = \boxed{200\ \text{N} = 0{,}2\ \text{kN}}$$

Obe veji vrvi (tovor + fiksna vrv) delujeta navpično navzdol → skupna navpična sila na škripcu:

$$F_{A,y} = 2 \cdot S = 400\ \text{N} = 0{,}4\ \text{kN}$$

> **Zakaj 2S?** Škripec drži dve veji vrvi. Vsaka nese polno silo $S = G$. Skupna sila, ki jo morajo prenesti ležaji škripca, je $2S$.

> **Poenostavitev (BTF izpiti):** Ko naloga navaja le tovor in ne pove kje je fiksirana vrv, pogosto privzamemo samo $F = G = S$ navzdol.

> **glej:** [[Blok 0 - Statika#Ravnovesje 2D]]

---

### Korak 2 — FBD vpetja B

Vpetje prevzame 3 reakcije: $B_x$, $B_y$, $M_B$.

Na točko A deluje sila $F_A = G = 0{,}2\ \text{kN}$ navzdol (poenostavitev: ena veja vrvi).

---

### Korak 3 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad B_x = 0$$

$$\sum F_y = 0 \quad \Rightarrow \quad B_y - G = 0 \quad \Rightarrow \quad \boxed{B_y = 0{,}2\ \text{kN}\ \uparrow}$$

$$\sum M_B = 0 \quad \Rightarrow \quad M_B - G \cdot a = 0$$

$$M_B = G \cdot a = 0{,}2 \cdot 2 = \boxed{0{,}4\ \text{kNm}}$$

---

### Korak 4 — Rezultati

| Reakcija | Vrednost | Smer |
|----------|----------|------|
| $B_x$ | 0 kN | — |
| $B_y$ | 0,2 kN | navzgor ↑ |
| $M_B$ | 0,4 kNm | (vrteče) |

> ⚠️ **Pogosta napaka:** Pozabiti, da škripec deluje na konzolo s TOČKOVNO silo $G$, ne porazdeljeno. Moment v vpetju: $M_B = G \cdot a$ (ročica je vodoravna razdalja od B do točke A, ne višina H!).

> ⚠️ **Napaka 2:** Ne zamešaj H in a pri momentu. $H$ je navpična višina stebra — ne prispeva k momentu vodoravne sile.

---

## NALOGA 2 — Škripec z nagnjeno vrvjo

![[statika_n2.svg|697]]

> **Besedilo naloge:** Isti L-nosilci (A zgoraj, B vpetje), a tokrat vrv na prostem koncu ni fiksirana navpično — teče pod kotom $\alpha = 30°$ glede na navpično. Tovor $m = 50\ \text{kg}$, ročica $a = 1{,}5\ \text{m}$, višina $H = 4\ \text{m}$. Izračunajte reakcije v vpetju B.

**Podatki:**
- $G = 50 \cdot 10 = 500\ \text{N} = 0{,}5\ \text{kN}$
- Vrv pod kotom $\alpha = 30°$ glede na navpično
- $a = 1{,}5\ \text{m}$, $H = 4\ \text{m}$

---

### Korak 1 — Sili v škripcu

Sila v vrvi je povsod enaka: $S = G = 0{,}5\ \text{kN}$.

Navpična veja (tovor): $S_1 = (0;\ -G) = (0;\ -0{,}5)\ \text{kN}$

Poševna veja (pod kotom 30° od navpične):

$$S_{2,x} = S \cdot \sin\alpha = 0{,}5 \cdot \sin 30° = 0{,}5 \cdot 0{,}5 = 0{,}25\ \text{kN}$$

$$S_{2,y} = -S \cdot \cos\alpha = -0{,}5 \cdot \cos 30° = -0{,}5 \cdot 0{,}866 = -0{,}433\ \text{kN}$$

> **Zakaj sin in cos?** Ker je kot $\alpha$ merjen od **navpičnice** (ne od vodoravnice), je vodoravna komponenta $S\sin\alpha$ in navpična $S\cos\alpha$.

> **glej:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

### Korak 2 — Skupna sila na točko A

$$F_{A,x} = S_{2,x} = +0{,}25\ \text{kN} \quad \text{(desno)}$$

$$F_{A,y} = S_{1,y} + S_{2,y} = -0{,}5 - 0{,}433 = -0{,}933\ \text{kN} \quad \text{(navzdol)}$$

---

### Korak 3 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad B_x + F_{A,x} = 0 \quad \Rightarrow \quad \boxed{B_x = -0{,}25\ \text{kN}\ \text{(levo)}}$$

$$\sum F_y = 0 \quad \Rightarrow \quad B_y + F_{A,y} = 0 \quad \Rightarrow \quad \boxed{B_y = +0{,}933\ \text{kN}\ \uparrow}$$

$$\sum M_B = 0 \quad \Rightarrow \quad M_B - F_{A,y} \cdot a - F_{A,x} \cdot H = 0$$

$$M_B = F_{A,y} \cdot a + F_{A,x} \cdot H = 0{,}933 \cdot 1{,}5 + 0{,}25 \cdot 4 = 1{,}4 + 1{,}0 = \boxed{2{,}4\ \text{kNm}}$$

> ⚠️ **Ključno:** Vodoravna komponenta $F_{A,x}$ ima ročico $H$ (navpična višina). Navpična komponenta $F_{A,y}$ ima ročico $a$ (vodoravna razdalja). Ne zamenjaj!

---

### Korak 4 — Rezultati

| Reakcija | Vrednost |
|----------|----------|
| $B_x$ | −0,25 kN (levo) |
| $B_y$ | +0,933 kN (gor) |
| $M_B$ | 2,4 kNm |

---

## NALOGA 3 — Valji v kupu (3+2+1)

![[statika_n3.svg|697]]

> **Besedilo naloge:** Na vodoravnih tleh leži 6 enakih gladkih valjev teže $G = 800\ \text{N}$ vsak, zloženih v piramido (3 spodaj, 2 v sredini, 1 zgoraj). Stene so navpične in gladke. Izračunajte: (a) normalno silo med zgornjim in srednjim valjem, (b) vodoravno silo F, ki jo stene morata prenesti na spodnja zunanja valja.

**Podatki:**
- $G = 800\ \text{N}$ na valj
- Valji so **gladki** → kontaktne sile so vedno **pravokotne na stično točko** (= v smeri med središčema)
- Središča valjev enakih polmerov tvorijo **enakostranični trikotnik** → kot med palicama središč = **60°**

---

### Korak 1 — Geometrija (ključno za razumevanje)

Ko se dva valja enakega polmera $r$ dotikata, je razdalja med njunima središčema $= 2r$. Središča treh valjev (2 spodaj + 1 zgoraj) tvorijo **enakostraničen trikotnik** s kotom 60°.

Smer kontaktne sile med zgornjim in sredinskim valjem je pod kotom $60°$ od navpičnice.

> **Vizualizacija:**
>
> ```
>      ( O )          ← zgornji valj (težišče)
>     /     \
>  60°       60°       ← smer kontaktnih sil N1
>   ( O ) ( O )        ← 2 sredinska valja
> ```

---

### Korak 2 — Analiza ZGORNJEGA valja

Na zgornji valj delujeta:
- $G = 800\ \text{N}$ navzdol
- 2 kontaktni sili $N_1$ (ena levo-dol, ena desno-dol), vsaka pod kotom $30°$ od navpičnice (= $60°$ od vodoravnice)

$$\sum F_y = 0 \quad \Rightarrow \quad 2 \cdot N_1 \cdot \cos 30° = G$$

$$N_1 = \frac{G}{2 \cos 30°} = \frac{800}{2 \cdot 0{,}866} = \frac{800}{1{,}732} = \boxed{462\ \text{N}}$$

> ⚠️ **Zakaj cos30°?** Ker je $N_1$ usmerjena pod **30° od navpičnice** (= 60° od vodoravnice). Njena navpična komponenta je $N_1 \cos30°$.

> **Preveritev kontrole:** $\sum F_x = 0$: $N_1\sin30° - N_1\sin30° = 0$ ✓ (simetrija)

> **glej:** [[Blok 0 - Statika#Ravnovesje v vozlišču]]

---

### Korak 3 — Analiza SREDINSKEGA valja (zunanjega)

Na zunanji sredinski valj delujejo:
- $G = 800\ \text{N}$ navzdol
- $N_1 = 462\ \text{N}$ od zgornjega valja (navzdol pod kotom 30° od navpičnice)
- $N_2$ od notranjega sredinskega valja (vodoravno, desno)
- $N_{tal}$ od tal (navzgor)
- $F$ od stene (vodoravno, noter)

$$\sum F_y = 0: \quad N_{tal} - G - N_1 \cos 30° = 0$$

$$N_{tal} = G + N_1 \cos 30° = 800 + 462 \cdot 0{,}866 = 800 + 400 = \boxed{1200\ \text{N}}$$

$$\sum F_x = 0: \quad F + N_1 \sin 30° - N_2 = 0$$

Za sistem z notranjo simetrijo: $N_2$ prenaša vodoravno silo zgornjega valja na nasprotno stran:

$$F = N_1 \sin 30° - N_2/2 \quad \Rightarrow \quad \text{(iz simetrije celotnega sistema)}$$

Alternativno — globalno ravnovesje celotnega sistema (lažje!):

$$\sum F_x^{cel} = 0: \quad F_{leva\_stena} + F_{desna\_stena} = 0 \quad \text{(ker so vodoravne sile le od sten)}$$

Za zunanji spodnji valj iz $\sum F_x = 0$:

$$\boxed{F = N_1 \sin 30° = 462 \cdot 0{,}5 = 231\ \text{N}}$$

---

### Korak 4 — Rezultati

| Veličina | Vrednost |
|----------|----------|
| Kontaktna sila zgornji–srednji $N_1$ | 462 N |
| Reakcija tal na vsak zunanji spodnji valj | 1200 N |
| Sila stene na zunanji spodnji valj $F$ | **231 N** |

> ⚠️ **Napaka:** Privzeti, da so kotakt. sile navpične. Niso! Valji se dotikajo pod kotom — sile so pravokotne na dotikališče (= skozi središči valjev).

> ⚠️ **Napaka 2:** Pozabiti sešteti vse sile na enega valja (G od teže + N od sosednjega valja, ne samo ena!).

---

## NALOGA 4 — Nagnjena konstrukcija z obremenitvijo pod kotom

![[statika_n4.svg|697]]

> **Besedilo naloge:** Prostoležeči nosilci dolžine $L = 6\ \text{m}$ je podprt v A (nepomični tečaj) in B (pomični valj). Na točki $C$ ($x_C = 4\ \text{m}$ od A) deluje sila $F = 15\ \text{kN}$ pod kotom $\alpha = 40°$ glede na navpičnico. Izračunajte reakcije $A_x$, $A_y$, $B_y$.

**Podatki:**
- Prostoležeč nosilci: A = nepomični tečaj (2 reakciji), B = pomični valj (1 reakcija $B_y$)
- $L = 6\ \text{m}$, $x_C = 4\ \text{m}$
- $F = 15\ \text{kN}$ pod kotom $\alpha = 40°$ od navpičnice

---

### Korak 1 — Razstavi silo F na komponenti

$$F_x = F \cdot \sin\alpha = 15 \cdot \sin 40° = 15 \cdot 0{,}643 = \boxed{9{,}64\ \text{kN}} \quad \text{(vodoravno)}$$

$$F_y = F \cdot \cos\alpha = 15 \cdot \cos 40° = 15 \cdot 0{,}766 = \boxed{11{,}49\ \text{kN}} \quad \text{(navpično navzdol)}$$

> ⚠️ **Ključno:** Ker je $\alpha$ merjen od **navpičnice**, je $F_x = F\sin\alpha$ in $F_y = F\cos\alpha$. Zamenjava je pogosta napaka!
>
> **Pravilo:** Kut od navpičnice → sin = vodoravno, cos = navpično. Kot od vodoravnice → obratno!

> **glej:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

### Korak 2 — Momentna enačba okrog A (direktno $B_y$)

$$\sum M_A = 0: \quad B_y \cdot L - F_y \cdot x_C + F_x \cdot 0 = 0$$

> Opomba: $F_x$ je vodoravna — pri vodoravnem nosilcu nima momenta okrog točke na isti osi (ročica = 0 za vodoravni nosilci brez višine).

$$B_y = \frac{F_y \cdot x_C}{L} = \frac{11{,}49 \cdot 4}{6} = \frac{45{,}96}{6} = \boxed{7{,}66\ \text{kN}\ \uparrow}$$

---

### Korak 3 — Enačbi sil

$$\sum F_y = 0: \quad A_y + B_y - F_y = 0 \quad \Rightarrow \quad A_y = F_y - B_y = 11{,}49 - 7{,}66 = \boxed{3{,}83\ \text{kN}\ \uparrow}$$

$$\sum F_x = 0: \quad A_x - F_x = 0 \quad \Rightarrow \quad \boxed{A_x = 9{,}64\ \text{kN}\ \rightarrow}$$

---

### Korak 4 — Kontrola

$$\sum M_B = 0: \quad -A_y \cdot L + F_y \cdot (L - x_C) - F_x \cdot 0 = -3{,}83 \cdot 6 + 11{,}49 \cdot 2 = -22{,}98 + 22{,}98 = 0 \quad ✓$$

---

### Korak 5 — Rezultati

| Reakcija | Vrednost | Smer |
|----------|----------|------|
| $A_x$ | 9,64 kN | desno → |
| $A_y$ | 3,83 kN | gor ↑ |
| $B_y$ | 7,66 kN | gor ↑ |

> ⚠️ **Pogosta napaka:** Pozabiti $A_x$ — nepomični tečaj ima **dve** reakciji ($A_x$, $A_y$). Pomični valj (B) ima samo $B_y$, ker se horizontalno prosto premika!

---

## NALOGA 5 — Steiner za T-prerez (BTF primer)

![[statika_n5.svg|697]]

> **Besedilo naloge:** Jekleni T-prerez sestavljata: pasnica $b_p = 12\ \text{cm}$, $h_p = 2\ \text{cm}$ (zgoraj) in stojina $b_s = 2\ \text{cm}$, $h_s = 12\ \text{cm}$ (spodaj). Skupna višina $H = 14\ \text{cm}$. Izračunajte: (a) skupno težišče $y_T$ od spodnjega roba, (b) vztrajnostni moment $J$ okrog skupne težiščne osi, (c) odpornostna momenta $W_{sp}$ in $W_{zg}$, (d) kritičen rob.

---

### Korak 1 — Razdelitev na enostavne like

| Del | Lik | $b_i$ | $h_i$ | $A_i$ [cm²] | $y_i$ od spodaj [cm] |
|-----|-----|-------|-------|-------------|----------------------|
| 1 — Stojina | Pravokotnik | 2 | 12 | **24** | 6,0 |
| 2 — Pasnica | Pravokotnik | 12 | 2 | **24** | 13,0 |
| **Skupaj** | | | | **48** | |

---

### Korak 2 — Skupno težišče $y_T$

$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i} = \frac{24 \cdot 6{,}0 + 24 \cdot 13{,}0}{48} = \frac{144 + 312}{48} = \frac{456}{48} = \boxed{9{,}5\ \text{cm od spodaj}}$$

$$e_{sp} = y_T = 9{,}5\ \text{cm} \qquad e_{zg} = H - y_T = 14 - 9{,}5 = 4{,}5\ \text{cm}$$

> **Intuicija:** Težišče je bliže pasnici (zgoraj), ker je pasnica razprostranjena in ima velik ploščinski prispevek pri višjih $y$-koordinatah.

> **glej:** [[Blok 1.5 - Geometrijske Karakteristike#Korak 2 — Skupno težišče]]

---

### Korak 3 — Vztrajnostni moment (Steiner)

$$I = I_0 + A \cdot d^2, \quad d_i = y_i - y_T$$

**Stojina** ($y_1 = 6{,}0$ cm, $d_1 = 6{,}0 - 9{,}5 = -3{,}5$ cm):

$$I_{stoj} = \frac{b_s \cdot h_s^3}{12} + A_s \cdot d_1^2 = \frac{2 \cdot 12^3}{12} + 24 \cdot 3{,}5^2 = 288 + 294 = \boxed{582\ \text{cm}^4}$$

**Pasnica** ($y_2 = 13{,}0$ cm, $d_2 = 13{,}0 - 9{,}5 = +3{,}5$ cm):

$$I_{pas} = \frac{b_p \cdot h_p^3}{12} + A_p \cdot d_2^2 = \frac{12 \cdot 2^3}{12} + 24 \cdot 3{,}5^2 = 8 + 294 = \boxed{302\ \text{cm}^4}$$

$$\boxed{J = I_{stoj} + I_{pas} = 582 + 302 = 884\ \text{cm}^4}$$

> **💡 Steinerjev stavek — fizikalni pomen:** Bolj ko je material oddaljen od skupnega težišča (velik $d$), večji je prispevek $A \cdot d^2$. Zato je T-prerez učinkovit: pasnica je daleč od težišča!

> **siehe:** [[Blok 1.5 - Geometrijske Karakteristike#Steinerjev stavek]]

---

### Korak 4 — Odpornostna momenta

$$W_{sp} = \frac{J}{e_{sp}} = \frac{884}{9{,}5} = \boxed{93{,}1\ \text{cm}^3} \quad \leftarrow \textbf{manjši → kritičen rob!}$$

$$W_{zg} = \frac{J}{e_{zg}} = \frac{884}{4{,}5} = \boxed{196{,}4\ \text{cm}^3}$$

---

### Korak 5 — Zaključek in primerjava

| Rob | $e$ [cm] | $W$ [cm³] | Opomba |
|-----|---------|-----------|--------|
| Spodnji | 9,5 | **93,1** ← manjši | **KRITIČEN!** |
| Zgornji | 4,5 | 196,4 | varnejši |

> ⚠️ **Ključna ugotovitev:** Čeprav je spodnji rob natezni (pri pozitivnem M), je dlje od težišča → večje napetosti! Kritičen rob ≠ nujno natezni rob — odvisno od geometrije!

> ⚠️ **Napaka:** Vzeti samo en $W$ (kot pri kvadratu/krogu). Pri asimetričnih prerezih **VEDNO** preveri oba!

---

## NALOGA 6 — Kombinirana naloga: nagnjena sila + Steiner + uklon

![[statika_n6.svg|697]]

> **Besedilo naloge (BTF tip):** Leseni steber pravokotnega prereza $b = 6\ \text{cm}$, $h = 10\ \text{cm}$ in dolžine $L = 3\ \text{m}$ je na vrhu obremenjen s silo $F = 8\ \text{kN}$ pod kotom $\alpha = 25°$ od navpičnice. Steber je spodaj togo vpet (konzola). Preverite: (a) napetost pri upogibu, (b) ali grozi uklon, (c) varnostni faktor za uklon. ($E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$, $\nu_{zaht} = 3$)

---

### Korak 1 — Razstavi silo F

$$F_N = F \cdot \cos\alpha = 8 \cdot \cos 25° = 8 \cdot 0{,}906 = \boxed{7{,}25\ \text{kN}} \quad \text{(osna tlačna)}$$

$$F_\perp = F \cdot \sin\alpha = 8 \cdot \sin 25° = 8 \cdot 0{,}423 = \boxed{3{,}38\ \text{kN}} \quad \text{(prečna → upogib)}$$

> ⚠️ Ker je $\alpha$ od navpičnice: osna komponenta = $F\cos\alpha$ (navzdol), prečna = $F\sin\alpha$ (vodoravno).

> **glej:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

### Korak 2 — Geometrija prereza (Steiner ni potreben — enostaven pravokotnik)

$$A = b \cdot h = 6 \cdot 10 = 60\ \text{cm}^2$$

$$I_{min} = \frac{h \cdot b^3}{12} = \frac{10 \cdot 6^3}{12} = \frac{2160}{12} = \boxed{180\ \text{cm}^4} \quad \leftarrow \text{šibka os (b je manjši)}$$

$$I_{max} = \frac{b \cdot h^3}{12} = \frac{6 \cdot 10^3}{12} = 500\ \text{cm}^4$$

$$W = \frac{b \cdot h^2}{6} = \frac{6 \cdot 10^2}{6} = 100\ \text{cm}^3 \quad \text{(os uklona)}$$

> ⚠️ **Uklon nastopi vedno po šibki osi** → vzamemo $I_{min}$!

> **siehe:** [[Blok 1.5 - Geometrijske Karakteristike#Imin za uklon]]

---

### Korak 3 — Upogib od prečne sile

Konzolni nosilci z vodoravno silo na vrhu → $M_{max}$ pri vpetju:

$$M_{max} = F_\perp \cdot L = 3{,}38 \cdot 300\ \text{cm} = \boxed{1014\ \text{kNcm}}$$

$$\sigma_M = \frac{M_{max}}{W} = \frac{1014}{100} = \boxed{10{,}14\ \text{kN/cm}^2}$$

Osna tlačna napetost:

$$\sigma_N = \frac{F_N}{A} = \frac{7{,}25}{60} = \boxed{0{,}121\ \text{kN/cm}^2}$$

Skupna napetost (superponiranje):

$$\sigma_{max} = \sigma_M + \sigma_N = 10{,}14 + 0{,}121 = \boxed{10{,}26\ \text{kN/cm}^2}$$

> Dopustna napetost: $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$ → $10{,}26 \gg 1{,}2$ → **PREKORAČENO!**

> ⚠️ **Komentar:** V praksi bi prerez dimenzionirali iz tega pogoja. Za namen naloge nadaljujemo z uklonom.

---

### Korak 4 — Euler uklon

Konzola: $\beta = 2$, $l_u = \beta \cdot L = 2 \cdot 300 = 600\ \text{cm}$

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2} = \frac{9{,}8696 \cdot 1000 \cdot 180}{600^2} = \frac{1{,}776 \cdot 10^6}{360\,000} = \boxed{4{,}93\ \text{kN}}$$

> **zobacz:** [[Blok 4 - Euler Uklon#Korak 4 — Fk]]

---

### Korak 5 — Vitkost in preveritev Eulerjevega območja

$$i_{min} = \sqrt{\frac{I_{min}}{A}} = \sqrt{\frac{180}{60}} = \sqrt{3} = 1{,}732\ \text{cm}$$

$$\lambda = \frac{l_u}{i_{min}} = \frac{600}{1{,}732} = \boxed{346}$$

$$\lambda_e = \pi \sqrt{\frac{E}{\sigma_{dop}}} = \pi \sqrt{\frac{1000}{1{,}2}} = 90{,}7$$

$$\lambda = 346 > \lambda_e = 90{,}7 \quad \Rightarrow \quad \textbf{Eulerova formula velja ✓}$$

---

### Korak 6 — Varnostni faktor

$$\nu = \frac{F_k}{F_N} = \frac{4{,}93}{7{,}25} = \boxed{0{,}68}$$

$$\nu = 0{,}68 < \nu_{zaht} = 3 \quad \Rightarrow \quad \textbf{❌ UKLON GROZI! Prerez je podhranjen.}$$

---

### Korak 7 — Zaključna tabela

| Kontrola | Vrednost | Dopustno | Ocena |
|----------|----------|----------|-------|
| $\sigma_{max}$ (upogib) | 10,26 kN/cm² | 1,2 kN/cm² | ❌ |
| $\nu_{uklon}$ | 0,68 | ≥ 3 | ❌ |

> **Zaključek:** Prerez $6 \times 10$ cm je bistveno premajhen za te obremenitve pri dolžini $L = 3\ \text{m}$. Potrebno povečanje prereza ali krajšanje stebra.

---

## Povzetek formul — izpit na hitro

### Škripec

$$S = G = m \cdot g \quad \text{(sila v vrvi = teža tovora)}$$

Obe veji vrvi → skupna sila na škripec = $2S$ (v enakem smeri)

Nagnjeni vrv pod kotom $\alpha$ od navpičnice: $S_x = S\sin\alpha$, $S_y = S\cos\alpha$

### Valji v kupu (enakostranični trikotnik)

$$N_1 \text{ od stika:} \quad 2N_1 \cos 30° = G \quad \Rightarrow \quad N_1 = \frac{G}{2\cos 30°} = \frac{G}{\sqrt{3}}$$

$$F_{stene} = N_1 \sin 30° = \frac{G}{2\sqrt{3}} = \frac{G\sqrt{3}}{6}$$

### Sila pod kotom $\alpha$ (od navpičnice)

| Merimo kot od... | Vodoravna | Navpična |
|-----------------|-----------|----------|
| Navpičnice | $F\sin\alpha$ | $F\cos\alpha$ |
| Vodoravnice | $F\cos\alpha$ | $F\sin\alpha$ |

> ⚠️ **Zapomni:** Od navpičnice → sin je vodoravna!

### Steiner — postopek v korakih

$$y_T = \frac{\sum A_i y_i}{\sum A_i}$$

$$J = \sum\left(\frac{b_i h_i^3}{12} + A_i \cdot d_i^2\right), \quad d_i = y_i - y_T$$

$$W_{sp} = \frac{J}{e_{sp}} = \frac{J}{y_T}, \quad W_{zg} = \frac{J}{H - y_T}$$

**Kritičen je MANJŠI W!**

### Konzolni steber z nagnjeno silo (kombinirana naloga)

1. Razstavi $F$ → $F_N = F\cos\alpha$ (osna), $F_\perp = F\sin\alpha$ (prečna)
2. Upogibni moment: $M = F_\perp \cdot L$ pri vpetju
3. $\sigma = M/W + F_N/A$ (superponiranje)
4. Uklon: $l_u = 2L$ (konzola), $F_k = \pi^2 E I_{min}/l_u^2$
5. $\nu = F_k / F_N \geq \nu_{zaht}$

---

## Povezave

- [[Blok 0 - Statika]] ← enačbe ravnovesja, vrste podpor
- [[Blok 1.5 - Geometrijske Karakteristike]] ← Steiner, I, W tabela
- [[Blok 2 - Upogib]] ← σ iz upogibnega momenta
- [[Blok 4 - Euler Uklon]] ← Fk, λ, β vrednosti
- [[Vaje - Trdnost in dimenzioniranje]] ← N2 (Euler konzola), N3 (T-prerez), N4 (N+M)
- [[Vaje - NTM diagrami - Vse vrste]] ← NTM diagrami pred napetostmi
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]

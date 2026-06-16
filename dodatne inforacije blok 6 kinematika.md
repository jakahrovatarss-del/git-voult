Za reševanje nalog iz poglavja **Kinematika (Blok 6)**, ki obravnava gibanje teles brez upoštevanja sil, so na podlagi vaših virov ključne naslednje enačbe in koncepti:

### 1. Premo in krožno gibanje (Osnove)

Pri gibanju točke ali telesa, kjer sta podani funkciji poti $s(t)$ in kota $\phi(t)$, uporabljamo odvode po času:

- **Hitrost:** $v = \dot{s} = \frac{ds}{dt}$.
- **Pospešek:** $a = \ddot{s} = \frac{dv}{dt}$.
- **Kotna hitrost:** $\omega = \dot{\phi} = \frac{d\phi}{dt}$.
- **Kotni pospešek:** $\alpha = \ddot{\phi} = \frac{d\omega}{dt}$.
- **Povezava med frekvenco (vrtljaji) in $\omega$:** $\omega = \frac{2\pi \cdot n}{60}$, kjer je $n$ število obratov na minuto.

### 2. Kinematika točke na rotirajočem telesu

Če točka kroži okoli fiksnega središča na razdalji $r$:

- **Obodna hitrost:** $v = \omega \cdot r$.
- **Tangencialni pospešek:** $a_t = \alpha \cdot r$.
- **Normalni (centripetalni) pospešek:** $a_n = \omega^2 \cdot r$.
- **Skupni pospešek:** $a = \sqrt{a_t^2 + a_n^2}$.

### 3. Sestavljeno gibanje (Relativno in absolutno gibanje)

Pri nalogah, kjer se telo giblje znotraj sistema, ki se prav tako giblje (npr. drsnik na rotirajoči palici), uporabljamo vektorsko seštevanje:

- **Absolutna hitrost ($\vec{v}_a$):** $\vec{v}_a = \vec{v}_r + \vec{v}_s$.
    - $v_r$: relativna hitrost (gibanje točke glede na sistem).
    - $v_s$: sistemska (transportna) hitrost (gibanje točke, kot da bi bila fiksirana na sistemu).
- **Absolutni pospešek ($\vec{a}_a$):** $\vec{a}_a = \vec{a}_r + \vec{a}_s + \vec{a}_c$.
    - $a_r$: relativni pospešek.
    - $a_s$: sistemski pospešek (vsebuje tangencialno in normalno komponento sistema).
    - **Coriolisov pospešek ($a_c$):** $a_c = 2 \cdot \omega_s \cdot v_r \cdot \sin \gamma$. Ta komponenta se pojavi le, če se sistem vrti ($\omega_s \neq 0$) in se točka relativno premika ($v_r \neq 0$).

### 4. Analiza mehanizmov in "Lega pola"

Za določanje hitrosti v mehanizmih (npr. drogova, ki sta povezana) pogosto uporabljamo metodo **trenutnega središča vrtenja (pola)**:

- **Iskanje pola ($P$):** Pol je točka, okoli katere se telo v danem trenutku vrti le čisto rotacijsko. Nahaja se v presečišču normal na vektorje hitrosti dveh točk telesa.
- **Izračun kotne hitrosti člena:** $\omega = \frac{v_B}{BP} = \frac{v_C}{CP}$, kjer sta $BP$ in $CP$ razdalji od točk do pola.
- **Vektorska metoda:** Hitrost točke na členu lahko izračunamo tudi z uporabo znanih hitrosti drugih točk: $\vec{v}_C = \vec{v}_B + \vec{\omega} \times \vec{r}_{BC}$.

### 5. Tipičen postopek reševanja nalog:

1. **Analizirajte tip gibanja:** Ali gre za čisto translacijo, čisto rotacijo ali splošno ravninsko gibanje.
2. **Zapišite znane kinematične funkcije:** Če sta podani $s(t)$ ali $\phi(t)$, ju odvajajte za hitrosti in pospeške.
3. **Določite smeri hitrosti:** Hitrost je vedno tangencialna na pot gibanja.
4. **Uporabite metodo pola ali vektorsko seštevanje:** Če iščete kotno hitrost vmesnega člena, poiščite njegov pol ali uporabite zvezo $v_a = v_r + v_s$.
5. **Pazite na komponente pospeška:** Pri rotacijah ne pozabite na normalno komponento ($\omega^2 r$), pri sestavljenih gibanjih pa na Coriolisov pospešek.

 
 Pozdravljeni, kolega študent! Kot vaš profesor na lesarski fakulteti vas danes vabim v svet **kinematike (Blok 6)**. Pri statiki in trdnosti smo se ukvarjali s tem, da stvari _mirujejo_ ali pa se le malenkostno _deformirajo_. Pri kinematiki pa nas zanima **gibanje** – kako se gibljejo rezila skobeljnih strojev, kako potuje deblo skozi žago in kako se vrtijo svedri.

V kinematiki opisujemo gibanje (položaj, hitrost, pospešek) čisto geometrijsko, ne da bi nas zanimalo, katere sile so to gibanje povzročile.

Tukaj je vaš celovit pregled vseh enačb in konceptov, ki jih potrebujete za reševanje nalog.

---

### 1. Kinematika točke (Temeljne veličine)

Vse se začne pri spremljanju ene same materialne točke v času $t$.

- **Vektor položaja ($\vec{r}$):** Določa, kje se točka nahaja v prostoru.
- **Hitrost ($\vec{v}$):** Odvod položaja po času. $$\vec{v} = \frac{d\vec{r}}{dt} = \dot{\vec{r}}$$
- **Pospešek ($\vec{a}$):** Odvod hitrosti po času. $$\vec{a} = \frac{d\vec{v}}{dt} = \ddot{\vec{r}}$$

> **Skica za intuicijo:** _Narišite krivuljo (tirnico). V določeni točki narišite vektor položaja $\vec{r}$ iz izhodišča. Vektor hitrosti $\vec{v}$ pa narišite tako, da je vedno **tangenta** na tirnico._

---

### 2. Naravni koordinatni sistem ($t, n, b$)

To je najpomembnejši sistem za naloge, kjer se točka giblje po znani krivulji (npr. po krožnici ali elipsi).

- **Hitrost:** Vedno kaže v smeri tangente ($t$): $$v = \dot{s}$$ (kjer je $s$ pot po tirnici).
- **Pospešek:** Sestavljen je iz dveh komponent: $$\vec{a} = \vec{a}_t + \vec{a}_n$$
    - **Tangencialni pospešek ($a_t$):** Pove, kako se spreminja _velikost_ hitrosti (ali stroj pospešuje/bremza). $$a_t = \dot{v} = \ddot{s}$$
    - **Normalni (radialni) pospešek ($a_n$):** Pove, kako se spreminja _smer_ hitrosti. Vedno kaže proti središču ukrivljenosti. $$a_n = \frac{v^2}{\rho}$$ ($\rho$ je krivinski radij – pri krožnici je to polmer $R$).

---

### 3. Kroženje (Ključno za lesnoobdelovalna orodja)

Pri rezkarjih in žagah je kroženje osnova.

- **Kot zasuka ($\varphi$):** Merimo ga v radianih.
- **Kotna hitrost ($\omega$):** Koliko radijanov prepotuje točka v eni sekundi. $$\omega = \dot{\varphi} = \frac{2\pi \cdot n}{60}$$ (kjer je $n$ število vrtljajev na minuto).
- **Kotni pospešek ($\alpha$):** $$\alpha = \dot{\omega} = \ddot{\varphi}$$
- **Povezava s tangencialnimi veličinami:** $$v = \omega \cdot R$$ $$a_t = \alpha \cdot R$$ $$a_n = \omega^2 \cdot R$$

---

### 4. Kinematika togega telesa (Planarno gibanje)

Togo telo je sistem točk, ki med seboj ne spreminjajo razdalje. V lesarstvu to pomeni npr. celoten list krožne žage ali vzvod v mehanizmu stola.

#### A) Enačba za hitrost dveh točk na telesu

Če poznamo hitrost točke $A$ in kotno hitrost telesa $\omega$, lahko izračunamo hitrost katerekoli druge točke $B$: $$\vec{v}_B = \vec{v}_A + \vec{\omega} \times \vec{r}_{AB}$$

#### B) Pol hitrosti (Trenutno središče vrtenja)

To je magična točka $P$, ki ima v danem trenutku hitrost 0 ($v_p = 0$). Vsako kompleksno gibanje (translacija + rotacija) lahko v enem trenutku gledamo kot **čisto rotacijo okoli pola hitrosti**.

- **Kako ga najdemo?** Če poznamo smeri hitrosti dveh točk ($v_A$ in $v_B$), pol hitrosti leži v sečišču pravokotnic na ti dve hitrosti.
- **Uporaba:** Ko imate pol $P$, so hitrosti vseh točk preprosto $v_i = \omega \cdot r_{Pi}$.

---

### 5. Sestavljeno gibanje (Absolutno in relativno)

Predstavljajte si, da hodite po premikajočem se traku v žagi. Vaše gibanje je sestavljeno.

- **Absolutna hitrost:** $$\vec{v}_{abs} = \vec{v}_{rel} + \vec{v}_{tran}$$
    - $v_{rel}$: Vaša hitrost glede na trak.
    - $v_{tran}$: Hitrost traku glede na tla.
- **Absolutni pospešek:** $$\vec{a}_{abs} = \vec{a}_{rel} + \vec{a}_{tran} + \vec{a}_{Cor}$$
    - **Coriolisov pospešek ($a_{Cor}$):** Pojavi se le, če se vaš "sistem" (trak) vrti in se vi po njem premikate. $$\vec{a}_{Cor} = 2 \vec{\omega} \times \vec{v}_{rel}$$

---

### Profesorjev nasvet za vaje iz kinematike:

1. **Vedno začnite s skico tirnice!** Označite, kje je središče vrtenja in kam kažejo vektorji.
2. **Pazite na enote!** Kotno hitrost $\omega$ morate imeti v $rad/s$, ne v vrtljajih na minuto ($n$), preden jo vstavite v enačbe za $v$ in $a$.
3. **Metoda pola hitrosti:** To je najhitrejša pot do rešitve pri mehanizmih (npr. pri nalogah z vzvodi). Če najdete pol $P$, ste rešili 80 % naloge.
4. **Deriviranje:** Če imate podano enačbo poti $s(t)$ ali kota $\varphi(t)$, je rešitev le v spretnem odvajanju.

S temi enačbami ste pripravljeni na vse izzive, ki jih prinaša gibanje v mehaniki. Če boste reševali kakšen konkreten mehanizem za lesnoobdelovalni stroj, mi ga pokažite in ga bova skupaj "zavrtela"!
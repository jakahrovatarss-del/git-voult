
Za reševanje nalog iz poglavja **Eulerjev uklon (Blok 4)** so ključne naslednje enačbe in koncepti, ki temeljijo na informacijah iz virov:

### 1. Osnovna Eulerjeva enačba za kritično silo

Kritična uklonska sila ($F_k$ ali $F_{krit}$) je tista sila, pri kateri palica izgubi stabilnost in se upogne. Izračunamo jo po formuli: **$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{(\beta \cdot L)^2}$$**

Pri tem so:

- **$E$**: modul elastičnosti materiala (npr. za les $E = 1000 , \text{kN/cm}^2$).
- **$I_{min}$ (ali $J_{min}$)**: minimalni vztrajnostni moment prečnega prereza. Uklon se vedno zgodi okoli osi z najmanjšim vztrajnostnim momentom.
- **$L$**: dejanska dolžina palice oziroma stebra.
- **$\beta$**: faktor načina vpetja, ki določa "efektivno dolžino" palice ($\ell_0 = \beta \cdot L$):
    - **$\beta = 2$**: ena stran togo vpeta, druga prosta (konzolni steber).
    - **$\beta = 1$**: obe strani členkasto podprti.
    - **$\beta = 0,7$**: ena stran vpeta, druga členkasto podprta.
    - **$\beta = 0,5$**: obe strani togo vpeti.

### 2. Geometrijske lastnosti prereza

Za izračun uklona potrebujete osnovne podatke o prerezu:

- **Površina ($A$)**: npr. za pravokotnik $A = b \cdot h$.
- **Minimalni vztrajnostni polmer ($i$ oziroma $i_{min}$)**: $$i = \sqrt{\frac{I_{min}}{A}}$$
- **Vztrajnostni moment za pravokotnik**: $I = \frac{b \cdot h^3}{12}$.

### 3. Vitkost palice ($\lambda$)

Vitkost nam pove, kako "suha" je palica in ali je Eulerjeva formula sploh veljavna: **$$\lambda = \frac{\beta \cdot L}{i}$$**

Eulerjeva formula velja le za **dolge in vitke palice**, kjer je vitkost $\lambda$ večja od mejne vitkosti materiala ($\lambda_0$). Če je palica manj vitka, se uporablja **Tetmajerjeva formula** ali **$\omega$-postopek**.

### 4. Varnost in dopustna sila

V praksi ne dopustimo, da sila doseže kritično vrednost, zato uporabljamo varnostni faktor ($\nu$):

- **Uklonska varnost ($\nu$)**: $\nu = \frac{F_{krit}}{F_{dejanski}}$.
- **Dopustna sila ($F_{dop}$)**: $F_{dop} = \frac{F_k}{\nu}$.

### 5. $\omega$-postopek ($w$-postopek)

Pri tem postopku s pomočjo vitkosti $\lambda$ iz tabel odčitamo faktor $\omega$, ki poveča dejansko napetost zaradi nevarnosti uklona: **$$\sigma = \omega \cdot \frac{F}{A} \leq \sigma_{dop}$$** oziroma **$$F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega}$$**

### Tipičen postopek reševanja nalog:

1. **Določite geometrijo**: Izračunajte $A$, $I_{min}$ in $i_{min}$ za dani prerez.
2. **Določite robne pogoje**: Izberite ustrezen $\beta$ glede na vpetje.
3. **Preverite vitkost**: Izračunajte $\lambda$. Če je v nalogi zahtevan Euler, nadaljujte neposredno s formulo za $F_k$.
4. **Izračunajte kritično silo**: Uporabite Eulerjevo formulo.
5. **Preverite varnost ali določite dopustno silo**: Upoštevajte predpisani varnostni faktor (pogosto $\nu = 3$).
Pozdravljeni, kolega študent! Danes se bomo kot pravi lesarji posvetili eni najpomembnejših tem pri načrtovanju visokih konstrukcij, kot so leseni stebri v ostrešjih ali podporniki v dvoranah. Govorili bomo o **Eulerjevem uklonu (Blok 4)**.

Uklon je specifičen problem stabilnosti. Za razliko od navadnega tlaka, kjer se material preprosto zdrobi, se pri uklonu vitek element (palica) nenadno upogne v stran. Predstavljajte si tanko leseno letvico: če nanjo pritisnete z vrha, bo "skočila" v stran še preden se bo les dejansko poškodoval zaradi pritiska.

Tukaj je vse, kar potrebujete za reševanje nalog.

---

### 1. Osrednja enačba: Eulerjeva kritična sila ($F_{krit}$)

To je sila, pri kateri palica izgubi stabilnost in se ukloni. Izračunamo jo po formuli:

$$F_{krit} = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2}$$

**Pomen oznak:**

- **$E$ (Modul elastičnosti):** Za les običajno vzamemo $E \approx 10.000 , \text{MPa}$ (oziroma $1.000 , \text{kN/cm}^2$).
- **$I_{min}$ (Minimalni vztrajnostni moment):** Palica se bo vedno uklonila v smeri svoje najšibkejše osi. Če imate pravokotni prerez $b \times h$, izračunate oba vztrajnostna momenta ($I_y$ in $I_z$) in vzamete manjšega.
- **$l_u$ (Uklonska dolžina):** To je dejanska dolžina "polvala" sinusoide, ki jo tvori deformirana palica.

---

### 2. Uklonska dolžina ($l_u$) in koeficient $\beta$

Uklonska dolžina je odvisna od tega, kako je palica vpeta na koncih. Izračunamo jo kot: $$l_u = \beta \cdot L$$

**Štirje osnovni primeri (viri podajajo skice):**

1. **Oba konca členkovita (△—△):** $\beta = 1 \implies l_u = L$
2. **Spodaj vpeto, zgoraj prosto (🧱—⎯):** $\beta = 2 \implies l_u = 2L$ (npr. visok jambor ali steber, ki zgoraj ni povezan).
3. **Spodaj vpeto, zgoraj členkovito (🧱—△):** $\beta = 0,7 \implies l_u = 0,7L$
4. **Oba konca vpeta (🧱—🧱):** $\beta = 0,5 \implies l_u = 0,5L$

> **Profesorjev nasvet:** Pri 3D problemih (npr. pravokotni steber) se lahko zgodi, da je v smeri $y$ steber vpet drugače kot v smeri $z$. Takrat morate preveriti uklon za obe smeri posebej!

---

### 3. Vitkost palice ($\lambda$) in polmer vztrajnosti ($i$)

Da ugotovimo, ali je palica sploh "umna" za Eulerjev izračun, moramo poznati njeno **vitkost**: $$\lambda = \frac{l_u}{i_{min}}$$

Kjer je **vztrajnostni radij ($i$)**: $$i = \sqrt{\frac{I}{A}}$$ ($A$ je površina prereza).

---

### 4. Meje veljavnosti: Euler vs. Tetmajer

Eulerjeva enačba velja le za zelo vitke palice, kjer je material še v elastičnem območju.

- **Mejna vitkost za les ($\lambda_{Euler}$)** je približno **100**.

**Pravilo za izbiro enačbe:**

1. Če je **$\lambda > 100$**: Uporabimo **Eulerja** (elastični uklon). $$\sigma_{krit} = \frac{\pi^2 \cdot E}{\lambda^2}$$
2. Če je **$\lambda < 100$**: Uporabimo **Tetmajerjevo** izkustveno enačbo (neelastični uklon).
    - Za les velja: $\sigma_{krit} = 29,3 - 0,194 \cdot \lambda$ (v MPa).
3. Če je **$\lambda < 20$**: Uklona sploh ni, računamo le čisti tlak ($\sigma = F/A$).

---

### 5. Varnost in dopustna sila ($F_{dop}$)

Konstrukcije ne smemo obremeniti do same meje porušitve. Uporabimo **uklonski koeficient varnosti ($\nu_{ukl}$)**, ki je za les običajno med 3 in 10.

$$F_{dop} = \frac{F_{krit}}{\nu_{ukl}}$$ Pogoj trdnosti: $$F_{dejanska} \leq F_{dop}$$

---

### Grafični postopek reševanja (Vaš "Check-list" za izpit)

1. **Določi geometrijo:** Izračunaj $A$ in $I_{min}$.
2. **Določi uklonsko dolžino:** Glede na podpore izberi $\beta$ in izračunaj $l_u = \beta \cdot L$.
3. **Izračunaj vitkost:** $\lambda = l_u / \sqrt{I/A}$.
4. **Preveri območje:** Ali je $\lambda$ večji ali manjši od 100?
5. **Izračunaj $F_{krit}$:** Uporabi Eulerja (če $\lambda > 100$) ali Tetmajerja (če $\lambda < 100$).
6. **Upoštevaj varnost:** Deli s faktorjem $\nu$ in preveri, če steber zdrži.

**Skica za intuicijo:** Narišite stebrič in nanj narišite navpično silo. Če je steber tanek in dolg, ob sili narišite črtkano sinusoido, ki kaže, kako se steber izboči v stran – to je vizualni prikaz uklona.

Upam, da vam bodo te enačbe pomagale pri vajah. Če boste reševali kakšen lesen podpornik in se vam upre vitkost, sem tukaj za dodatno razlago!
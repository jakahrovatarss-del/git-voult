Za uspešno reševanje nalog iz poglavja **Torzija (Blok 5)**, ki obravnava obremenitve gredi in nosilcev na zasuk, morate poznati naslednje ključne enačbe in postopke, povzete iz vaših virov:

### 1. Notranji torzijski moment ($M_t$)

Prvi korak pri vsaki nalogi je določitev **torzijskega momenta**, ki deluje v prerezu.

- **Izračun momenta:** Torzijski moment je enak vsoti vseh zunanjih momentov (navorov), ki delujejo okoli vzdolžne osi nosilca: $M_t = \sum (F_i \cdot r_i)$.
- **Diagram $M_t$:** Pri nosilcih z več obremenitvami je treba narisati diagram poteka notranjega torzijskega momenta vzdolž osi $x$, da določite **maksimalni torzijski moment ($M_t^{max}$)**, ki je ključen za dimenzioniranje.

### 2. Strižna napetost zaradi torzije ($\tau$)

Torzija v prerezu povzroča **strižne napetosti**. Za izračun maksimalne napetosti uporabljamo formulo: **$$\tau_{max} = \frac{M_t}{W_t}$$** kjer je:

- **$\tau_{max}$**: največja strižna napetost v prerezu.
- **$M_t$**: torzijski moment v obravnavanem prerezu.
- **$W_t$**: torzijski odpornostni moment prereza.

### 3. Torzijski odpornostni moment ($W_t$)

Izračun $W_t$ je močno odvisen od oblike prečnega prereza. Viri se osredotočajo predvsem na **tankostenske zaprte prereze** (npr. votli pravokotniki, trikotniki):

- **Splošna formula za tankostenske zaprte prereze:** **$$W_t = (A_{zun} + A_{notr}) \cdot t_{min}$$**.
    - **$A_{zun}$**: Površina, ki jo oklepa zunanji rob prereza.
    - **$A_{notr}$**: Površina, ki jo oklepa notranji rob prereza.
    - **$t_{min}$**: Minimalna debelina stene prereza.
- **Primer trikotnega prereza:** Za votel enakostranični trikotnik s stranico $a$ se površina izračuna kot $A = \frac{a \cdot v}{2}$, nato pa se upošteva zunanja in notranja površina glede na debelino stene.

### 4. Pogoj trdnosti in dimenzioniranje

Pri preverjanju varnosti ali določanju dimenzij nosilca (npr. parametra $c$ ali debeline stene) mora veljati, da dejanska napetost ne preseže **dopustne strižne napetosti ($\tau_{dop}$)**: **$$\tau_{max} \leq \tau_{dop}$$**. Iz tega pogoja lahko izpeljemo minimalni potrebni $W_t$ ali dimenzije prereza: **$$W_{t, min} = \frac{M_t^{max}}{\tau_{dop}}$$**.

### 5. Deformacija pri torziji – zasuk ($\phi$)

Poleg napetosti je včasih treba izračunati tudi **kot zasuka** prostega konca nosilca:

- Zasuk ($\phi$) je odvisen od dolžine nosilca ($L$), torzijskega momenta ($M_t$), strižnega modula materiala ($G$) in torzijskega vztrajnostnega momenta ($I_t$ ali $J_t$).
- Viri navajajo uporabo strižnega modula $G$ za materiale, kot sta jeklo ali les (npr. za jeklo $G = 80$ GPa, za les so vrednosti nižje).

### Pomembni koraki pri reševanju:

1. **Analiza obremenitev:** Določite vse zunanje sile in njihove ročice glede na os zasuka.
2. **Določitev $M_t$:** Izračunajte reakcijo v vpetju in narišite diagram torzijskih momentov.
3. **Geometrija prereza:** Natančno izračunajte površine ($A_{zun}$, $A_{notr}$) in določite $t_{min}$.
4. **Izračun napetosti:** Uporabite $\tau = M_t / W_t$ in primerjajte z dopustno vrednostjo.
5. **Pazite na enote:** Vedno preračunajte enote tako, da so usklajene (npr. kN in cm v kNm in cm² ali N in mm v Nm in mm²).
6. Pozdravljeni, kolega študent! Kot vaš profesor na lesarski fakulteti vas danes vabim v svet **torzije (vzvoja)**. To je tisto poglavje v mehaniki, ki nam razloži, kako se gredi v lesnoobdelovalnih strojih ali stebla rezkarjev upirajo "zasuku", ko zarežejo v trd les.

Pri torziji ne govorimo o upogibanju navzdol, temveč o relativnem zasuku prečnih prerezov okoli vzdolžne osi palice. Tukaj so vse enačbe in koncepti, ki jih boste potrebovali pri "Bloku 5".

---

### 1. Osnovna intuicija in navor ($M_t$)

Predstavljajte si, da z rokama ožemate mokro brisačo – to je čista torzija. V mehaniki torzijski moment ($M_t$) povzroči sila $F$, ki deluje na ročici $a$: $$M_t = F \cdot a$$

**Profesorjev namig:** Pri rezkarjih je ta ročica polmer rezkarja ($r$), sila pa je tista, ki jo les izvaja na rezilo.

---

### 2. Neovirana torzija okroglih prerezov (Polni in votli)

To je najpogostejši primer pri gredah. Napetosti v prerezu so **strižne napetosti ($\tau$)**.

#### A) Porazdelitev napetosti

Strižna napetost v poljubni točki na razdalji $r$ od središča je: $$\tau = G \cdot r \cdot \vartheta$$ Kjer je:

- **$G$**: Strižni modul materiala (za jeklo $\approx 80.000$ MPa, za les je precej nižji in odvisen od smeri vlaken).
- **$\vartheta$**: Specifični kot zasuka (zasuk na enoto dolžine).

#### B) Največja napetost ($\tau_{max}$)

Največja napetost je vedno na **zunanjem obodu** ($r = R$): $$\tau_{max} = \frac{M_t}{I_p} \cdot R = \frac{M_t}{W_t}$$

> **Grafični prikaz napetosti:** _Narišite krog (prerez gredi). V središču je napetost 0. Od središča proti robu napetost linearno raste. Na robu narišite najdaljše puščice, ki so tangencialne na obod krožnice._

#### C) Geometrijske lastnosti (Za okrogel prerez premera $d$)

- **Polarni vztrajnostni moment ($I_p$):** $I_p = \frac{\pi \cdot d^4}{32}$
- **Torzijski odpornostni moment ($W_t$):** $W_t = \frac{\pi \cdot d^3}{16}$

---

### 3. Deformacija: Kot zasuka ($\varphi$)

Če želite vedeti, za koliko stopinj se bo zasukal konec palice dolžine $L$: $$\varphi = \frac{M_t \cdot L}{G \cdot I_p}$$ _Rezultat dobite v radianih ($1 , \text{rad} \approx 57,3^\circ$)_.

---

### 4. Torzija neokroglih prerezov (Posebni primeri)

Pri lesarstvu pogosto srečamo pravokotne nosilce. Tu krožna simetrija ne velja več!

- **Pravokotni prerez ($b \times h$):** Uporabljamo koeficiente $C_1$ in $C_2$, ki jih razberemo iz tabel glede na razmerje $h/b$. $$\tau_{max} = \frac{M_t}{C_1 \cdot b^2 \cdot h}$$ $$\varphi = \frac{M_t \cdot L}{C_2 \cdot b^3 \cdot h \cdot G}$$
- **Tankostenski zaprti prerezi (Bredtova enačba):** Če imate votlo cev poljubne oblike z debelino stene $t$: $$\tau = \frac{M_t}{2 \cdot A_{sred} \cdot t}$$ _($A_{sred}$ je površina, ki jo oklepa središčna linija stene)_.
- **Odprti tankostenski prerezi (U-profil, L-profil):** Ti so na torzijo zelo šibki! $$W_t \approx \frac{1}{3} \sum (h_i \cdot t_i^3)$$

---

### 5. Glavne napetosti in superpozicija

Ko palico zvijate, se v materialu pojavijo tudi natezne in tlačne napetosti pod kotom **45 stopinj**.

- **Mohrova krožnica za čisto torzijo:** Središče je v koordinatnem izhodišču, glavni napetosti pa sta $\sigma_1 = \tau$ in $\sigma_2 = -\tau$.

Če imate hkrati **torzijo in upogib** (npr. pri rezkarju), izračunamo ekvivalentno napetost po von Misesu: $$\sigma_{ekv} = \sqrt{\sigma_{upogib}^2 + 3 \cdot \tau_{torzija}^2}$$

---

### Profesorjev nasvet za vaje:

1. **Preverite enote!** Momenti so pogosto v $kNm$ ali $Nmm$, vztrajnostni momenti pa v $cm^4$ ali $mm^4$. Vedno vse pretvorite v $N$ in $mm$ (rezultat bo v MPa).
2. **Identificirajte prerez:** Ali je gred polna, votla ali morda pravokotna?.
3. **Skicirajte NTM diagrame:** Torzijski moment $M_t$ se lahko vzdolž gredi spreminja, če je nanjo nasajenih več jermenic.

Če boste reševali nalogo z rezkarjem ali gredjo s poševnim ozobljenjem, kjer se torzija meša z osnimi silami, si pomagajte s principom superpozicije, ki smo ga obravnavali pri prejšnjih blokih. Srečno!
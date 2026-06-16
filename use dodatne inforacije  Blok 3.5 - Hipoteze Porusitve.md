Za uspešno reševanje nalog iz poglavja **Hipoteze porušitve (Blok 3.5)**, kjer določamo **ekvivalentno napetost** ($\sigma_{ekv}$), morate poznati naslednje enačbe in koncepte, ki izhajajo neposredno iz vaših virov:

### 1. Osnovni koncept ekvivalentne napetosti

Ekvivalentna napetost nam omogoča, da zapleteno večosno napetostno stanje primerjamo z enoosnim preizkusom (npr. nateznim testom). Konstrukcija je **varna**, če velja: $$\sigma_{ekv} \leq \sigma_{dop}$$ Pri čemer je $\sigma_{dop}$ dopustna napetost materiala.

### 2. Izračun glavnih napetosti ($\sigma_1, \sigma_2, \sigma_3$)

Preden lahko uporabite hipoteze porušitve, morate poznati **glavne napetosti**. Te dobite iz podanega napetostnega tenzorja $\sigma_{ij}$ z reševanjem karakteristične enačbe (iskanje lastnih vrednosti): $$\det(\sigma_{ij} - \sigma \cdot \delta_{ij}) = 0$$

Če imate ravninsko napetostno stanje ($\sigma_x, \sigma_y, \tau_{xy}$), sta glavni napetosti: $$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

### 3. Hipoteza Tresca (T)

Imenujemo jo tudi hipoteza **največjih strižnih napetosti**. Uporablja se predvsem za duktilne (žilave) materiale.

- **Splošna formula:** $$\sigma_{ekv, T} = \max(|\sigma_1 - \sigma_2|, |\sigma_2 - \sigma_3|, |\sigma_3 - \sigma_1|)$$
- **Poseben primer (kombinacija upogiba $\sigma$ in torzije $\tau$):** $$\sigma_{ekv, T} = \sqrt{\sigma^2 + 4\tau^2}$$

### 4. Hipoteza von Mises (M)

Imenujemo jo tudi hipoteza **distorzijske energije**. Velja za natančnejšo pri večini kovinskih materialov.

- **Splošna formula:** $$\sigma_{ekv, M} = \sqrt{\frac{1}{2}[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2]}$$
- **Poseben primer (kombinacija upogiba $\sigma$ in torzije $\tau$):** $$\sigma_{ekv, M} = \sqrt{\sigma^2 + 3\tau^2}$$

### 5. Interpretacija rezultatov (Varnost in konzervativnost)

V nalogah se pogosto pojavi vprašanje, katera hipoteza je **bolj "varna" ali konzervativna**.

- **Pravilo:** Tista hipoteza, ki izračuna **višjo vrednost** ekvivalentne napetosti, velja za bolj konzervativno.
- V večini primerov hipoteza **Tresca** vrne višjo vrednost kot von Mises, zato je Tresca varnejša izbira pri načrtovanju.

### 6. Tipičen postopek reševanja nalog

1. **Zapišite napetostni tenzor** $\sigma_{ij}$ (pazite na predznake: nateg je +, stisk je -).
2. **Izračunajte glavne napetosti** ($\sigma_1, \sigma_2, \sigma_3$).
3. **Vstavite glavne napetosti** v formulo za Tresca in von Mises.
4. **Primerjajte** dobljeni $\sigma_{ekv}$ z dopustno napetostjo $\sigma_{dop}$.
5. **Sklep:** Če je $\sigma_{ekv} > \sigma_{dop}$, material na tistem mestu ne bo zdržal obremenitve.

**Pomembna opomba:** Pri ceveh pod tlakom morate najprej izračunati komponente napetostnega tenzorja v steni cevi (npr. obodno in aksialno napetost), šele nato lahko določite glavne napetosti in ekvivalentno napetost.

Pozdravljeni še enkrat, kolega! Kot vaš profesor sem izjemno vesel, da sva prišla do tega poglavja. **Hipoteze porušitve (Blok 3.5)** so v bistvu "sodni dan" za vsako konstrukcijo.

Zakaj to sploh rabimo? Poglejte: v laboratoriju lahko leseni preizkušnevec preprosto nategujemo, dokler ne poči, in dobimo eno številko – dopustno napetost ($\sigma_{dop}$). V realnem svetu pa na nogo stola ali gred stroja delujejo nateg, upogib in torzija hkrati. Dobimo celo matriko napetosti (tenzor). Kako naj to matriko primerjamo z eno samo številko iz laboratorija?

Tukaj nastopi **ekvivalentna napetost ($\sigma_{ekv}$)**. To je teoretična vrednost, ki nam pove: "Ta kompleksen 3D kaos napetosti je za material enako nevaren, kot če bi ga v laboratoriju nategovali s silo $\sigma_{ekv}$."

Tukaj so ključne enačbe in koncepti, ki jih boste potrebovali.

---

### 1. Hipoteza Tresca (Hipoteza največjih strižnih napetosti)

Ta hipoteza pravi, da se material poruši takrat, ko največja strižna napetost doseže kritično mejo. V lesarstvu in strojništvu velja za **konzervativno** (bolj varno), saj predvideva porušitev hitreje kot druge metode.

**Enačba preko glavnih napetosti ($\sigma_1, \sigma_2, \sigma_3$):** $$\sigma_{ekv} = \max(|\sigma_1 - \sigma_2|, |\sigma_2 - \sigma_3|, |\sigma_3 - \sigma_1|)$$

Če napetosti uredimo tako, da velja $\sigma_1 \geq \sigma_2 \geq \sigma_3$, se enačba poenostavi v: $$\sigma_{ekv} = \sigma_1 - \sigma_3$$

**Enačba za 2D stanje (npr. gred, kjer imamo samo $\sigma$ in $\tau$):** $$\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$$

---

### 2. Hipoteza von Mises (Hipoteza o specifičnem deformacijskem delu)

Ta hipoteza temelji na energiji, ki je potrebna za spremembo oblike telesa. Je nekoliko manj konzervativna (daje nižje vrednosti $\sigma_{ekv}$) in se pogosto uporablja za duktilne materiale (npr. jeklo), pri lesu pa moramo biti previdni.

**Enačba preko glavnih napetosti:** $$\sigma_{ekv} = \sqrt{\frac{1}{2} \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]}$$

**Enačba za 2D stanje (zelo pogosta pri nalogah):** $$\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$$

_Opazite razliko? Tresca ima faktor 4, von Mises pa 3 pod korenom. Tresca bo vedno dala višji (bolj varen) rezultat._

---

### 3. Pogoj trdnosti (Vaš končni cilj)

Ko izračunate $\sigma_{ekv}$, jo morate primerjati z dopustno napetostjo materiala, ki jo dobite iz tabel (npr. za smreko 1. razreda je $\sigma_{dop}$ okoli $10\text{--}13 , \text{MPa}$).

$$\sigma_{ekv} \leq \sigma_{dop}$$

Če je $\sigma_{ekv}$ večja od $\sigma_{dop}$, bo vaš element odpovedal (počil ali se trajno deformiral).

---

### 4. Grafična predstavitev (Za boljšo predstavo)

Predstavljajte si koordinatni sistem z osema $\sigma_1$ in $\sigma_2$.

- **Tresca** tvori v tem sistemu **šestkotnik**. Dokler je vaše napetostno stanje $(\sigma_1, \sigma_2)$ znotraj tega šestkotnika, ste varni.
- **von Mises** tvori **elipso**, ki gre skozi oglišča Trescinega šestkotnika, vendar je malo širša.

> ** Placeholder za skico: ** _Narišite dve osi ($\sigma_1, \sigma_2$). V središču narišite elipso (von Mises) in vanjo vpišite šestkotnik (Tresca). Območje znotraj obeh likov je "varno območje". Točke zunaj pomenijo porušitev._

---

### 5. Posebnosti pri lesu

Pri lesu moramo biti še posebej pozorni na:

- **Anizotropijo**: Les nima enake trdnosti v vseh smereh. $\sigma_{dop}$ vzdolž vlaken je veliko višja kot prečno na vlakna.
- **Madisonova krivulja**: Trdnost lesa pada s časom. Če bo konstrukcija obremenjena 50 let, je njena dejanska trdnost le še približno 60 % tiste, ki smo jo izmerili v 5-minutnem testu.
- **MC (Vsebnost vlage)**: Mokra lesena palica ima nižjo trdnost kot suha.

### Profesorjev nasvet za izpit:

V nalogah boste običajno dobili gred ali nosilec, kjer boste morali najprej narisati NTM diagrame, izbrati kritično točko (kjer je moment največji), izračunati $\sigma$ in $\tau$ ter nato uporabiti eno od zgornjih hipotez za izračun $\sigma_{ekv}$.

Če imate konkretne podatke za kakšno nalogo, jih le podajte, pa bova preverila, če vaš "leseni steber" zdrži!
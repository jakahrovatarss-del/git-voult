Za reševanje nalog iz poglavja **Napetostno stanje (Blok 3)** so na podlagi virov ključni naslednji koncepti, enačbe in postopki:

### 1. Napetostni tenzor

Napetostno stanje v točki je opisano z napetostnim tenzorjem $\sigma_{ij}$, ki v 3D obliki vsebuje normalne napetosti ($\sigma_x, \sigma_y, \sigma_z$) in strižne napetosti ($\tau_{xy}, \tau_{xz}, \tau_{yz}$): $$\sigma_{ij} = \begin{pmatrix} \sigma_x & \tau_{xy} & \tau_{xz} \ \tau_{yx} & \sigma_y & \tau_{yz} \ \tau_{zx} & \tau_{zy} & \sigma_z \end{pmatrix}$$

### 2. Glavne napetosti in smeri

Glavne napetosti ($\sigma_1, \sigma_2, \sigma_3$) so lastne vrednosti napetostnega tenzorja, ki jih določimo z reševanjem karakteristične enačbe: $$\det(\sigma_{ij} - \sigma \cdot \delta_{ij}) = 0$$

- **V 2D stanju (ravninsko):** Glavne napetosti izračunamo kot: $$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
- **Kot glavnih smeri ($\phi$):** Kot med osjo $x$ in normalo na ravnino, kjer deluje glavna napetost: $$\tan(2\phi) = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

### 3. Ekvivalentne napetosti (Trdnostne hipoteze)

Uporabljajo se za oceno varnosti konstrukcije, ko imamo večosno napetostno stanje:

- **Tresca (T):** Maksimalna strižna napetost. $$\sigma_{ekv} = \max(|\sigma_1 - \sigma_2|, |\sigma_2 - \sigma_3|, |\sigma_3 - \sigma_1|)$$ V ravninskem primeru ($\sigma, \tau$): $\sigma_{ekv} = \sqrt{\sigma^2 + 4\tau^2}$.
- **von Mises (M):** Energija distorzije. $$\sigma_{ekv} = \sqrt{\frac{1}{2}[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2]}$$ V ravninskem primeru ($\sigma, \tau$): $\sigma_{ekv} = \sqrt{\sigma^2 + 3\tau^2}$.
- **Varnost:** Hipoteza, ki da **višjo vrednost** ekvivalentne napetosti, velja za bolj **konzervativno** (varnejšo).

### 4. Povezava med napetostmi in deformacijami (Hookov zakon)

Pri prehodu med deformacijskim tenzorjem ($\varepsilon_{ij}$) in napetostnim tenzorjem ($\sigma_{ij}$) uporabljamo Laméjeve konstante:

- **Laméjeva konstanta ($\lambda$):** $\lambda = \frac{E \cdot \nu}{(1 - 2\nu)(1 + \nu)}$
- **Strižni modul ($G$):** $G = \frac{E}{2(1 + \nu)}$
- **Volumska dilatacija:** $\varepsilon_v = \varepsilon_x + \varepsilon_y + \varepsilon_z$

**Izračun napetosti iz deformacij:** $$\sigma_i = \lambda \cdot \varepsilon_v + 2G \cdot \varepsilon_i$$ (velja za $x, y, z$) $$\tau_{ij} = 2G \cdot \varepsilon_{ij}$$

### 5. Napetosti na poljubno nagnjeni ravnini

Če ravnina oklepa kot $\phi$ z osjo $x$, sta normalna ($\sigma_n$) in strižna ($\tau_n$) napetost: $$\sigma_n = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2} \cos(2\phi) + \tau_{xy} \sin(2\phi)$$ $$\tau_n = -\frac{\sigma_x - \sigma_y}{2} \sin(2\phi) + \tau_{xy} \cos(2\phi)$$

### 6. Mohrova krožnica

Mohrova krožnica je grafični prikaz napetostnega stanja. Središče krožnice leži na osi $\sigma$ v točki $\frac{\sigma_x + \sigma_y}{2}$, polmer pa je enak $\sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$.

### 7. Dodatni pomembni koncepti

- **Volumska sprememba:** $\Delta V = V \cdot \varepsilon_v$, kjer je $V$ prvotni volumen.
- **Dopustna napetost:** Stanje je varno, če je $\sigma_{ekv} \leq \sigma_{dop}$.
- **Specifični primeri:** Za cevi pod tlakom je treba določiti komponente napetostnega tenzorja v steni cevi (radialna, obodna, aksialna).

Pozdravljeni, kolega študent! Kot vaš profesor na lesarski fakulteti vas bom danes popeljal skozi osrčje **teorije napetosti** (Blok 3). To poglavje je temelj vsega, kar boste kasneje delali pri dimenzioniranju lesenih vezi in nosilcev.

Napetostno stanje nam pove, kakšne notranje "sile" občuti material v določeni točki, ko ga obremenimo. Spodaj so zbrane vse ključne enačbe in koncepti, ki jih boste potrebovali za reševanje izpitnih nalog.

---

### 1. Napetostni tenzor ($\sigma_{ij}$)

V poljubni točki telesa napetostno stanje opišemo z **napetostnim tenzorjem**. Predstavljajte si majhen elementarni kvader (ali kocko) znotraj lesenega stebra. Na vsako ploskev delujejo normalne in strižne napetosti.

Tenzor v 3D zapišemo kot matriko: $$\sigma_{ij} = \begin{pmatrix} \sigma_x & \tau_{xy} & \tau_{xz} \ \tau_{yx} & \sigma_y & \tau_{yz} \ \tau_{zx} & \tau_{zy} & \sigma_z \end{pmatrix}$$

- **$\sigma$ (normalne napetosti):** Delujejo pravokotno na ploskev (nateg (+) ali tlak (-)).
- **$\tau$ (strižne napetosti):** Delujejo v ravnini ploskve.
- Velja **simetrija**: $\tau_{xy} = \tau_{yx}$, $\tau_{xz} = \tau_{zx}$, $\tau_{yz} = \tau_{zy}$.

---

### 2. Napetostni vektor ($\vec{p}$) na poljubni ravnini

Če ta mali kvader "zarežete" pod nekim kotom, ki ga določa normala $\vec{n} = (\cos \alpha, \cos \beta, \cos \gamma)$, lahko izračunate komponente napetostnega vektorja $\vec{p}$:

$$p_x = \sigma_x \cos \alpha + \tau_{yx} \cos \beta + \tau_{zx} \cos \gamma$$ $$p_y = \tau_{xy} \cos \alpha + \sigma_y \cos \beta + \tau_{zy} \cos \gamma$$ $$p_z = \tau_{xz} \cos \alpha + \tau_{yz} \cos \beta + \sigma_z \cos \gamma$$

Ko imate vektor $\vec{p}$, lahko izračunate dejansko **normalno napetost ($\sigma_n$)** in **strižno napetost ($\tau_n$)** na tej nagnjeni ploskvi:

- **Normalna napetost:** $\sigma_n = \vec{p} \cdot \vec{n} = p_x n_x + p_y n_y + p_z n_z$.
- **Tangencialna (strižna) napetost:** $\tau_n = \sqrt{|\vec{p}|^2 - \sigma_n^2}$.

---

### 3. Glavne napetosti ($\sigma_1, \sigma_2, \sigma_3$)

To je najpomembnejši del nalog. Iskanje glavnih napetosti pomeni iskanje takšne orientacije kvadra, kjer so vse **strižne napetosti enake nič** ($\tau = 0$). Te napetosti dobimo z reševanjem determinante:

$$\det \begin{viding} \sigma_x - \sigma & \tau_{xy} & \tau_{xz} \ \tau_{yx} & \sigma_y - \sigma & \tau_{yz} \ \tau_{zx} & \tau_{zy} & \sigma_z - \sigma \end{viding} = 0$$

Iz tega dobimo kubično enačbo: $$\sigma^3 - I_1 \sigma^2 + I_2 \sigma - I_3 = 0$$ Kjer je **$I_1$ prva invarianta** (vsota po diagonali): $I_1 = \sigma_x + \sigma_y + \sigma_z$.

**Rezultat:** Dobimo tri realne rešitve, ki jih razvrstimo po velikosti: **$\sigma_1 \geq \sigma_2 \geq \sigma_3$**.

---

### 4. Ravninsko napetostno stanje (RNS / 2D)

Večina nalog na vajah in kolokvijih se osredotoča na 2D primer, kjer je npr. $\sigma_z = 0$ in $\tau_{xz} = \tau_{yz} = 0$.

**Glavne napetosti v 2D:** $$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

**Kot glavnih smeri ($\varphi$):** $$\tan(2\varphi) = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

---

### 5. Mohrova krožnica (Grafična rešitev)

To je vaš vizualni pripomoček št. 1. Namesto računanja lahko napetosti določite grafično.

**Postopek risanja:**

1. Narišite osi $\sigma$ (abscisa) in $\tau$ (ordinata).
2. Vrišite točki: $P_x (\sigma_x, -\tau_{xy})$ in $P_y (\sigma_y, \tau_{xy})$.
3. Povežite točki z daljico. Kjer daljica seka os $\sigma$, je **središče krožnice $S$**.
    - $S = \frac{\sigma_x + \sigma_y}{2}$.
4. Narišite krožnico skozi točki $P_x$ in $P_y$. **Radij $r$** krožnice predstavlja največjo strižno napetost.
5. Kjer krožnica seka os $\sigma$, dobite **glavne napetosti $\sigma_1$ in $\sigma_2$**.

**Zakaj je to koristno?** Na krožnici lahko vidite, kako se napetosti spreminjajo, ko vrtite element. V 3D primeru imamo tri takšne krožnice, ki so vgnezdene ena v drugi.

---

### Profesorjev nasvet za intuicijo:

Pri lesu je poznavanje smeri napetosti ključno zaradi njegove **anizotropije**. Če so glavne napetosti poravnane z lesnimi vlakni, bo konstrukcija zdržala veliko več, kot če vlakna tečejo poševno (strižna odpoved). Ko rešujete nalogo z napetostnim tenzorjem, si vedno predstavljajte, kako se ta mali delec v materialu "razteza" ali "stiska" pod vplivom izračunanih $\sigma_1$ in $\sigma_2$.

Če potrebujete izračun za konkretno nalogo s številkami, mi jo pošljite in jo bova skupaj rešila korak za korakom!
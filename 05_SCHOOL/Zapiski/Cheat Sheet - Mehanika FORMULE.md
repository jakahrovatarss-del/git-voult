---
tags: [mehanika, cheat-sheet, formule, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# Cheat Sheet — Mehanika FORMULE

> Samo formule, koncepti in pravila. Brez primerov, brez razlag.
> Celoten cheat sheet z razlagami: [[Cheat Sheet - Mehanika Celotna]]

---

## BLOK 0 — STATIKA

### Ravnotežje

$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0 \quad \text{(2D)}$$

$$\sum F_x=0,\ \sum F_y=0,\ \sum F_z=0,\ \sum M_x=0,\ \sum M_y=0,\ \sum M_z=0 \quad \text{(3D)}$$

### Razstavljanje sile

| Kot od | $F_x$ | $F_y$ |
|--------|-------|-------|
| Navpičnice α | $F\sin\alpha$ | $F\cos\alpha$ |
| Vodoravnice α | $F\cos\alpha$ | $F\sin\alpha$ |

### Rezultanta

$$R_x = \sum F_{x,i}, \quad R_y = \sum F_{y,i}, \quad R = \sqrt{R_x^2+R_y^2}$$

### Redukcija na točko O (2D)

$$M_O = \sum(x_i \cdot F_{y,i} - y_i \cdot F_{x,i})$$

### Paličje — metoda vozlišč

$$\text{Za vsako vozlišče: } \sum F_x=0,\ \sum F_y=0 \quad \text{(privzami nateg +)}$$

### Paličje — metoda prereza (Ritter)

$$\text{Prereži 3 palice} \to \sum M \text{ okrog presečišča 2 neznanih} \to \text{direktno 3. neznanka}$$

### Stabilnost — kritični kot guganja

$$\tan\alpha = \frac{x_T}{y_T} \quad \text{(pogoj: težišče točno nad vrtiščem, } B_y = 0\text{)}$$

Odmik težišča: $x_T$ = vodoravno od vrtišča, $y_T$ = navpično od vrtišča.

🔗 [[Naloga - Mehanika - Statika Stol Valj Stabilnost]]

### Trenje (Coulomb)

$$F_{tr} \leq \mu_s \cdot N, \qquad \tan\alpha \leq \mu_s$$

### Zagozda (wedge friction)

Na **vsaki** kontaktni površini ločeno: $F_{tr,i} = \mu_i \cdot N_i$

$$\text{FBD zagozde} \to \sum F_x = 0,\ \sum F_y = 0 \to F_{min}$$

Tipično: 2–3 trenjske sile hkrati → zapiši vsako normalo + trenje posebej. Trenjska sila deluje **nasprotno** smeri premika zagozde.

### Podpore

| Podpora | Reakcije | Neznanke |
|---------|----------|----------|
| Tečaj/pin | $A_x$, $A_y$ | 2 |
| Valj/kotalka | $B_y$ | 1 |
| Vpetje | $A_x$, $A_y$, $M_A$ | 3 |

**Pravilo:** Piši moment okrog točke z največ neznankami → direktna rešitev.

---

## BLOK 1 — NTM DIAGRAMI

### Diferencialne zveze

$$\frac{dT}{ds} = -q, \qquad \frac{dM}{ds} = T$$

### Tipični $M_{max}$

| Obremenitev                                       | $M_{max}$                                       |
| ------------------------------------------------- | ----------------------------------------------- |
| Konzola, sila $F$ na koncu                        | $F \cdot L$                                     |
| Konzola, porazdeljena $q$                         | $q L^2 / 2$                                     |
| Prostoležeč, $F$ na sredini                       | $F L / 4$                                       |
| Prostoležeč, porazdeljena $q$                     | $q L^2 / 8$                                     |
| Prostoležeč, $F$ pri razdalji $a$ od leve podpore | $\dfrac{F \cdot a \cdot b}{L}$ (kjer $b = L-a$) |
| Previs (sila $F$ za podporo pri razdalji $a$)     | $F \cdot a$                                     |

### Oblika diagrama

- $q = 0$: $T$ = konst, $M$ = linearen
- $q = $ konst: $T$ = linearen, $M$ = **parabola**
- Osamljena sila $F$: lom v $T$, kink v $M$
- Osamljeni moment $M_0$: skok v $M$, $T$ nespremenjen

### Robni pogoji

| Prosti konec | $T=0$, $M=0$ |
|---|---|
| Vpetje | $y=0$, $y'=0$ |
| Notranje tečišče | $M=0$ |

> 🔗 Naloge: [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] — lomljeni okvir, Gerber memberek, 5 polj

### 3D NTM — prostorska gred

6 notranjih veličin v vsakem prerezu:

| Veličina | Opis |
|----------|------|
| $N$ | Osna sila (vzdolž osi gredi) |
| $T_n$, $T_b$ | Prečni sili v ravnini $n$ in $b$ |
| $M_t$ | Torzijski moment |
| $M_n$, $M_b$ | Upogibna momenta v dveh ravninah |

Naravni koordinatni sistem (levoročni): os $t$ = tangenta (vzdolž gredi), os $n$ = normala (navpik), os $b$ = binormala (vodoravno).

Postopek prereza — ravnotežje **levo** od P pri koordinati $s$:
$$N = -\sum F_t, \quad T_n = -\sum F_n, \quad T_b = -\sum F_b$$
$$M_t = -\sum M_t^{ext}, \quad M_n(s) = A_z \cdot s - \ldots, \quad M_b(s) = -A_y \cdot s + \ldots$$

**Jermenica** (razlika napetosti v krakoma, polmer $R$):
$$\boxed{M_t = (S_1 - S_2) \cdot R}$$

**Poševno ozobljenje** (kot poševnosti $\beta$, sila $F$ pravokotno na bočnico):
$$F_t = F\cos\beta \quad \text{(tangencialna → povzroča } M_t\text{)}, \qquad F_a = F\sin\beta \quad \text{(aksialna → povzroča upogib)}$$

**Risanje 3D diagramov:** $T_n$ in $T_b$ v ločenih ravninah (ali skupaj z oznakama ↕ in ↔); enako $M_n$ in $M_b$.

> 🔗 Primer: [[Vaje - NTM diagrami - Vse vrste]] / NotrSileVaje N2

---

## BLOK 1.5 — GEOMETRIJSKE KARAKTERISTIKE

### Težišče sestavljenega prereza

$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}$$

### Steinerjev stavek

$$I_x = \sum\left(I_{x,i} + A_i \cdot \Delta y_i^2\right)$$

### Standardni prerezi

| Prerez | $I$ | $W = I/e$ |
|--------|-----|-----------|
| Pravokotnik $b \times h$ | $\frac{bh^3}{12}$ | $\frac{bh^2}{6}$ |
| Polni krog $d$ | $\frac{\pi d^4}{64}$ | $\frac{\pi d^3}{32}$ |
| Votli krog $d_o, d_i$ | $\frac{\pi(d_o^4-d_i^4)}{64}$ | $\frac{\pi(d_o^4-d_i^4)}{32 d_o}$ |
| Votel pravokotnik $B\times H$ brez $b\times h$ | $\dfrac{BH^3-bh^3}{12}$ | $\dfrac{BH^3-bh^3}{6H}$ |

### Polarna vztrajnost

$$I_p = I_x + I_y \quad \text{(za krog: } I_p = 2I\text{)}$$

### Odpornostni moment torzija (krog)

$$W_t = \frac{\pi d^3}{16} = 2W$$

### Polmer inercije

$$i = \sqrt{\frac{I}{A}}$$

### Statični moment prereza $S$

$$S = A' \cdot y_{T'} \quad \text{(ploščina nad rezom × razdalja težišča od nevtralne osi)}$$

### Glavne vztrajnosti (Mohr za prerez)

$$I_{1,2} = \frac{I_x+I_y}{2} \pm \sqrt{\left(\frac{I_x-I_y}{2}\right)^2 + I_{xy}^2}$$

---

## BLOK 2 — UPOGIB

### Dimenzioniranje prereza

$$\sigma_{max} = \frac{M_{max}}{W} \leq \sigma_{dop} \quad \Rightarrow \quad W_{min} = \frac{M_{max}}{\sigma_{dop}}$$

### Minimalne dimenzije iz $W_{min}$

| Prerez | Formula |
|--------|---------|
| Pravokotnik, $h=2b$ | $b = \sqrt[3]{\frac{3 W_{min}}{2}}$ |
| Polni krog | $d = \sqrt[3]{\frac{32 M_{max}}{\pi \sigma_{dop}}}$ |

### Strižna napetost

$$\tau = \frac{T \cdot S}{I \cdot b}, \qquad \tau_{max} = 1{,}5 \cdot \frac{T}{A} \quad \text{(pravokotnik)}$$

### Kombinirana N + M

$$\sigma = \frac{N}{A} \pm \frac{M}{W}$$

### Diferencialna enačba elastike

$$EI \cdot y''(x) = M(x)$$

### Materialni podatki

| Material | $E$ [kN/cm²] | $\sigma_{dop}$ [kN/cm²] |
|----------|-------------|------------------------|
| Jeklo S235 | 21 000 | 16 |
| Les (iglavci) | 1 000 | 1,0–1,2 |

---

## BLOK 2.5 — POVESI (DEFORMACIJE PRI UPOGIBU)

### Tabela povesov

| Nosilec | Obtežba | Poves $f_{max}$ | Zasuk $\varphi$ |
|---------|---------|-----------------|-----------------|
| Konzola | $F$ na koncu | $\dfrac{FL^3}{3EI}$ | $\dfrac{FL^2}{2EI}$ |
| Konzola | $q$ po dolžini | $\dfrac{qL^4}{8EI}$ | $\dfrac{qL^3}{6EI}$ |
| Prostoležeč | $F$ na sredini | $\dfrac{FL^3}{48EI}$ | $\dfrac{FL^2}{16EI}$ |
| Prostoležeč | $q$ po dolžini | $\dfrac{5qL^4}{384EI}$ | $\dfrac{qL^3}{24EI}$ |
| Prostoležeč | $F$ na $a$, $b=L-a$ | $\dfrac{Fa^2b^2}{3EIL}$ | — |

**Superpozicija:** $f_{skupni} = \sum f_i$ (veljavno za linearne sisteme!)

---

## BLOK 3 — NAPETOSTNO STANJE (MOHROVA KROŽNICA)

### Mohrova krožnica

$$\sigma_{sr} = \frac{\sigma_x+\sigma_y}{2}, \qquad R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

$$\sigma_{1,2} = \sigma_{sr} \pm R, \qquad \tau_{max} = R$$

$$\tan(2\varphi) = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

### Napetosti na poljubni ravnini $\varphi$

$$\sigma(\varphi) = \sigma_{sr} + R\cos(2\varphi), \qquad \tau(\varphi) = -R\sin(2\varphi)$$

### Kontrola (invarianta I₁)

$$\sigma_1 + \sigma_2 = \sigma_x + \sigma_y \quad \text{(mora biti enako!)}$$

### Hookov zakon 3D

$$\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y+\sigma_z)\right], \quad \text{(ciklično za } y, z\text{)}$$

$$G = \frac{E}{2(1+\nu)}$$

### Čisto torzijsko stanje

$$\sigma_x=0,\ \tau_{xy}=\tau \quad\Rightarrow\quad \sigma_1=+\tau,\ \sigma_2=-\tau,\ \varphi_0=45°$$

---

## BLOK 3.5 — HIPOTEZE PORUŠITVE

### Von Mises (HMH) — distorzijska energija

$$\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop} \quad \text{(2D, } \sigma+\tau\text{)}$$

$$\sigma_{ekv,VM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2} \quad \text{(2D, } \sigma_1,\sigma_2\text{)}$$

$$\sigma_{ekv,VM} = \sqrt{\tfrac{1}{2}\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\right]} \quad \text{(3D)}$$

### Tresca — max strižna napetost

$$\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} \leq \sigma_{dop} \quad \text{(2D, } \sigma+\tau\text{)}$$

$$\sigma_{ekv,T} = \sigma_1 - \sigma_3 \quad \text{(3D, obvezna razvrstitev } \sigma_1\geq\sigma_2\geq\sigma_3\text{!)}$$

### Ključno pravilo

$$\boxed{\text{Tresca} = 4\tau^2 \quad \text{VM} = 3\tau^2 \quad \Rightarrow \quad \text{Tresca vedno višji = bolj konzervativna}}$$

### Varnostni faktor

$$\nu = \frac{\sigma_{dop}}{\sigma_{ekv}} \geq \nu_{zahtevani}$$

---

## BLOK 4 — EULER UKLON

### Kritična sila

$$F_k = \frac{\pi^2 \cdot E \cdot I_{min}}{l_u^2}$$

### Uklonska dolžina

$$l_u = \beta \cdot L$$

| Robni pogoji | $\beta$ |
|--------------|---------|
| Oba konca vpeta | 0,5 |
| Vpetje + pin | 0,7 |
| Oba memberka (standard) | **1,0** |
| Konzola | **2,0** ← najnevarnejša |

### Vitkost

$$\lambda = \frac{l_u}{i}, \qquad i = \sqrt{\frac{I_{min}}{A}}, \qquad \lambda_e = \pi\sqrt{\frac{E}{\sigma_{dop}}}$$

| Material | $\lambda_e$ |
|----------|-------------|
| Jeklo S235 | ≈ 114 |
| Les | ≈ 90–99 |

### Kritična napetost (Euler, velja le za $\lambda > \lambda_e$)

$$\sigma_{krit} = \frac{\pi^2 E}{\lambda^2}$$

### Tetmajer (les, $20 < \lambda < \lambda_e$)

$$\sigma_{krit} = 29{,}3 - 0{,}194 \cdot \lambda \quad [\text{MPa}]$$

### ω-postopek (jeklo, vmesna vitkost)

$$\sigma = \omega \cdot \frac{F}{A} \leq \sigma_{dop}, \qquad F_{dop} = \frac{\sigma_{dop} \cdot A}{\omega}$$

### Dimenzioniranje

$$I_{min,potr} = \frac{F \cdot l_u^2 \cdot \nu}{\pi^2 \cdot E}$$

### Meje veljavnosti (les)

| $\lambda$ | Postopek |
|-----------|---------|
| $< 20$ | Samo tlak: $\sigma = F/A$ |
| $20$ – $\lambda_e$ | Tetmajer / ω |
| $> \lambda_e$ | **Euler** |

**Pravilo:** Vedno vzemi $I_{min}$ — uklon po **šibki osi**!

---

## BLOK 5 — TORZIJA

### Polni krog

$$\tau_{max} = \frac{M_t}{W_t}, \qquad W_t = \frac{\pi d^3}{16} = 2W$$

$$\varphi = \frac{M_t \cdot L}{G \cdot I_p}, \qquad I_p = \frac{\pi d^4}{32} = 2I$$

### Votli krog

$$W_t = \frac{\pi(d_o^4-d_i^4)}{16 d_o}, \qquad I_p = \frac{\pi(d_o^4-d_i^4)}{32}$$

### Bredt (zaprt tankosten profil — box, cev)

$$\tau = \frac{M_t}{2 \cdot A_m \cdot t}$$

$$A_m = (a-t)(b-t) \quad \text{(pravokotni box — srednja linija, NE zunanja!)}$$

### Odprti profil (U, L, I — ŠIBKI!)

$$W_t \approx \frac{1}{3}\sum h_i t_i^3 \quad \text{← zelo majhen, izogibaj torziji!}$$

### Dimenzioniranje

$$W_{t,min} = \frac{M_{t,max}}{\tau_{dop}}$$

### Kombinirano M + Mt

$$\sigma = \frac{M}{W}, \quad \tau = \frac{M_t}{W_t}$$

$$\text{VM:} \quad \sigma_{ekv} = \sqrt{\sigma^2+3\tau^2} \leq \sigma_{dop}$$
$$\text{Tresca:} \quad \sigma_{ekv} = \sqrt{\sigma^2+4\tau^2} \leq \sigma_{dop}$$

### Ekvivalentni moment (krožni prerez — direktno dimenzioniranje)

$$M_{ekv,VM} = \sqrt{M^2 + 0{,}75\,M_t^2} \quad \Rightarrow \quad d = \sqrt[3]{\frac{32\,M_{ekv,VM}}{\pi\,\sigma_{dop}}}$$

$$M_{ekv,T} = \frac{1}{2}\!\left(M + \sqrt{M^2 + M_t^2}\right) \quad \text{(velja ko } \sigma_2 \geq 0\text{)}$$

### Materialni podatki

| Material | $G$ [kN/cm²] | $\tau_{dop}$ [kN/cm²] |
|----------|-------------|----------------------|
| Jeklo S235 | ≈ 8 077 | ≈ 9,2 |

$$G = \frac{E}{2(1+\nu)}$$

---

## BLOK 6 — KINEMATIKA

### Osnove točke

$$v = \dot{s}, \quad a = \dot{v}, \quad \omega = \dot{\varphi}, \quad \alpha = \dot{\omega}$$

$$\omega = \frac{2\pi n}{60} \quad \text{[rpm → rad/s]}$$

### EPG — enakomerno pospešeno gibanje ($a = \text{konst}$)

$$v = v_0 + at, \qquad s = v_0 t + \tfrac{1}{2}at^2, \qquad v^2 = v_0^2 + 2a\Delta s \quad \text{(brez časa!)}$$

### Naravni koordinatni sistem

$$a_t = \dot{v} = \alpha \cdot R \quad \text{(tangencialni — menja velikost)}$$

$$a_n = \frac{v^2}{\rho} = \omega^2 R \quad \text{(normalni — menja smer, kaže PROTI centru)}$$

$$a = \sqrt{a_t^2 + a_n^2}$$

### Relativno gibanje togega telesa

$$\vec{v}_B = \vec{v}_A + \vec{\omega} \times \vec{r}_{AB}, \qquad |v_{B/A}| = \omega \cdot r_{AB} \quad \text{(⊥ na } r_{AB}\text{)}$$

$$\vec{a}_B = \vec{a}_A + \alpha \times r_{AB} - \omega^2 r_{AB}$$

### Pol hitrosti P

$$v_B = \omega \cdot \overline{PB} \quad \text{(P = točka kjer } v=0\text{)}$$

Postopek: nariši $\bot$ na vsako znano hitrost → presečišče = P.

### Mehanizem — štiričlenski (splošni postopek)

$$\vec{v}_B = \vec{v}_A + \omega_{AC} \times \vec{r}_{AB} \quad \text{→ pogoj iz odvodne palice → } \omega_{AC}$$

$$\vec{v}_C = \vec{v}_A + \omega_{AC} \times \vec{r}_{AC}$$

**Pogoj odvodne palice EB (E = NI, kot $\beta$):** $\vec{v}_B \perp \text{EB}$ → $\dfrac{v_{Bx}}{v_{By}} = -\tan\beta$ (ali $-\cot\beta$, odvisno od smeri)

🔗 [[Naloga - Mehanika - Kinematika Mehanizem ADAC]] — Izpit 17. 4. 2015

### Kolo, ki se kotali (brez drsenja)

$$v_{kontakt} = 0 \quad \text{(pol = stik s podlago)}$$

$$v_{center} = \omega R, \qquad v_{vrh} = 2\omega R$$

### Sestavljeno gibanje

$$\vec{v}_{abs} = \vec{v}_{rel} + \vec{v}_{trans}$$

$$\vec{a}_{abs} = \vec{a}_{rel} + \vec{a}_{trans} + \vec{a}_{Cor}$$

$$\vec{a}_{Cor} = 2\vec{\omega} \times \vec{v}_{rel} \quad \text{(samo če } \omega \neq 0 \text{ IN } v_{rel} \neq 0\text{)}$$

### Kinematična veriga (zobniki)

$$i_{12} = \frac{\omega_1}{\omega_2} = \frac{n_1}{n_2} = \frac{z_2}{z_1}$$

### Gibalna stanja

| Stanje | $s(t)$ / $\varphi(t)$ | $a_t$ | $a_n$ |
|--------|----------------------|-------|-------|
| Enakomerno premočrtno | $v_0 t$ | 0 | 0 |
| Enakomerno pospešeno | $v_0 t + \frac{1}{2}at^2$ | $a$ | 0 |
| Enakomerno krožno | $\omega t$ | 0 | $\omega^2 R$ |
| Neenakomerno krožno | $\omega_0 t + \frac{1}{2}\alpha t^2$ | $\alpha R$ | $\omega^2 R$ |

---

## BLOK 7 — DINAMIKA IN NIHANJE

### Newton II — translacija

$$\sum \vec{F} = m \cdot \vec{a} \quad \text{[kN = t·m/s², masa v tonah!]}$$

### Newton II — rotacija (okrog fiksne osi O)

$$\sum M_O = I_O \cdot \alpha$$

$$I_O = I_T + m \cdot d^2 \quad \text{(Steiner)}$$

### Momenti inercije

| Telo | Os | $I$ |
|------|----|-----|
| Palica $L$ | Skozi konec | $\dfrac{mL^2}{3}$ |
| Palica $L$ | Skozi sredino | $\dfrac{mL^2}{12}$ |
| Disk/valj $R$ | Os simetrije | $\dfrac{mR^2}{2}$ |
| Obroč $R$ | Os simetrije | $mR^2$ |
| Sfera $R$ | Diameter | $\dfrac{2mR^2}{5}$ |
| Pravokotna plošča $a \times b$ | Os ⊥ plošči skozi težišče | $\dfrac{m(a^2+b^2)}{12}$ |

> 🔗 Naloge: [[Naloga - Mehanika - Dinamika Mesalo Steiner]] — Steiner za odmaknjeno rezilo, navor za pospeševanje

### D'Alembertov princip

$$\sum \vec{F} + (-m\vec{a}) = 0 \quad \text{(dinamika kot statika z inercijsko silo)}$$

### Energetski zakoni

$$A = F \cdot s \cdot \cos\varphi, \qquad A = M \cdot \varphi \quad \text{(moment)}$$

$$P = F \cdot v = M \cdot \omega$$

$$A_{net} = \Delta E_k = E_{k2} - E_{k1}$$

### Kinetična energija

$$E_k = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2$$

### Ohranitev energije (konzervativni sistem)

$$E_k + E_p = \text{const}, \qquad E_p = mgh + \frac{1}{2}kx^2$$

### Prosto nihanje

$$m\ddot{x} + kx = 0$$

$$\omega_0 = \sqrt{\frac{k}{m}} \quad \text{[rad/s]}, \qquad f_0 = \frac{\omega_0}{2\pi} \quad \text{[Hz]}, \qquad T_0 = \frac{2\pi}{\omega_0} \quad \text{[s]}$$

### Nihanje z dušenjem

$$m\ddot{x} + c\dot{x} + kx = 0$$

$$\xi = \frac{c}{2\sqrt{km}}, \qquad \omega_d = \omega_0\sqrt{1-\xi^2}$$

### Resonanca

$$\omega_{vzb} = \omega_0 \quad \Rightarrow \quad \text{amplituda} \to \infty \text{ (brez dušenja)}$$

### Matematično nihalo

$$\omega_0 = \sqrt{\frac{g}{L}}$$

### Torzijsko nihanje gredi z diskom

$$I\ddot{\varphi} + k_t\varphi = 0, \qquad \omega_0 = \sqrt{\frac{k_t}{I}}$$

---

## HITRI PREGLED — FORMULE ZA IZPIT

### Dimenzioniranje — zaporedni koraki

```
1. STATIKA (Blok 0):     ΣFx=0, ΣFy=0, ΣM=0 → reakcije
2. NTM (Blok 1):         M(x), T(x) diagrami → Mmax, Tmax
3. GEOMETRIJA (Blok 1.5): yT, I, W, Wt
4. NAPETOSTI (Blok 2/5): σ=M/W, τ=T·S/(I·b), τ=Mt/Wt
5. KONTROLA (Blok 3.5):  VM: √(σ²+3τ²) ali Tresca: √(σ²+4τ²) ≤ σdop
6. UKLON (Blok 4):       λ=lu/i → Euler/Tetmajer → Fk
```

### Ključne enačbe na izpitu

$$\boxed{\sigma_{max} = \frac{M}{W} \leq \sigma_{dop}}$$

$$\boxed{F_k = \frac{\pi^2 E I_{min}}{l_u^2}}$$

$$\boxed{\sigma_{ekv,VM} = \sqrt{\sigma^2+3\tau^2} \leq \sigma_{dop}}$$

$$\boxed{\omega_0 = \sqrt{\frac{k}{m}}}$$

$$\boxed{\tau_{Bredt} = \frac{M_t}{2 A_m t}}$$

### Materialne konstante (jeklo S235)

| Konstanta | Vrednost |
|-----------|---------|
| $E$ | 21 000 kN/cm² |
| $G$ | 8 077 kN/cm² |
| $\sigma_{dop}$ | 16 kN/cm² |
| $\tau_{dop}$ | 9,2 kN/cm² |
| $\nu$ (Poisson) | 0,3 |
| $\lambda_e$ | 114 |

### Pogoste napake

- Uklon: vzeti $I_{max}$ namesto **$I_{min}$** (šibka os!)
- Torzija: $W_t = 2W$ za krog — ne $W_t = W$
- Bredt: $A_m$ = srednja linija, ne zunanja ploščina
- Tresca/VM: zamenjati faktor **4** (Tresca) in **3** (VM)
- 3D Tresca: razvrstiti $\sigma_1 \geq \sigma_2 \geq \sigma_3$ — $\sigma_z=0$ je pogosto **vmesna** vrednost!
- Dinamika: masa v **kg ali t**, ne kN!
- Konzola: $\beta = 2$, $l_u = 2L$ — ne $l_u = L$

---

## DODATNE FORMULE (iz TIP sekcij)

### Gerber nosilci

$$M_{čl} = 0 \quad \text{(notranji členek = pogoj)}$$

Postopek: razstavi v členku → reši "viseči" del → preneši silo na drugi del (nasprotno!).

### Euler jermen

$$\frac{F_1}{F_2} = e^{\mu\theta} \quad \text{($F_1$ = napeta stran, $\theta$ v radianih!)}$$

$$180° = \pi\ \text{rad}, \quad 270° = \frac{3\pi}{2}\ \text{rad}$$

### Kolut + trak (band brake)

$$\frac{F_1}{F_2} = e^{\mu\theta} \quad \text{(Euler za trak)}, \qquad M_{zav} = (F_1 - F_2) \cdot R$$

**Postopek:** 1. Euler → $F_1/F_2$ iz kota ovoja $\theta$. 2. Pogoj $M_{zav} = M_{mot}$ → $F_1 - F_2$. 3. $F_1, F_2$ iz razmerja.

### Vrvi — katenoida

$$y = a\cosh\frac{x}{a}, \qquad a = \frac{H_0}{q_0}$$

$H_0$ = vodoravna komponenta (konstanta vzdolž vrvi), $q_0$ = obtežba na m.

### Vrvi — segmentna vrv (točkovne obtežbe)

$$H = \text{const vzdolž celotne vrvi}$$

$$T_i = \sqrt{H^2 + V_i^2}, \qquad \tan\theta_i = \frac{V_i}{H}$$

**Postopek:**
1. Globalno ravnotežje → $A_x, A_y, B_x, B_y$
2. $V_i$ = vertikalna vsota sil od leve do i-tega segmenta
3. $H$ iz geometrijskega pogoja (znana kotota ali dolžina segmenta)
4. $T_{max}$ = maksimalna vertikalna vsota $V$

### Škripci

$$\text{Fiksni škripec:} \quad F_A = 2G \qquad \text{Gibljivi škripec:} \quad S = G/2$$

### Valji v kupu (60°)

Središča → enakostranični trikotnik → kontaktna sila med valji pod **30° od navpičnice**:

$$2N_1\cos30° = G \quad \Rightarrow \quad N_1 = \frac{G}{\sqrt{3}}$$

### Lamé-jev zakon (napetosti iz deformacij)

$$\sigma_x = \frac{E}{(1+\nu)(1-2\nu)}\left[(1-\nu)\varepsilon_x+\nu(\varepsilon_y+\varepsilon_z)\right], \qquad \tau_{xy} = G\cdot\gamma_{xy}$$

### Vzmet — kombinacije

$$k_{eq} = k_1 + k_2 \quad \text{(vzporedni)}$$

$$\frac{1}{k_{eq}} = \frac{1}{k_1} + \frac{1}{k_2} \quad \text{(zaporedni)}$$

### Newton II — klanec s trenjem

$$a = g(\sin\alpha - \mu_k\cos\alpha)$$

### Newton II — dve kladi (Atwood)

$$a = \frac{m_1 g - \mu m_2 g}{m_1 + m_2}, \qquad S = m_1(g-a)$$

### Bat-klip (ročica pod kotom θ)

$$\omega = \frac{v_A}{L\sin\theta}, \qquad v_B = \frac{v_A}{\tan\theta}$$

### L-oblika / portalni okvir — vogal

$$N_{navp} = T_{vodor}, \qquad T_{navp} = N_{vodor}$$

### Dimenzioniranje prereza (različni h/b razmerji)

| Razmerje | $W$ | Formula za $b$ |
|----------|-----|----------------|
| $h = 2b$ | $\frac{2b^3}{3}$ | $b = \sqrt[3]{\frac{3W_{min}}{2}}$ |
| $h = 1{,}5b$ | $0{,}375b^3$ | $b = \sqrt[3]{\frac{W_{min}}{0{,}375}}$ |

### Tetmajer (les) — konkretne vrednosti

$$\sigma_k = a_T - b_T\cdot\lambda, \qquad a_T = 2{,}93\ \text{kN/cm}^2, \quad b_T = 0{,}0194\ \text{kN/cm}^2$$

| $\lambda$ (les) | Postopek |
|-----------------|---------|
| $< 60$ | Samo tlak: $\sigma = F/A$ |
| $60$ – $90$ | Tetmajer |
| $> 90$ | Euler |

### Resonanca — ukrepi

$$\text{Resonanca pri: } \Omega_{vzb} = \omega_0 \quad \Rightarrow \quad \text{amplituda} \to \infty$$

$$\text{Priporoča se: } \left|\frac{\Omega}{\omega_0} - 1\right| > 20\%$$

Ukrepi: sprememba $n$, dodaj maso ($\omega_0\downarrow$), ojači vzmet ($\omega_0\uparrow$), dušilnik.

### Vzmet — energija pri nihanju

$$\frac{1}{2}kx_0^2 = \frac{1}{2}mv_{max}^2 \quad \Rightarrow \quad v_{max} = x_0\cdot\omega_0$$

---

## Povezave

- [[Cheat Sheet - Mehanika Celotna]] ← celoten cheat sheet z razlagami in SVG diagrami
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] ← Blok 1: Gerber + L-oblika
- [[Naloga - Mehanika - Dinamika Mesalo Steiner]] ← Blok 7: Steiner + navor
- [[Naloga - Mehanika - Statika Stol Valj Stabilnost]] ← Blok 0: guganje, tan α = xT/yT
- [[Naloga - Mehanika - Kinematika Mehanizem ADAC]] ← Blok 6: mehanizem, pol P, ωAC, vC
- [[Blok 0 - Statika]] | [[Blok 1 - NTM Diagrami]] | [[Blok 1.5 - Geometrijske Karakteristike]]
- [[Blok 2 - Upogib]] | [[Blok 2.5 - Deformacije pri Upogibu]] | [[Blok 3 - Napetostno Stanje]]
- [[Blok 3.5 - Hipoteze Porusitve]] | [[Blok 4 - Euler Uklon]] | [[Blok 5 - Torzija]]
- [[Blok 6 - Kinematika]] | [[Blok 7 - Dinamika Nihanje]]

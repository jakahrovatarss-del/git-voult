---
tags: [mehanika, kinematika, dinamika, pol-hitrosti, nihanje, newton, energija, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# Poglavje — 3. + 4. SKLOP: Kinematika in Dinamika

## Namen

Celovit zapisek za **3. SKLOP: Kinematika** in **4. SKLOP: Dinamika** — vse tipe nalog z rešitvami. Kinematika dá gibanje (a, α), dinamika poveže gibanje s silami (F, M). Skupaj tvorita neločljiv par.

> **Teorija:** [[Blok 6 - Kinematika]] | [[Blok 7 - Dinamika Nihanje]]

---

## Pregled tipov nalog

| # | Tip naloge | Ključna formula | Naloge |
|---|-----------|-----------------|--------|
| 1 | Kinematika točke: at, an | $a_n = v^2/\rho = \omega^2 R$ | N1 |
| 2 | Pol hitrosti — kolo na ravnini | Pol = stična točka | N2 |
| 3 | Pol hitrosti — bat-klip drsnik | Pol = presečišče ⊥ na v | N3 |
| 4 | Pol hitrosti — štirivezni mehanizem | $\omega = v/r_P$ | N4 |
| 5 | Coriolisov pospešek | $a_{Cor} = 2\omega v_{rel}$ | N5 |
| 6 | Newton II — dve kladi | $\sum F = ma$ za vsako telo | N6 |
| 7 | Newton II — klanec s trenjem | $F_{net} = mg\sin\alpha - \mu mg\cos\alpha$ | N7 |
| 8 | Energetski zakoni — vzmet+masa | $\frac{1}{2}kx_0^2 = \frac{1}{2}mv^2$ | N8 |
| 9 | Dinamika togega telesa — rotacija | $\sum M_O = I_O \alpha$ | N9 |
| 10 | Nihanje — lastna frekvenca | $\omega_0 = \sqrt{k/m}$ | N10 |
| 11 | Prisilno nihanje — resonanca | $\omega_{vzb} = \omega_0$ | N11 |

---

## 3. SKLOP: KINEMATIKA

---

## 1. KINEMATIKA TOČKE — NARAVNI KOORDINATNI SISTEM

### N1 — Točka na krožnici: at, an, a_skupni

> **Besedilo:** Točka se giblje po krožnici polmera $R = 0{,}5\ \text{m}$ z začetno kotno hitrostjo $\omega_0 = 4\ \text{rad/s}$ in konstantnim kotnim pospeškom $\alpha = 2\ \text{rad/s}^2$. Ob $t = 2\ \text{s}$ izračunaj:
> a) kotno hitrost $\omega$, b) tangencialni pospešek $a_t$, c) normalni pospešek $a_n$, d) skupni pospešek $a$.

#### Korak 1 — Kotna hitrost ob t=2s

$$\omega(t) = \omega_0 + \alpha \cdot t = 4 + 2 \cdot 2 = \boxed{8\ \text{rad/s}}$$

#### Korak 2 — Tangencialni pospešek (menja velikost v)

$$a_t = \alpha \cdot R = 2 \cdot 0{,}5 = \boxed{1{,}0\ \text{m/s}^2}$$

> **Fizikalni pomen:** Točka se pospešuje vzdolž tirnice — pospešek je v smeri $v$.

#### Korak 3 — Normalni pospešek (menja smer v)

$$a_n = \omega^2 \cdot R = 8^2 \cdot 0{,}5 = 64 \cdot 0{,}5 = \boxed{32{,}0\ \text{m/s}^2}$$

> **Fizikalni pomen:** Točka mora "zaviti" po krožnici — centripetalni pospešek kaže VEDNO **proti središču**. 

> ⚠️ **PAST:** $a_n$ ni nič samo pri $\omega = 0$ ali $R \to \infty$ (premočrtno gibanje). Visoka kotna hitrost → ogromen $a_n$!

#### Korak 4 — Skupni pospešek

$$a = \sqrt{a_t^2 + a_n^2} = \sqrt{1{,}0^2 + 32{,}0^2} = \sqrt{1 + 1024} = \sqrt{1025} = \boxed{32{,}02\ \text{m/s}^2}$$

Smer skupnega pospeška glede na tangento:

$$\varphi = \arctan\left(\frac{a_n}{a_t}\right) = \arctan\left(\frac{32}{1}\right) = 88{,}2°\ \text{od tangente}$$

> **Primerjava:** $a_t = 1\ \text{m/s}^2$ je 32× manjši od $a_n = 32\ \text{m/s}^2$ → skupni vektor je skoraj enak centripetalnem.

> **gl.:** [[Blok 6 - Kinematika#Gibalna stanja — primerjalna tabela]]

---

## 2. POL HITROSTI — KOLO NA RAVNINI

### N2 — Kolo se kotali brez drsenja

> **Besedilo:** Kolo polmera $R = 0{,}3\ \text{m}$ se kotali brez drsenja po vodoravni podlagi. Hitrost centra $v_C = 1{,}5\ \text{m/s}$ (vodoravno desno). Določi: a) kotno hitrost $\omega$, b) hitrost vrha $v_D$, c) hitrost točke $A$ (na desnem robu koles — 90° od vrha glede na center).

#### Korak 1 — Pol hitrosti

Za kotaljenje brez drsenja je **stična točka s podlago vedno pol**:

$$v_{stik} = 0 \Rightarrow P = \text{stična točka (spodaj)}$$

> **Zakaj?** Kotaljenje brez drsenja = stična točka se ne premika relativno glede na podlago. Torej miruje → je pol.

#### Korak 2 — Kotna hitrost

$$\omega = \frac{v_C}{r_{PC}} = \frac{v_C}{R} = \frac{1{,}5}{0{,}3} = \boxed{5\ \text{rad/s}}$$

#### Korak 3 — Hitrost vrha D ($r_{PD} = 2R$)

$$v_D = \omega \cdot r_{PD} = 5 \cdot 2 \cdot 0{,}3 = \boxed{3{,}0\ \text{m/s}}\ \text{(navzgor + desno)}$$

> **Intuicija:** Vrh se giblje 2× hitreje kot center. Smer $v_D$: ⊥ na $\overline{PD}$ = navzgor desno (pod 45° v tem primeru ne, saj PD je navpičnica — smer je čisto vodoravna).

Točno: $P$ je spodaj, $D$ je zgoraj → $\overrightarrow{PD}$ kaže navzgor → $v_D \perp \overrightarrow{PD}$ kaže **vodoravno desno** ✓

#### Korak 4 — Hitrost točke A (desni rob, 90° od vrha)

Točka A je pri koordinati (R, 0) od centra = (R, R) od pola P.

$$r_{PA} = \sqrt{R^2 + R^2} = R\sqrt{2} = 0{,}3\sqrt{2} = 0{,}424\ \text{m}$$

$$v_A = \omega \cdot r_{PA} = 5 \cdot 0{,}424 = \boxed{2{,}12\ \text{m/s}}$$

Smer $v_A$: ⊥ na $\overrightarrow{PA}$ = pod kotom 45° (navzgor desno).

> **Sanity check:** $v_{stik} = \omega \cdot 0 = 0$ ✓, $v_C = \omega \cdot R = 1{,}5$ ✓, $v_{vrh} = \omega \cdot 2R = 3{,}0$ ✓

> **gl.:** [[Blok 6 - Kinematika#Intuicija]] | [[Koncept - Kinematika Mehanizmi#Primer 2 — Kolo ki se kotali po tleh]]

---

## 3. POL HITROSTI — BAT-KLIP (DRSNIK + ROČICA)

### N3 — Ročica AB: A drsi vodoravno, B drsi navpično

> **Besedilo:** Ročica $AB = 0{,}5\ \text{m}$, nagnjena pod kotom $\theta = 30°$ od vodoravnice. Konec $A$ drsi vodoravno po spodnji vodili s hitrostjo $v_A = 1{,}5\ \text{m/s}$ (desno). Konec $B$ drsi navpično po levi vodili. Določi kotno hitrost ročice $\omega$ in hitrost točke $B$.

#### Korak 1 — Geometrija

$$x_A = L\cos 30° = 0{,}5 \cdot 0{,}866 = 0{,}433\ \text{m}, \qquad y_B = L\sin 30° = 0{,}5 \cdot 0{,}5 = 0{,}25\ \text{m}$$

**Koordinate:** $A = (0{,}433,\ 0)$, $B = (0,\ 0{,}25)$

#### Korak 2 — Iskanje pola P (presečišče pravokotnic na $v$)

| Točka | Smer $v$ | Pravokotnica na $v$ |
|-------|---------|---------------------|
| $A$ | → (vodoravna) | navpičnica skozi $A$: $x = 0{,}433$ |
| $B$ | ↑ (navpična) | vodoravnica skozi $B$: $y = 0{,}25$ |

$$\boxed{P = (0{,}433,\ 0{,}25)}$$

> **Ključni korak:** Pravokotnica na hitrost, NE na telo! $v_A$ je vodoravna → pravokotnica je navpična.

#### Korak 3 — Razdalje od pola

$$r_{PA} = |y_P - y_A| = 0{,}25 - 0 = 0{,}25\ \text{m}$$

$$r_{PB} = |x_P - x_B| = 0{,}433 - 0 = 0{,}433\ \text{m}$$

#### Korak 4 — Kotna hitrost ročice

$$\omega = \frac{v_A}{r_{PA}} = \frac{1{,}5}{0{,}25} = \boxed{6{,}0\ \text{rad/s}}$$

#### Korak 5 — Hitrost točke B

$$v_B = \omega \cdot r_{PB} = 6{,}0 \cdot 0{,}433 = \boxed{2{,}6\ \text{m/s}}\quad \text{(navzgor ↑)}$$

**Smer:** $\overrightarrow{PB}$ kaže vodoravno levo → $v_B \perp \overrightarrow{PB}$ kaže navzgor ↑ ✓

> **Kontrola:** $r_{PA}/r_{PB} = 0{,}25/0{,}433 = \tan30°$ → ustreza geometriji ✓

> **gl.:** [[Konzept - Kinematika Mehanizmi#Algoritem]] | [[Blok 6 - Kinematika#Kako začeti reševati]]

---

## 4. POL HITROSTI — ŠTIRIVEZNI MEHANIZEM

### N4 — Mehanizem z dvema ročicama (tip izpit BTF 2013)

> **Besedilo** (iz kolokvija 2013): Sistem palic AC in BD. Ročica AC ($|AC|=0{,}4\ \text{m}$) je vpeta v $A$ (fiksna os vrtenja), njena prosta točka $C$ je tečajno vezana na telo $CD$ ($|CD|=0{,}6\ \text{m}$). Telo $CD$ je na koncu $D$ vezano na ročico $BD$ ($|BD|=0{,}3\ \text{m}$, fiksna os $B$). Geometrija: $A$ in $B$ sta fiksna, $|AB|=0{,}5\ \text{m}$ vodoravno. V danem položaju: ročica $AC$ je navpična (C nad A), ročica $BD$ je navpična (D nad B), telo $CD$ je vodoravno. Dana je $\omega_{AC} = 2\ \text{rad/s}$ (v smeri urnega kazalca). Določi $\omega_{BD}$ in hitrost točke $E$ (sredina $CD$).

#### Korak 1 — Hitrosti točk C in D

$$v_C = \omega_{AC} \cdot |AC| = 2 \cdot 0{,}4 = 0{,}8\ \text{m/s}$$

Smer $v_C$: ⊥ na $\overrightarrow{AC}$ = navpičnica ↑ v smeri urnega kazalca → $v_C$ je **vodoravna** (desno ali levo?). Ker ω je UKU → točka C se premika v desno: $v_C = 0{,}8\ \text{m/s}\ \rightarrow$

Podobno za ročico BD: D je nad B, $v_D$ ⊥ BD → $v_D$ je **vodoravna**.

#### Korak 2 — Pol telesa CD

| Točka | Smer $v$ | Pravokotnica |
|-------|---------|--------------|
| $C$ | vodoravna → | navpičnica skozi $C$ |
| $D$ | vodoravna (smer neznana) | navpičnica skozi $D$ |

Obe pravokotnici sta navpični → presečišče je **v neskončnosti** → telo $CD$ v tem trenutku izvaja **translacijo** (čisto premočrtno gibanje)!

$$v_D = v_C = \boxed{0{,}8\ \text{m/s}}\ (\rightarrow)$$

> **Intuicija:** Ko sta obe ročici vzporedni (obe navpični), se vezni člen premika vzporedno — to je translacijski položaj mehanizma.

#### Korak 3 — Kotna hitrost ročice BD

$$\omega_{BD} = \frac{v_D}{|BD|} = \frac{0{,}8}{0{,}3} = \boxed{2{,}67\ \text{rad/s}}$$

#### Korak 4 — Hitrost točke E (sredina CD)

Ker je gibanje translacijsko:

$$v_E = v_C = v_D = \boxed{0{,}8\ \text{m/s}\ (\rightarrow)}$$

> **Komentar:** V splošnem (ročici nista vzporedni) bi bila $v_E$ med $v_C$ in $v_D$ po legi. Translacijski položaj je posebni primer — izpitna past!

> **gl.:** [[Koncept - Kinematika Mehanizmi#Primer 3 — Štirivezni mehanizem]]

---

## 5. CORIOLISOV POSPEŠEK

### N5 — Točka na vrtljivem traku

> **Besedilo:** Vrtljivi disk se vrti s konstantno kotno hitrostjo $\omega = 3\ \text{rad/s}$. Po žlebu (ki je radialna premica na disku) se točka premika od centra navzven z relativno hitrostjo $v_{rel} = 0{,}5\ \text{m/s}$ (konstantna). V trenutku, ko je točka na razdalji $r = 0{,}4\ \text{m}$ od centra, izračunaj vse komponente pospeška.

#### Korak 1 — Transportni (centripetalni) pospešek

$$a_{trans,n} = \omega^2 \cdot r = 3^2 \cdot 0{,}4 = \boxed{3{,}6\ \text{m/s}^2}\ \text{(kaže proti centru)}$$

(Ker $\omega = const$: $a_{trans,t} = \alpha \cdot r = 0$)

#### Korak 2 — Relativni pospešek

$$a_{rel} = 0\ \text{(ker } v_{rel} = const\text{)}$$

#### Korak 3 — Coriolisov pospešek

$$a_{Cor} = 2 \cdot \omega \cdot v_{rel} = 2 \cdot 3 \cdot 0{,}5 = \boxed{3{,}0\ \text{m/s}^2}$$

Smer: pravokotna na $v_{rel}$ (= pravokotna na žleb, v smeri vrtenja).

$$a_{abs} = \sqrt{a_{trans,n}^2 + a_{Cor}^2} = \sqrt{3{,}6^2 + 3{,}0^2} = \sqrt{12{,}96 + 9{,}0} = \sqrt{21{,}96} = \boxed{4{,}69\ \text{m/s}^2}$$

> **Coriolisov pospešek obstaja SAMO ko:**  
> - Referenčni sistem se **vrti** ($\omega \neq 0$)  
> - Točka se **relativno premika** v tem sistemu ($v_{rel} \neq 0$)  
> - Manjka eden od pogojev → $a_{Cor} = 0$

> **gl.:** [[Blok 6 - Kinematika#Sestavljeno gibanje — Podrobneje]]

---

## 4. SKLOP: DINAMIKA

---

## 6. NEWTON II — DVE KLADI Z VRVICO

### N6 — Sistem dveh klad (Atwood s trenjem)

> **Besedilo:** Kladivo $m_1 = 5\ \text{kg}$ visi vertikalno, kladica $m_2 = 8\ \text{kg}$ leži na vodoravni mizi s koeficientom trenja $\mu = 0{,}2$. Povezani sta z nerjavno vrvico čez idealen škripec ($g = 10\ \text{m/s}^2$). Določi pospešek sistema $a$ in silo v vrvici $S$.

#### Korak 1 — FBD za vsako telo (ločeno!)

**Kladivo** $m_1$ (pozitivna smer = navzdol):

$$m_1 g - S = m_1 a \quad \Rightarrow \quad 50 - S = 5a \tag{1}$$

**Kladica** $m_2$ (pozitivna smer = desno):

$$N = m_2 g = 8 \cdot 10 = 80\ \text{N}, \qquad F_{tr} = \mu N = 0{,}2 \cdot 80 = 16\ \text{N}$$

$$S - F_{tr} = m_2 a \quad \Rightarrow \quad S - 16 = 8a \tag{2}$$

#### Korak 2 — Rešimo sistem enačb

Seštejem (1) in (2):

$$50 - 16 = 5a + 8a \quad \Rightarrow \quad 34 = 13a \quad \Rightarrow \quad \boxed{a = 2{,}62\ \text{m/s}^2}$$

Iz (1): $S = 50 - 5 \cdot 2{,}62 = 50 - 13{,}1 = \boxed{36{,}9\ \text{N}}$

Kontrola iz (2): $S - 16 = 36{,}9 - 16 = 20{,}9 = 8 \cdot 2{,}62$ ✓

> **Metoda D'Alembert:** Alternativno dodaj inercijski sili $m_1 a$ in $m_2 a$ ter reši statično (Blok 0). Rezultat je enak.

> **gl.:** [[Blok 7 - Dinamika Nihanje#Energetski zakoni — delo moč energija]] | [[Blok 0 - Statika#Kombinacije z drugimi bloki]]

---

## 7. NEWTON II — KLANEC S TRENJEM

### N7 — Klanec: spust z dinamičnim trenjem

> **Besedilo:** Masa $m = 20\ \text{kg}$ se spušča po klancu naklon $\alpha = 25°$ s kinematičnim koeficientom trenja $\mu_k = 0{,}15$. Izračunaj: a) pospešek telesa, b) hitrost po $t = 3\ \text{s}$, c) prevoženo pot.

#### Korak 1 — Normalna sila in trenje

$$N = mg\cos\alpha = 20 \cdot 10 \cdot \cos25° = 200 \cdot 0{,}906 = 181{,}2\ \text{N}$$

$$F_{tr} = \mu_k \cdot N = 0{,}15 \cdot 181{,}2 = \boxed{27{,}2\ \text{N}}\ \text{(nasprotno od gibanja = navzgor po klancu)}$$

#### Korak 2 — Newton II vzdolž klanca (os x = vzdolž klanca navzdol)

$$\sum F_x = mg\sin\alpha - F_{tr} = m \cdot a$$

$$200 \cdot \sin25° - 27{,}2 = 20a \quad \Rightarrow \quad 84{,}5 - 27{,}2 = 20a \quad \Rightarrow \quad 57{,}3 = 20a$$

$$\boxed{a = 2{,}87\ \text{m/s}^2}$$

#### Korak 3 — Kinematika (enakomerno pospešeno gibanje)

$$v(3) = v_0 + at = 0 + 2{,}87 \cdot 3 = \boxed{8{,}6\ \text{m/s}}$$

$$s(3) = v_0 t + \frac{1}{2}at^2 = 0 + \frac{1}{2} \cdot 2{,}87 \cdot 9 = \boxed{12{,}9\ \text{m}}$$

> **Kombinacija Kinematika + Dinamika:** Dinamika (Newton II) da pospešek → kinematika (Blok 6) da hitrost in pot. Klasična "zmagovalna kombinacija" na izpitu!

> **gl.:** [[Blok 7 - Dinamika Nihanje#Intuicija]] | [[Blok 0 - Statika#Trenje — Coulombov zakon]]

---

## 8. ENERGETSKI ZAKONI — VZMET + MASA

### N8 — Sprostitev vzmeti: izračun hitrosti

> **Besedilo:** Vzmet togosti $k = 800\ \text{N/m}$ je stisnjena za $x_0 = 0{,}10\ \text{m}$. Masa $m = 2\ \text{kg}$ se sprosti iz mirovanja. Kakšna je hitrost mase, ko vzmet pride do naravne dolžine? Gibanje je vodoravno (gravitacijo zanemarimo).

#### Korak 1 — Zakon o ohranitvi energije

Konzervativni sistem (brez trenja, brez dušenja):

$$E_{k,1} + E_{p,1} = E_{k,2} + E_{p,2}$$

$$0 + \frac{1}{2}kx_0^2 = \frac{1}{2}mv_{max}^2 + 0$$

#### Korak 2 — Izračun vmax

$$v_{max} = x_0 \sqrt{\frac{k}{m}} = 0{,}10 \cdot \sqrt{\frac{800}{2}} = 0{,}10 \cdot \sqrt{400} = 0{,}10 \cdot 20 = \boxed{2{,}0\ \text{m/s}}$$

> **Elegantna zveza s nihanjem:** $\omega_0 = \sqrt{k/m} = 20\ \text{rad/s}$ je lastna frekvenca. Maksimalna hitrost pri nihanju = $v_{max} = \omega_0 \cdot A$ (amplituda = $x_0$) → $v_{max} = 20 \cdot 0{,}10 = 2{,}0\ \text{m/s}$ ✓

#### Korak 3 — Kontrola z izrekom o delu

$$A_{vzmeti} = \frac{1}{2}kx_0^2 = \frac{1}{2} \cdot 800 \cdot 0{,}01 = 4{,}0\ \text{J}$$

$$\Delta E_k = \frac{1}{2}mv^2 = \frac{1}{2} \cdot 2 \cdot 4{,}0 = 4{,}0\ \text{J} \quad ✓$$

> **gl.:** [[Blok 7 - Dinamika Nihanje#Energetski zakoni — delo moč energija]]

---

## 9. DINAMIKA TOGEGA TELESA — ROTACIJA

### N9 — Disk: kotni pospešek in vrtljaji po t sekund

> **Besedilo:** Polni jekleni disk, masa $m = 5\ \text{kg}$, polmer $R = 0{,}20\ \text{m}$. Na gred deluje navor $M_z = 0{,}5\ \text{Nm}$ (pri stalni geometriji trenja zanemarimo). Disk miruje ob $t = 0$. Izračunaj: a) kotni pospešek $\alpha$, b) kotno hitrost po $t = 3\ \text{s}$, c) vrtljaje na minuto (obr/min) po $t = 3\ \text{s}$.

#### Korak 1 — Masni vztrajnostni moment diska

$$I_O = \frac{1}{2}mR^2 = \frac{1}{2} \cdot 5 \cdot 0{,}04 = \boxed{0{,}10\ \text{kg\,m}^2}$$

> **Zakaj $\frac{1}{2}mR^2$?** Za polni homogeni disk je moment inercije glede na os skozi center = $\frac{1}{2}mR^2$. Za obroč = $mR^2$ (vsa masa na $R$). Za palico = $\frac{1}{3}mL^2$ (konec).

#### Korak 2 — Newton II za rotacijo

$$\sum M_O = I_O \cdot \alpha \quad \Rightarrow \quad \alpha = \frac{M_z}{I_O} = \frac{0{,}5}{0{,}10} = \boxed{5{,}0\ \text{rad/s}^2}$$

#### Korak 3 — Kotna hitrost po t=3s

$$\omega(3) = \omega_0 + \alpha t = 0 + 5{,}0 \cdot 3 = \boxed{15{,}0\ \text{rad/s}}$$

#### Korak 4 — Vrtljaji na minuto

$$n = \frac{\omega \cdot 60}{2\pi} = \frac{15{,}0 \cdot 60}{2\pi} = \frac{900}{6{,}283} = \boxed{143\ \text{obr/min}}$$

> **Enote PAST:** Masa MORA biti v **kg**, ne v kN! $1\ \text{kN} = 1000\ \text{N} = 1000\ \text{kg·m/s}^2$ → masa $= 1000/g \approx 100\ \text{kg}$.

> **gl.:** [[Blok 7 - Dinamika Nihanje#Momenti inercije — Tabela]]

---

## 10. NIHANJE — LASTNA FREKVENCA

### N10 — Masa na vzporednih vzmeteh

> **Besedilo:** Voziček mase $m = 4\ \text{kg}$ je podprt z dvema vzporednima vzmetema $k_1 = k_2 = 500\ \text{N/m}$. Izračunaj: a) ekvivalentno togost, b) lastno frekvenco $\omega_0$, c) nihajni čas $T_0$, d) frekvenco $f_0$ v Hz.

#### Korak 1 — Ekvivalentna togost (vzporedna vzmetna)

$$k_{eq} = k_1 + k_2 = 500 + 500 = \boxed{1000\ \text{N/m}}$$

> **Vzporedna vzmet** (obe se stisneta za isti $x$): $k_{eq} = \Sigma k_i$
> **Zaporedna vzmet** (enaka sila v obeh): $\frac{1}{k_{eq}} = \Sigma \frac{1}{k_i}$

#### Korak 2 — Gibalna enačba

$$m\ddot{x} + k_{eq} x = 0$$

#### Korak 3 — Lastna frekvenca

$$\omega_0 = \sqrt{\frac{k_{eq}}{m}} = \sqrt{\frac{1000}{4}} = \sqrt{250} = \boxed{15{,}81\ \text{rad/s}}$$

#### Korak 4 — Nihajni čas in frekvenca

$$T_0 = \frac{2\pi}{\omega_0} = \frac{2\pi}{15{,}81} = \boxed{0{,}397\ \text{s}}$$

$$f_0 = \frac{\omega_0}{2\pi} = \frac{15{,}81}{6{,}283} = \boxed{2{,}52\ \text{Hz}}$$

> **gl.:** [[Blok 7 - Dinamika Nihanje#Intuicija]]

---

## 11. PRISILNO NIHANJE — RESONANCA

### N11 — Preveritev resonance stroja

> **Besedilo:** Stroj (masa $m = 4\ \text{kg}$, enaki vzmetni podatki kot N10: $k_{eq} = 1000\ \text{N/m}$, $\omega_0 = 15{,}81\ \text{rad/s}$) obratuje pri $n = 150\ \text{obr/min}$. Ali je nevarnost resonance?

#### Korak 1 — Kotna frekvenca vzbujevalne sile

$$\omega_{vzb} = \frac{n \cdot 2\pi}{60} = \frac{150 \cdot 2\pi}{60} = \frac{300\pi}{60} = 5\pi = \boxed{15{,}71\ \text{rad/s}}$$

#### Korak 2 — Primerjava z lastno frekvenco

$$\frac{\omega_{vzb}}{\omega_0} = \frac{15{,}71}{15{,}81} = 0{,}994 \approx 1{,}0$$

> **Razmerje blizu 1 → RESONANCA!** Amplituda brez dušenja → $\infty$. Z dušenjem → amplituda je še vedno večkratnik statičnega odmika → nevarna vibracija, utrujenostni lom!

#### Korak 3 — Praktični ukrepi

| Ukrep | Kaj naredi | Smer |
|-------|-----------|------|
| Sprememba $n$ | $\omega_{vzb}$ premakne stran od $\omega_0$ | Povečaj ali zmanjšaj rpm |
| Dodaj maso $m$ | $\omega_0 = \sqrt{k/m}$ pade | zmanjša $\omega_0$ |
| Ojači vzmetenje $k$ | $\omega_0$ naraste | odmakne $\omega_0$ od $\omega_{vzb}$ |
| Dušilnik $c$ | omeji amplitudo, ne premakne $\omega_0$ | prigušitev resonance |

**Priporočilo:** Spremenite obrate na npr. $n = 120\ \text{obr/min}$ ($\omega_{vzb} = 12{,}57\ \text{rad/s}$, razmerje = 0{,}795) ali $n = 180\ \text{obr/min}$ ($\omega_{vzb} = 18{,}85$, razmerje = 1{,}19).

> **gl.:** [[Blok 7 - Dinamika Nihanje#Prepoznavanje razlik med podtipi nalog]]

---

## "Zmagovalne kombinacije" po profesorju

```
1. KINEMATIKA → DINAMIKA (klasika izpitov BTF):
   Korak 1: Pol hitrosti → ω, v točk (Blok 6)
   Korak 2: α iz pospeškov → M = I·α (Blok 7)
   Tipično: mehanizem, izračunaj navor za pospešek

2. DINAMIKA → TRDNOST (centrifugalne sile):
   Korak 1: Newton II → dinamična sila F_din (Blok 7)
   Korak 2: NTM → dimenzioniranje gredi pod F_din (Blok 1-2)
   Tipično: gred pri visokih obratih, centrifugalna obremenitev

3. NIHANJE + VARNOST (resonanca):
   Korak 1: ω₀ = √(k/m) — lastna frekvenca stroja
   Korak 2: ω_delo = 2πn/60 — delovni obrati
   Korak 3: |ω_delo - ω₀|/ω₀ < 20% → NEVARNO
   Tipično: lesarski stroj (žaga, rezkalo, skobeljnik)

4. ENERGIJA (najelegantnejše za hitrosti):
   Brez izračuna pospeška ali vmesnih sil
   Ep₁ + Ek₁ = Ep₂ + Ek₂  (konzervativni sistem)
   Tipično: vzmet + masa, tobogan, nihalo
```

---

## Povzetek izpitnih formul

### Kinematika točke

$$a_t = \alpha \cdot R,\quad a_n = \omega^2 R = \frac{v^2}{\rho},\quad a = \sqrt{a_t^2+a_n^2}$$

$$v = \omega \cdot r, \quad \omega = \frac{2\pi n}{60}$$

### Pol hitrosti

$$v_A = \omega \cdot r_{PA} \quad \text{(razdalja od pola!)}$$

Pol = presečišče pravokotnic na $\vec{v}$ skozi vsako točko telesa.

### Coriolisov pospešek

$$a_{Cor} = 2\omega v_{rel} \quad \text{(samo ko }\omega\neq0 \text{ IN } v_{rel}\neq0\text{)}$$

### Newton II

$$\sum F = ma \quad \text{(za vsako telo posebej!)}$$

$$\sum M_O = I_O \cdot \alpha$$

### Energetski zakoni

$$A_{net} = \Delta E_k, \quad E_k + E_p = const$$

$$E_k = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2, \quad E_p = mgh + \tfrac{1}{2}kx^2$$

### Nihanje

$$m\ddot{x}+kx=0 \Rightarrow \omega_0=\sqrt{k/m}, \quad T_0=2\pi/\omega_0, \quad f_0=\omega_0/(2\pi)$$

$$\text{Resonanca: } \omega_{vzb} \approx \omega_0 \Rightarrow \text{amplitude} \to \infty$$

---

## Hierarhija zahtevnosti

```
OSNOVNE:
  ├── at, an točke (ω·R, ω²·R)
  ├── Kolo se kotali (pol = stik)
  └── Newton II — eno telo

SREDNJE:
  ├── Bat-klip (presečišče ⊥ na v)
  ├── Dve kladi z vrvico (sistem enačb)
  ├── Nihanje ω₀ = √(k/m)
  └── Rotacijska dinamika I·α = M

NAPREDNE:
  ├── Štirivezni mehanizem (posebni primeri!)
  ├── Coriolisov pospešek (ω × v_rel)
  ├── Resonanca (ω_vzb ≈ ω₀)
  └── Kinematika + Dinamika skupaj (kombinirano)
```

---

## Povezave

- [[Blok 6 - Kinematika]] ← teorija, pol hitrosti, enačbe
- [[Blok 7 - Dinamika Nihanje]] ← Newton II, nihanje, momenti inercije
- [[Blok 0 - Statika]] ← D'Alembert (dinamika → statika)
- [[Koncept - Kinematika Mehanizmi]] ← podrobna razlaga pola hitrosti
- [[Poglavje - Statika]] ← predhodni sklop
- [[Poglavje - Trdnost]] ← Dinamika + Trdnost kombinacija
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

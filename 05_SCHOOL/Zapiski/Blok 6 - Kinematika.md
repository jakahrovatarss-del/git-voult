---
tags: [mehanika, kinematika, mehanizmi, pol-hitrosti, kotaljenje, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 6 — Kinematika

## VSE ENAČBE

```
KINEMATIKA TOČKE — OSNOVE:
  v = ds/dt = ṡ       (hitrost = odvod poti)
  a = dv/dt = s̈       (pospešek = odvod hitrosti)
  ω = dφ/dt = φ̇       (kotna hitrost)
  α = dω/dt = φ̈       (kotni pospešek)
  ω = 2π·n / 60       (pretvorba iz vrtljajev/min v rad/s!)

NARAVNI KOORDINATNI SISTEM (t, n):
  at = v̇ = s̈               (tangencialni — menja velikost v)
  an = v²/ρ = ω²·R          (normalni — menja smer v, kaže PROTI centru)
  a_skupni = √(at² + an²)

HITROST točke B glede na A:
  vB = vA + ω × rAB
  |vB/A| = ω · rAB
  Smer: pravokotno na rAB

POSPEŠEK točke B glede na A:
  aB = aA + α × rAB - ω²·rAB
  Tangencialni del: at = α · r  (pravokoten na r)
  Normalni del:     an = ω² · r  (kaže PROTI središču!)

KOTNO GIBANJE:
  v = ω · r         [m/s]
  at = α · r        [m/s²]
  an = ω² · r       [m/s²]

KOLO KI SE KOTALI (brez drsenja):
  vkontakt = 0  (pol hitrosti = kontaktna točka)
  vcentra = ω · R
  vvrh = 2 · vcentra
  ω = vcentra / R

POL HITROSTI (P):
  Hitrost vsake točke ⊥ na polmer do P
  Vsi polmeri kažejo na P
  vB = ω · PB   (razdalja od pola!)

SESTAVLJENO GIBANJE (relativno + transportno):
  v_abs = v_rel + v_trans
  a_abs = a_rel + a_trans + a_Cor
  a_Cor = 2 · ω × v_rel    (Coriolisov pospešek)
  Pojavi se SAMO če: sistem se vrti (ω≠0) IN točka se relativno premika (v_rel≠0)

KINEMATIČNA VERIGA:
  i12 = ω1/ω2 = n1/n2 = z2/z1   (zobniki)
  v1 = v2   na kontaktni točki  (pas, veriga)
```

---

## Intuicija

### Fizikalna slika — "Vsako togo telo se trenutno vrti okrog neke točke"

Kinematika je gibanje brez sil — samo geometrija gibanja. Ključna intuicija:

> Vsako ravninsko gibanje togega telesa lahko v vsakem trenutku opišemo kot **vrtenje okrog neke točke** — pola hitrosti. Ta točka se premika, a v danem trenutku obstaja vedno ena.

> *Vizualizacija:* Kolo na cesti. V trenutku, ko se dotika tal, je kontaktna točka pri miru — to je pol hitrosti. Vrh kolesa se giblje 2× hitreje od centra. Vsaka točka "obkroži" pol.

**Analogija — kolesarjenje:** Kolo se kotali brez drsenja. Center se giblje naprej s $v$. Zgornja točka platišča se giblje s $2v$. Spodnja točka (kontakt z asfaltom) miruje. To je pol hitrosti.

---

### Miselni eksperiment — "Sledi točki na kolesu"

Označi točko na obodu kolesa. Ko se kolo kotali, ta točka izrisuje **cikloido** — ne kroga, ne premice. V dnu je hitrost nič, v vrhu je hitrost maksimalna. To je direktna vizualizacija, zakaj je pol hitrosti pri stiku s podlago.

**Deformiraj do ekstrema:**
- Oba konca palice se gibljeta vzporedno (translacija): pol hitrosti je v neskončnosti → nič vrtenja.
- Ena točka miruje: pol hitrosti je tam → čisto vrtenje.

---

### Zakaj enačba izgleda tako?

$$v_B = v_A + \vec{\omega} \times \vec{r}_{AB}, \qquad |v_{B/A}| = \omega \cdot r_{AB}$$

**Zakaj vektorski produkt?** Ker pri vrtenju je hitrost pravokotna na polmer. $\omega$ je kotna hitrost (smer: os vrtenja), $r$ je položajni vektor — produkt da vektor pravokoten na oba = hitrost.

**Zakaj $v_B = \omega \cdot \overline{PB}$?** Ker pol $P$ miruje ($v_P = 0$). Vsaka točka se "vrti" okrog $P$ z isto $\omega$. Hitrost je sorazmerna razdalji od pola.

> *Enote:* $[v] = [\omega] \cdot [r] = \text{rad/s} \cdot \text{m} = \text{m/s}$ ✓

---

### Mejni primeri (sanity check)

| Situacija | Pol hitrosti | Pričakuješ |
|---|---|---|
| Kolo se kotali brez drsenja | Kontaktna točka s podlago | $v_{center} = \omega R$, $v_{vrh} = 2\omega R$ |
| Čista translacija | V neskončnosti | Vse točke imajo enako hitrost |
| Čisto vrtenje okrog $O$ | V točki $O$ | $v \propto r$ od $O$ |
| Palica vpeta v $A$, $v_A = 0$ | Točka $A$ | $v_B = \omega \cdot AB$ |

---

### Veriga vzrokov → Blok 7

Kinematika dá hitrosti in pospeške → te "odzive" poveže dinamika s silami:
- $a$ iz Blok 6 → vstopi v Newton II: $F = m \cdot a$ (Blok 7)
- $\alpha$ iz Blok 6 → vstopi v rotacijsko Newton II: $M = I \cdot \alpha$ (Blok 7)

> **Povzetek:** Kinematika = geometrija gibanja. Dinamika = vzrok gibanja. Skupaj: Blok 6 + 7.

> **glej:** [[Blok 7 - Dinamika Nihanje#Intuicija]]

---

## Gibalna stanja — primerjalna tabela

| Gibalno stanje | Pogoj | $s(t)$ / $\varphi(t)$ | $v(t)$ / $\omega(t)$ | $a_t$ | $a_n$ |
|----------------|-------|----------------------|----------------------|-------|-------|
| Premočrtno enakomerno | $a = 0$ | $s = v_0 t$ | $v = v_0 = \text{const}$ | 0 | 0 |
| Premočrtno enako-pospešeno | $a = \text{const}$ | $s = v_0 t + \frac{1}{2}at^2$ | $v = v_0 + at$ | $a \neq 0$ | 0 (ker $R = \infty$) |
| Enakomerno krožno | $\omega = \text{const}$ | $\varphi = \omega t$ | $\omega = \text{const}$ | $a_t = 0$ | $a_n = \omega^2 R$ |
| Neenakomerno krožno | $\alpha \neq 0$ | $\varphi = \varphi_0 + \omega_0 t + \frac{1}{2}\alpha t^2$ | $\omega = \omega_0 + \alpha t$ | $a_t = \alpha R$ | $a_n = \omega^2 R$ |
| Harmonično (nihanje) | $\ddot{x} + \omega_0^2 x = 0$ | $x = A\cos(\omega_0 t + \phi)$ | $v = -A\omega_0\sin(\omega_0 t + \phi)$ | $a = -\omega_0^2 x$ | — |

> **Ključna razlika:** $a_n$ (normalni) menja **smer** hitrosti, $a_t$ (tangencialni) menja **velikost**. Pri premočrtnem gibanju $a_n = 0$ ker $\rho = \infty$.

> **Skupni pospešek:** $a = \sqrt{a_t^2 + a_n^2}$ — vedno pozitiven skalar; smer določi kompozicija!

> **gl.:** [[Blok 7 - Dinamika Nihanje#VSE ENAČBE]]

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "kinematika", "mehanizem", "hitrost točke"
- "pol hitrosti", "kolo se kotali"
- "kolesa, zobniki, bat"
- "kotna hitrost", "ω", "vrtenje"
- Podano: hitrosti, kotne hitrosti ali geometrija mehanizma

**Kaj je podano:**
- Hitrost enega elementa (npr. $v_A$, $\omega_1$)
- Geometrija (dolžine palic, radiji koles)
- Položaj mehanizma (kot, razdalja)

**Kaj se sprašuje:**
- Hitrost točke ($v_B$, $v_C$)
- Kotna hitrost elementa ($\omega_2$)
- Pospešek točke (tangencialni $a_t$ + normalni $a_n$)
- Pol hitrosti mehanizma

---

## Kako začeti reševati

**Metoda pola hitrosti:**

**Korak 1:** Nariši mehanizem v danem položaju (natančna skica!)

**Korak 2:** Identificiraj točke z znano hitrostjo
- Kjer je hitrost znana: nariši vektor $v$
- Kjer je hitrost nič: to je pol hitrosti

**Korak 3:** Za vsako palico: hitrost točke ⊥ na palico od pola
- Naredi pravokotnice na palice skozi znane točke
- Presečišče = pol hitrosti

**Korak 4:** Iz pola izračunaj hitrosti:
$$v_B = \omega \cdot \overline{PB}$$

---

**Kotno gibanje (kolo, zobnik):**

**Korak 1:** Identifkiraj kinematično verigo
**Korak 2:** Kontaktni pogoj: $v_{kontakt,1} = v_{kontakt,2}$
**Korak 3:** Za kotaljenje: $v_{center} = \omega \cdot R$, pol je pri stiku!

---

**Pospešek:**

$$\vec{a}_B = \vec{a}_A + \vec{a}_{B/A}^n + \vec{a}_{B/A}^t$$

- $a_{B/A}^n = \omega^2 \cdot r_{AB}$ (centripetalni, kaže v A)
- $a_{B/A}^t = \alpha \cdot r_{AB}$ (tangencialni, ⊥ na $r_{AB}$)

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Metoda |
|-----|----------------|--------|
| Enoosno vrtenje | Eno telo se vrti okrog fiksne osi | $v = \omega \cdot r$ |
| Kolo se kotali | Gibanje + vrtenje, stik s podlago | Pol = kontaktna točka |
| Drsnik + palica | "bat-klip" mehanizem, translacija + vrtenje | Pol hitrosti, vektorski seštevek |
| Zobniki | Dani zobi ali polmeri koles | $\omega_1/\omega_2 = z_2/z_1$ |
| Pospešek točke | "izračunaj pospeška" | $a = a_t + a_n$ (vektorsko!) |
| 3D mehanizem | Prostorska geometrija | Vektorski produkt $\omega \times r$ |

---

## Sestavljeno gibanje — Podrobneje

| Komponenta | Enačba | Pogoj |
|------------|--------|-------|
| $v_{abs}$ | $v_{rel} + v_{trans}$ | vedno |
| $a_{rel}$ | relativni pospešek v sistemu | vedno |
| $a_{trans}$ | $a_t^{sys} + a_n^{sys}$ | vedno |
| $a_{Cor}$ | $2\omega \times v_{rel}$ | samo če ω≠0 IN v_rel≠0 |

> ⚠️ **Coriolisov pospešek** je pravokoten na $v_{rel}$ v ravnini gibanja — pogosta napaka je pozabiti ga!

---

## Kombinacije z drugimi bloki

### Blok 6 + 7 (Kinematika + Dinamika)
Naloga: Najprej kinematika (hitrosti, pospešek), nato dinamika (sile, momenti).
1. Iz kinematike: $\alpha$, $a$
2. Vstavi v Newton II: $F = m \cdot a$, $M = I \cdot \alpha$

### Blok 6 + 0 (Kinematika + Statika)
Naloga: Mehizem v ravnovesju → virtualni pomiki.
- Princip virtualnih del: $\delta W = \sum F_i \cdot \delta s_i = 0$

### Blok 6 + 2.5 (Kinematika + Deformacije)
Redkeje — deformabilna telesa v gibanju.

---

## Tipični mehanizmi na izpitu

```
1. KOLO NA RAVNINI (kotaljenje brez drsenja):
   - Pol = stik s podlago
   - vC (vrh) = 2·vcentra
   - vA (sredina) = ω·R

2. BAT-KLIP:
   - Bat translira, pero se vrti
   - Pol pero = presek ⊥ iz A in ⊥ iz B

3. DVOJNA PALICA:
   - Dve palici, skupno tečaj v sredini
   - ω1, ω2 iz geometrije

4. ZOBNIŠKA DVOJICA:
   - ω1·r1 = ω2·r2
   - i = ω1/ω2 = r2/r1 = z2/z1
```

---

## Pogosta napaka

- Normalni pospešek je vedno usmerjen **proti** centru vrtenja (centripetalni)
- Pol hitrosti ni nujno na telesu — je lahko zunaj
- Za kotaljenje: pol = stično mesto, NE center!
- Vektori hitrosti se seštevajo **vektorsko**, ne skalarno

---

## Povezave

- [[Koncept - Kinematika Mehanizmi]] ← podrobna razlaga
- [[Blok 7 - Dinamika Nihanje]] ← naslednji korak (Newton)
- [[Blok 0 - Statika]] ← statično ravnovesje mehanizmov
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

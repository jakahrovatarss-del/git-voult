---
tags: [mehanika, statika, reakcije, paličje, trenje, 3D, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 0 — Statika

## VSE ENAČBE

```
RAVNOTEŽJE 2D (3 enačbe):
  ΣFx = 0,  ΣFy = 0,  ΣMA = 0   (moment okrog poljubne točke)

RAVNOTEŽJE 3D (6 enačb):
  ΣFx=0, ΣFy=0, ΣFz=0
  ΣMx=0, ΣMy=0, ΣMz=0

PALIČJE — METODA VOZLIŠČ:
  Za vsako vozlišče: ΣFx=0, ΣFy=0   (2 enačbi)
  Predpostavi nateg (+), tlak (-)

PALIČJE — METODA PREREZA:
  Prereži 3 palice, seštej levo → 3 enačbe
  Trik: ΣM okrog presečišča 2 neznanih palic → direktno 3. neznanka

COULOMB TRENJE:
  Ftr = μ · N     (mejno trenje)
  Ftr ≤ μs · N    (statično)
  tan(α) ≤ μs     (pogoj za nezdrs pri poševnini)

REZULTANTA PORAZDELJENE OBTEŽBE:
  q·L deluje v težišču = L/2 od roba (enakomerna q)

MOMENT PARE SIL:
  M = F · d       (d = razdalja med silama)
```

---

## Intuicija

### Fizikalna slika — "Ravnovesje je nič pospeška"

Statika je Newton II z $a = 0$. Ko je telo v miru, vsota vseh sil natanko nič — ne zato, ker sil ni, ampak ker se **izničijo**. Vsaka podpora "potisne nazaj" ravno toliko, kolikor obremenitev pritiska nanjo.

> *Vizualizacija:* Predstavljaj si konstrukcijo kot telo, ki "plava" v polju sil. Vsaka sila je puščica. Ko so vse puščice skupaj nič — telo ne gre nikamor.

**Analogija — miza s štirimi nogami:** Ko porazdeling teže ni enaka, noge prevzamejo različne dele. Odstraviš eno nogo → teža se prerazporedi. Odstraviš dve → miza pade. To je razlika med statično določenim in nedoločenim sistemom.

---

### Miselni eksperiment — "Odreži podporo"

Za vsako nalogo: miselno odreži eno podporo. Kaj se zgodi?
- Konstrukcija se premakne → podpora je statično **nujna**.
- Ostane v ravnovesju → je redundantna (statično nedoločena).

Ko pišeš FBD in ne veš, ali si kaj pozabil: **"Ali bi se telo premaknilo brez te sile?"** Če da → jo potrebuješ.

---

### Zakaj enačba izgleda tako?

$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0$$

Tri enačbe, ker ima telo v ravnini **3 prostostne stopnje**: pomik x, pomik y, zasuk. Vsaka enačba "zaklene" eno.

**Zakaj momentna enačba?** Ker sila na ročici povzroča vrtenje. $M = F \cdot r$ — enota $\text{N·m}$ = energija na radian. Momentna enačba je tista, ki locira, *kje* sila deluje. Brez nje ne bi razlikoval med silo nad podporo in silo na sredini.

> *Mejni primer — sila točno nad tečajem:* Moment te sile je nič → ne prispeva k zasuku → tečaj jo prevzame 100 %.

---

### Mejni primeri (sanity check)

| Situacija | Pričakuješ |
|---|---|
| Sila točno nad eno podporo | Ta podpora prevzame 100 %, druga 0 % |
| Sila na sredini prostoležečega | Vsaka podpora prevzame $F/2$ (simetrija) |
| Moment brez sil | Podpori prevzameta par sil $\pm M/L$ |
| Konzola z $F$ na koncu | Vpetje: reakcija $F$ gor + moment $F \cdot L$ |

---

### Veriga vzrokov → Blok 1

Reakcije iz statike so **vstopni podatek za vse nadaljnje bloke**. Ko poznaš $R_A$ in $R_B$, z metodo preseka izračunaš notranje sile $N$, $T$, $M$ — to je [[Blok 1 - NTM Diagrami|Blok 1]].

> **Povzetek:** Statika → reakcije → ki postanejo obremenitve za [[Blok 1 - NTM Diagrami|NTM diagrami]] → [[Blok 2 - Upogib|napetosti]] → [[Blok 4 - Euler Uklon|uklon]].

> **glej:** [[Blok 1 - NTM Diagrami#Intuicija]]

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "izračunaj reakcije", "podpore", "ravnotežje"
- "paličje", "palice", "palična sila"
- "trenje", "zdrs", "koeficient trenja $\mu$"
- "moment", "silo prenesi v točko"
- Podano: sile, podpore, geometrija

**Kaj je podano:**
- Konstrukcija ali telo s silami
- Vrsta podpor (členek, valj, vpetje)
- Geometrija (dolžine, koti)
- Morda: $\mu$ za trenjske probleme

**Kaj se sprašuje:**
- Reakcije v podporah $A_x$, $A_y$, $B_y$, $M_A$
- Sile v palicah (nateg/tlak)
- Pogoj za nezdrs (trenje)

---

## Kako začeti reševati

**Reakcije 2D:**

**Korak 1:** Nariši FBD (prosto telo) z vsemi silami in reakcijami

**Korak 2:** Zapiši 3 enačbe ravnovesja:
$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0$$

> **Trik:** Moment piši okrog točke, kjer se seka največ neznank — rešiš eno enačbo direktno!

**Korak 3:** Reši sistem enačb — začni z momentno enačbo (samo 1 neznanka)

**Korak 4:** Kontrola: vstavi v preostalo enačbo — mora biti = 0!

---

**Paličje — metoda vozlišč:**

**Korak 1:** Izračunaj reakcije (globalno ravnovesje)

**Korak 2:** Začni pri vozlišču z najmanj neznankami (tipično 2)

**Korak 3:** Za vsako vozlišče: $\sum F_x = 0$, $\sum F_y = 0$ → določi 2 neznani

**Korak 4:** Napreduj do naslednjega vozlišča

---

**Paličje — metoda prereza:**

**Korak 1:** Odreži konstrukcijo skozi **3 palice** (čez katere želiš sile)

**Korak 2:** 3 enačbe ravnovesja za odrezani del → direktno 3 sile

> ⚠️ **Max 3 neznane palice** v prerezu!

---

## Vrste podpor in reakcije

| Podpora | Simbol | Reakcije | Neznanke |
|---------|--------|----------|----------|
| Tečaj/pin (nepomičen) | △ | $A_x$, $A_y$ | 2 |
| Valj/drsnik (pomičen) | ○— | $B_y$ | 1 |
| Vpetje | ▬ | $A_x$, $A_y$, $M_A$ | 3 |
| Prosti konec | | — | 0 |

**Statično določena 2D:** 3 enačbe = 3 neznane reakcije

---

## Trenje — Coulombov zakon

$$F_{tr} \leq \mu_s \cdot N$$

**Pogoj za ravnovesje (ni zdrsalo):**
$$F_{delovna} \leq \mu_s \cdot N$$

**Kritični kot (naklon):**
$$\tan \alpha \leq \mu_s \quad \Leftrightarrow \quad \alpha \leq \arctan(\mu_s)$$

**Postopek:**
1. Nariši FBD, razstavi silo teže $G$ na normalo in tangencialno komponento
2. $N = G\cos\alpha$, $F_{tang} = G\sin\alpha$
3. Preveri: $G\sin\alpha \leq \mu_s \cdot G\cos\alpha$ → $\tan\alpha \leq \mu_s$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Metoda |
|-----|----------------|--------|
| Prostoležeč / konzola | Dve podpori ali vpetje | 3 enačbe |
| Paličje | "Mrežna konstrukcija", vozlišča | Vozlišče ali prerez |
| Trenje | Dan $\mu$, "zdrsne?" | Coulomb kontrola |
| 3D sistem | Prostorska geometrija | 6 enačb |
| Porazdel. obtežba $q$ | $q$ po dolžini | Rezultanta $qL$ v težišču |

---

## Kombinacije z drugimi bloki

### Blok 0 + 1 (Statika → NTM) ← **VEDNO SKUPAJ**
Vsaka NTM naloga se začne z reakcijami. Blok 0 je korak 1 za vse ostale bloke.

### Blok 0 + 4 (Statika → Uklon)
Tlačni steber: statika da $N$ (osno silo), nato Euler kontrola.

### Blok 0 + 7 (D'Alembert)
Dinamika kot "statika z inercijsko silo": $F + (-m\vec{a}) = 0$.

---

## Hitri seznam formul

```
2D:   ΣFx=0,  ΣFy=0,  ΣM=0
3D:   +ΣMx=0, ΣMy=0, ΣMz=0

PALIČJE VOZL:  ΣFx=0, ΣFy=0 po vozlišču
PALIČJE PREZ:  odreži 3 palice → ΣM okrog presečišč

TRENJE:  Ftr ≤ μN,  tan(α) ≤ μs
```

---

## Pogosta napaka

- Napačen predznak reakcije — negativen rezultat pomeni obrnjeno smer
- Pozabiti na porazdeljeno obtežbo $q$ prenesti v rezultanto $qL$ v težišče
- 3D sistem: pozabiti na vse 6 enačb
- Paličje: privzamemo nateg → negativen rezultat pomeni tlak

---

## Povezave

- [[STATIKA]] ← podrobnejše note iz predavanj
- [[Koncept - NTM Diagrami]] ← naslednji korak (notranje sile)
- [[Blok 1 - NTM Diagrami]] ← naslednji blok
- [[Blok 4 - Euler Uklon]] ← tlačni steber
- [[Blok 7 - Dinamika Nihanje]] ← D'Alembert
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]

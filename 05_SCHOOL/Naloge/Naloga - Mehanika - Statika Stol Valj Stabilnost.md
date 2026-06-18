---
tags: [mehanika, statika, ravnotežje, stabilnost, prevrnitev, kotni-pogoj]
predmet: Mehanika
datum: 2026-06-18
vir: "Profesor — 2. letnik, BTF izpit 1. feb 2019"
status: rešeno
---

# Naloga — Statika: Stol in valj (stabilnost pri guganju)

## Namen

Izračunaj reakcije v stoječem stolu in določi kritični kot nagiba $\alpha$, pri katerem se stol z osebo (valj) ravno prične prevračati nazaj.

---

## Dano

![[stol_valj_stabilnost.svg|697]]

| Oznaka | Vrednost |
|--------|---------|
| Razdalja med nogami | $d$ |
| Višina nog (sedalo) | $d$ |
| Višina naslonjala (nad sedalom) | $d$ → skupaj do vrha D: $2d$ |
| Premer valja (osebe) | $d$ → polmer $R = d/2$ |
| Teža osebe | $G$ (na en okvir: $G/2$) |
| Podpora A | Nepremičen tečaj (pin) pri $(0, 0)$ |
| Podpora B | Valj/kotalka pri $(d, 0)$ |

**Koordinate:**

| Točka | Koordinate | Opis |
|-------|-----------|------|
| A | $(0, 0)$ | zadnja noga (vrtišče) |
| B | $(d, 0)$ | sprednja noga |
| C | $(0, d)$ | stik sedala in naslonjala |
| D | $(0, 2d)$ | vrh naslonjala |
| T | $(d/2,\ 3d/2)$ | težišče valja |

> 💡 $x_T = R = d/2$ (valj ob naslonjalu), $y_T = d + R = d + d/2 = 3d/2$ (višina nog + polmer)

**Iskano:** Reakciji $A_y, B_y$ pri mirovanju; kritični kot $\alpha$ pri guganju (By=0).

---

## KORAK 1 — FBD in geometrija

Stol tvorita dve L-okvirji. Računamo za **en okvir** → teža $G/2$.

Valj s polmerom $R = d/2$ se dotika:
- sedala pri $(d/2,\ d)$ — kontaktna točka zgoraj
- naslonjala pri $(0,\ 3d/2)$ — kontaktna točka na strani

Težišče valja T leži v sredini: $x_T = d/2$, $y_T = d + d/2 = 3d/2 = 1{,}5d$.

---

## KORAK 2 — Reakcije v mirujočem stanju

**$\sum M_A = 0$** (moment okrog A):

$$B_y \cdot d - \frac{G}{2} \cdot x_T = 0 \quad \Rightarrow \quad B_y \cdot d = \frac{G}{2} \cdot \frac{d}{2}$$

$$\boxed{B_y = \frac{G}{4}}$$

**$\sum F_y = 0$:**

$$A_y + B_y - \frac{G}{2} = 0 \quad \Rightarrow \quad A_y = \frac{G}{2} - \frac{G}{4}$$

$$\boxed{A_y = \frac{G}{4}}$$

> 💡 **Intuicija:** Težišče valja je točno na $x_T = d/2$ — torej sredi razpona stola. Obe nogi nosita enak del teže.

---

## KORAK 3 — Kritični kot guganja ($\alpha$)

Ko se stol nagne nazaj za kot $\alpha$, sprednja noga B izgubi stik s tlemi ($B_y = 0$). Ravnotežje je možno le, če leži težišče T **točno navpično nad vrtiščem A**.

**Pogoj (zasuk koordinatnega sistema za $\alpha$):**

$$x_T \cos\alpha - y_T \sin\alpha = 0$$

Vstavimo $x_T = d/2$, $y_T = 3d/2$:

$$\frac{d}{2}\cos\alpha - \frac{3d}{2}\sin\alpha = 0$$

$$\frac{1}{2}\cos\alpha = \frac{3}{2}\sin\alpha$$

$$\tan\alpha = \frac{x_T}{y_T} = \frac{d/2}{3d/2} = \frac{1}{3}$$

$$\boxed{\alpha = \arctan\!\left(\frac{1}{3}\right) \approx 18{,}43°}$$

---

## KORAK 4 — Intuicija in primerjava

**Zakaj je $\alpha$ tako majhen?**

| Primer | $x_T / y_T$ | $\alpha$ | Razlaga |
|--------|------------|---------|---------|
| Nizko težišče ($y_T = x_T$) | $1/1$ | $45°$ | lahkoten stol |
| Naš stol ($y_T = 3x_T$) | $1/3$ | $18{,}43°$ | visoko naslonjalo poveča nestabilnost |

Višje kot je težišče, **manjši je kritični kot** — stol se prej preverne.

**Splošna formula:**

$$\tan\alpha = \frac{x_T}{y_T}$$

---

## Povzetek

| Korak | Formula | Vrednost |
|-------|---------|---------|
| $x_T$ | $R = d/2$ | $d/2$ |
| $y_T$ | $d + R = d + d/2$ | $3d/2$ |
| $B_y$ (mirovanje) | $\frac{G}{2} \cdot \frac{x_T}{d}$ | $G/4$ |
| $A_y$ (mirovanje) | $G/2 - B_y$ | $G/4$ |
| **$\tan\alpha$** | $x_T / y_T$ | $1/3$ |
| **$\alpha$** | $\arctan(1/3)$ | **$\approx 18{,}43°$** |

**Pogoste napake:**
- ⚠️ $y_T$ = višina nog + polmer valja — ne samo polmer!
- ⚠️ $\tan\alpha = x_T / y_T$, ne obratno ($x_T$ je manjši → $\alpha < 45°$)
- ⚠️ Dva okvira → vsak nosi $G/2$, ne $G$!
- ⚠️ Pogoj guganja: T mora biti **nad A** (ne nad B)

---

## Flashcards

Q: Kako določiš $y_T$ za valj, ki sedi na sedalu višine $d$?
A: $y_T = d_{\text{višina sedala}} + R_{\text{polmer valja}} = d + d/2 = 3d/2$.

Q: Kateri pogoj nastopi, ko se stol ravno preverne nazaj?
A: $B_y = 0$ — sprednja noga se dvigne, stol balansira na zadnji nogi A. Težišče mora biti točno nad A.

Q: Kakšna je splošna formula za kritični kot guganja?
A: $\tan\alpha = x_T / y_T$ — razmerje vodoravne in navpične oddaljenosti težišča od vrtišča.

Q: Zakaj visoko naslonjalo zmanjša stabilnost stola?
A: Veča $y_T$ ob nespremenjeni $x_T$ → manjši $\tan\alpha$ → manjši kritični kot → stol se lažje prevrne.

---

## Povezave

- [[Blok 0 - Statika]] — ravnotežje togega telesa, reakcije
- [[Cheat Sheet - Mehanika FORMULE]] — Blok 0: Ravnotežje, $\sum M_A = 0$
- [[Cheat Sheet - Mehanika Celotna]] — TIP A: Ravnotežje togega telesa
- [[Vaje - Statika - Vse vrste]] — sorodni primeri

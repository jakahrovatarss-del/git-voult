---
name: mehanika-reševanje-nalog
description: "Kako reševati mehanika naloge — korak po korak algoritmi za vsak blok, tipične napake, stil odgovarjanja"
metadata:
  node_type: memory
  type: project
---

# Mehanika — Reševanje Nalog

## Splošni stil odgovarjanja

1. **Napiši dano/iskano** — definiraj spremenljivke s simboli in enotami
2. **FBD ali skica** — vedno najprej nariši (ali opiši) prosto telo
3. **Enačbe** — zapiši splošno enačbo, nato vstavi vrednosti
4. **Vmesni rezultati** — zapiši vsak korak (ne preskakuj)
5. **Končni rezultat** v $\boxed{...}$ z enoto
6. **Preveri** — dimenzioniranje: σ_max ≤ σ_dop; ravnotežje: ΣF=0; predznak M

---

## Blok 0 — Statika

### Algoritem reakcij (2D):
1. Nariši FBD z vsemi silami in podpornimi reakcijami
2. `ΣMA = 0` (okrog podpore z največ neznankami) → direktno B_y
3. `ΣFy = 0` → A_y
4. `ΣFx = 0` → A_x (ali H_A)
5. Preveritev: `ΣMB = 0` mora biti = 0

**Tipična napaka:** Horizontalna sila (H_A pri vrtljivi podpori) v ΣFy namesto ΣFx.

### Sile pod kotom:
- Kot od **navpičnice** α: Fx = F·sin α, Fy = F·cos α
- Kot od **vodoravnice** α: Fx = F·cos α, Fy = F·sin α
- **Napaka:** Zamenjava sin/cos glede na referenčno os kota!

### Moment sile:
- M = F · d (d = ročica = pravokotna razdalja)
- Predznak: + navzgor × levo od točke, − sicer (ali z desnim pravilom)

---

## Blok 1 — NTM Diagrami

### 6-koračni algoritem:
**Korak 0:** Tip konstrukcije — ali je os zlomljena? (→ N ≠ 0)
**Korak 1:** FBD z vsemi silami (porazdeljene q, točkovne F, momenti M_0)
**Korak 2:** Reakcije (ΣFx=0, ΣMA=0→By, ΣFy=0→Ay; preveri ΣMB=0)
**Korak 3:** Definiraj prereze — na vsakem mestu spremembe obtežbe
**Korak 4:** Metoda prereza — gledamo Z LEVE (pozitivno = zgoraj):
   - N(x) = ΣFx,levo (→ pozitivno)
   - T(x) = ΣFy,levo (↑ pozitivno)
   - M(x) = Σmomentov_levo (leva stran se vrti v smeri urinega kazalca = +)
**Korak 5:** T=0 → M_max (integral T da M)
**Korak 6:** Nariši diagrame — preveri robne pogoje

### Diferencialni odnosi:
- dT/dx = −q(x) → q navzdol pomeni T pada (naklon = −q)
- dM/dx = T(x) → M je integral T
- Kjer q=0: T = konst, M = linearna
- Kjer q≠0: T = linearna, M = parabola (2. red)
- **Skok v T** pri točkovni sili F
- **Skok v M** pri skoncentriranem momentu M_0

### Oblika diagramov:
- Prosta leva ali desna točka: T=0, M=0
- Vpeta podpora: T≠0, M≠0 (reakcijski moment)
- Mmax je tam kjer T=0 (ali kjer T menja predznak)

---

## Blok 1.5 — Geometrijske karakteristike

### Postopek za sestavljeni prerez:
1. Razdeli na enostavne like (pravokotnik, krog, ...)
2. Izračunaj A_i za vsak del
3. Težišče: **y_T = Σ(A_i · y_i) / ΣA_i**  (meri od spodnjega roba)
4. Lastni vztrajnostni moment: J_xi = b·h³/12 (ali π·d⁴/64)
5. Steiner: **J_x = Σ(J_xi + A_i · d_i²)**  kjer d_i = razdalja težišča dela od skupnega težišča
6. W_y = J_x / e_max  (e_max = oddaljenost najdaljšega vlakna od osi)

### Prerezi — formule:
| Prerez | J_x | W_x |
|--------|-----|-----|
| Pravokotnik b×h | b·h³/12 | b·h²/6 |
| Krog d | π·d⁴/64 | π·d³/32 |
| Votel krog D,d | π(D⁴−d⁴)/64 | π(D⁴−d⁴)/(32D) |

**Napaka:** Steiner = A·d² (ne J·d²!). d = razdalja TEŽIŠČ, ne robov.
**Uklon:** Vedno j_min = h·b³/12 (manjša dimenzija b kubiramo!)

---

## Blok 2 — Upogib

### 7-koračni algoritem:
1. **Reakcije** — FBD, ΣMA→By, ΣFy→Ay (korak 0: statika)
2. **M-diagram** — definiraj x, zapiši M(x) po odsekih, najdi M_max kjer T=0
3. **Geometrija prereza** — y_T, J_x, Steiner
4. **Napetosti** — σ = M·e/J  (e = oddaljenost od nevtralne osi do kritičnega vlakna)
5. **Kritična vlakna** — spodaj: e_sp = y_T, zgoraj: e_zg = h − y_T
6. **Dimenzioniranje** — izpelji W_req = M_max/σ_dop, reši za b ali d, zaokroži NAVZGOR
7. **Preveri** — vstavi dimenzijo in izračunaj σ_max ≤ σ_dop

### Asimetrični prerez (U, T, C):
- σ_sp = M·e_sp/J  (sp = spodnja vlakna, e_sp = razdalja od osi do spodnjega roba)
- σ_zg = M·e_zg/J  (zg = zgornja vlakna)
- Kateri je večji = kritičen!
- Smer M določi katera vlakna so v nategu/tlaku

**Tipične napake:**
| Napaka | Prava pot |
|--------|-----------|
| Horizontalna sila v ΣFy | ΣFx=0 posebej |
| Napačen predznak rezultante | Pokaži smer s puščico |
| Steiner = J_i·d² | Steiner = A_i·d² |
| Dimenzija zaokrožena navzdol | Vedno navzgor (varnost!) |
| e = celotna višina h | e = razdalja od nevtr. osi |

---

## Blok 3 — Napetostno stanje (Mohr)

### Postopek Mohrova krog:
1. Definiraj stanje: σx, σy, τxy (pozitivno: τ na levi stranki navzgor)
2. Središče: **σ_sr = (σx + σy) / 2**
3. Polmer: **R = √( ((σx−σy)/2)² + τxy² )**
4. Glavne napetosti: **σ1,2 = σ_sr ± R**
5. Maksimalni strig: **τ_max = R**
6. Kot: **tan(2φ0) = 2·τxy / (σx−σy)**
   - φ0 = kot do ravnine z σ1 (meri od x-ravnine)

### Mohr diagram koordinatni sistem:
- Os x = σ (pozitivno DESNO = nateg)
- Os y = τ (pozitivno NAVZDOL — KONVENCIJA!)
- Točka A = (σx, τxy_navzdol), točka B = (σy, τxy_navzgor)
- Krog čez A in B s središčem S = (σ_sr, 0)

### Ravnine (orientacija):
- Ravnina σ1: brez striga (τ=0), normala pod kotom φ0
- Ravnina τ_max: pod 45° od ravnine σ1

---

## Blok 3.5 — Hipoteze Porušitve

### Tresca (maks. strig):
- **τ_max = (σ1 − σ3) / 2 ≤ τ_dop = σ_dop / 2**
- Ekvivalentna napetost: σ_ekv,Tr = σ1 − σ3

### Von Mises (deformacijska energija):
- **σ_ekv,VM = √(σ1² + σ2² + σ3² − σ1σ2 − σ2σ3 − σ1σ3) ≤ σ_dop**
- Za ravninsko stanje (σ3=0): σ_ekv = √(σ1² − σ1·σ2 + σ2²)
- Alternativno (direktno iz σx,σy,τ):
  σ_ekv = √(σx² + σy² − σxσy + 3τ²)

### Kdaj katera:
- Tresca: jeklo, konzervativnejša (varnejša)
- Von Mises: duktilni materiali, pogosteje v praksi

---

## Blok 4 — Euler Uklon

### Algoritem:
1. Določi **β** glede na vpetje:
   | Tip | β |
   |-----|---|
   | Oba členkasto | 1.0 |
   | Spodaj vpeto, zgoraj členkasto | 0.7 |
   | Oba vpeta | 0.5 |
   | Spodaj vpeto, zgoraj prosto | 2.0 |

2. **Uklonska dolžina:** lu = β · L
3. **I_min** — uklon okrog šibke osi (manjša dimenzija b kubiramo):
   - Pravokotnik: I_min = h · b³/12 (b < h!)
4. **Vztrajnostni polmer:** i = √(I_min / A)
5. **Vitkost:** λ = lu / i
6. Primerjaj z **λe** (mejnik Euler/Tetmajer):
   - λ > λe → **Euler:** F_k = π²·E·I_min / lu²
   - λ ≤ λe → **Tetmajer ali ω metoda:** F_dop = σ_dop · A / ω(λ)

### ω metoda:
- ω = f(λ, material) — beri iz tabele
- F_dop = σ_dop · A / ω  (koeficient uklona ω ≥ 1)

**Tipična napaka:** I_min = h·b³/12 ne h³·b/12 — b je MANJŠA dimenzija!

---

## Blok 5 — Torzija

### Polni krog:
- **τ = Mt / Wt**  kjer Wt = π·d³/16 = 2·Wx
- **φ = Mt · L / (G · Ip)**  kjer Ip = π·d⁴/32 = 2·Jx

### Votli prerez (Bredt):
- **τ = Mt / (2 · A_m · t)**
- A_m = ploščina zaprte srednje linije (ne materialna ploščina!)
- t = debelina stene

### Kombinirano upogib + torzija:
- σ = M / Wx (od upogiba)
- τ = Mt / Wt (od torzije)
- Vstavi v Tresca ali Von Mises za σ_ekv

---

## Kako odgovarjati na izpitu

### Format odgovora:
```
Dano: [seznam vrednosti z enotami]
Iskano: [kaj iščemo]

Korak 1: [ime koraka]
  [enačba splošno]
  [vstavi vrednosti]
  = [rezultat z enoto]

...

Rezultat: [boxed ali poudarjen]
```

### Enote:
- Sile: kN ali N
- Razdalje: cm ali m (ne mešaj v isti nalogi!)
- Napetosti: kN/cm² ali MPa (1 MPa = 1 N/mm² = 0.1 kN/cm²)
- Vztrajnostni momenti: cm⁴ ali mm⁴

### Preverjanje rezultatov:
- Upogib: σ_max ≤ σ_dop (drugače dimenzioniranje ne drži)
- NTM: Robni pogoji (M=0 na prosti podpori, T=0 na prostem koncu)
- Statika: ΣF=0 in ΣM=0 po izračunu reakcij
- Uklon: F_k > F (varnostni faktor > 1)

**Linked memories:** [[mehanika-vault-status]], [[mehanika-svg-diagrami]], [[obsidian-note-style]]

---
type: izračun
tags:
  - baterija
  - polnilnica
  - wallbox
  - roi
created: 2026-06-16
---

# Izračun - Baterija in Polnilnica

> Del projekta → [[Projekt - Sončna Elektrarna Šentjernej]]

## 20 kWh hišna baterija

### Cena (2026)
| Komponenta | Cena (ocena) |
|-----------|-------------|
| Baterija 20 kWh (hardware) | ~6.000–9.000 € |
| Hibridni inverter (če ga ni) | ~1.500–3.000 € |
| Montaža + inštalacija | ~1.000–2.000 € |
| **Skupaj** | **~8.500–14.000 €** |

Povprečna evropska cena (H2 2025): **~711 €/kWh** za rezidenčne baterije.

### Priporočene blagovne znamke
Zgornji cenovni razred (kakovost): **BYD, Pylontech, SolarEdge, Huawei**
Spodnji razred (cenovno): kitajski noname

### Dimenzije (orientacijsko)
- 20 kWh LFP baterija (npr. BYD Battery-Box Premium HV): **~57 × 76 × 13 cm**, ~115 kg
- Postavitev: zid v garaži/kotlovnici, pokončno

### Zakaj 20 kWh in ne manj?
- Touareg polnjenje: 16 kWh → baterija mora pokriti vsaj eno polno polnjenje
- Passat polnjenje: 12,5 kWh
- Skupaj: 28,5 kWh/noč — baterija 20 kWh + del direktno iz paneljev ali omrežja
- Manjša baterija (10 kWh) bi pokrila samo Passat ali polovico obojih

## Wallbox polnilnica

### Cene (hardware)
| Polnilnica | Moč | Cena |
|-----------|-----|------|
| Wallbox Pulsar Plus | 7,4–22 kW | ~500–800 € |
| ETI EVC-HOME11 | 11 kW | ~350–500 € |
| Teison Smart | 22 kW | ~400–600 € |

**Montaža + inštalacija:** +300–600 €

### Katera moč?
- **Touareg R**: max polnjenje 7,2 kW → 7,4 kW wallbox zadostuje (polnjenje ~2 h)
- **Passat GTE**: max 3,6 kW → katerikoli wallbox zadostuje (polnjenje ~3–4 h)
- **Priporočilo:** 11 kW wallbox (z rezervo za prihodnost, EVs imajo višje stopnje)

## Subvencije (2026)

### Baterija — Borzen razpis
- **Subvencija:** do **45 %** upravičenih stroškov, max **225 €/kWh**
- Upravičeni stroški: baterija, inverter, inštalacije
- ⚠️ **Rok priključka na omrežje: 31. 7. 2026** — pohiti!

### Polnilnica — Borzen/MOPE razpis
- Fizične osebe (Sklop A): do **60 %** stroškov nakupa polnilnice
- Do **50 %** stroškov montaže

## Ali se splača? (ROI baterija samostojno)

### Scenarij: samo nočna tarifa (brez sončnih panelov)
| | |
|---|---|
| Ponoči polni iz omrežja | ~0,08–0,10 €/kWh |
| Podnevi troši iz baterije (ne iz omrežja) | prihranek ~0,12 €/kWh |
| Prihranek na 20 kWh/dan | ~2–3 € → **~600–900 €/leto** |
| Cena sistema (po subvenciji ~45 %) | ~5.500–7.000 € |
| **ROI (samo baterija)** | **~7–12 let** |

### Scenarij: baterija + sončni paneli ← priporočeno
- Presežek sončne energije podnevi → shrani v baterijo → ponoči v avto + hišo
- Lastna poraba: 30 % (brez) → **70 % (z baterijo)**
- ROI celotnega sistema: **~8,5 let** (glej [[Izračun - Dimenzioniranje in ROI]])

> **Zaključek:** Brez panelov baterija sama vrne v ~7–12 letih — sprejemljivo, ne odlično. Z paneli skupaj se povratna doba prepolovi na ~8,5 let, ker drastično raste lastna poraba.

## Nočno polnjenje — logika sistema

```
[Paneli podnevi] → [Baterija 20 kWh] → [Ponoči: Touareg + Passat + hiša]
                ↗                    ↘
           [Hiša podnevi]         [Omrežje (backup, zimske noči)]
```

- **Poleti:** paneli napolnijo baterijo in hišo → zvečer polni avta brez omrežja
- **Pozimi:** 13,5 kWp da ~5–6 kWh/dan → baterija ne bo polna → omrežje dopolni razliko

## Naslednji koraki
- [ ] Preveriti Borzenov razpis za baterije — **rok 31. 7. 2026**
- [ ] Odločiti moč wallboxa (11 ali 22 kW)
- [ ] Preveriti obstoječo električno inštalacijo (trifazni priključek?)

## Povezave
- [[Projekt - Sončna Elektrarna Šentjernej]]
- [[Izračun - Dimenzioniranje in ROI]]
- [[Vir - Predpisi Sončna Elektrarna Slovenija]]

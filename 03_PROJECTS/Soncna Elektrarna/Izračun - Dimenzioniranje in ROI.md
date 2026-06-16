---
type: izračun
tags:
  - solarni-paneli
  - roi
  - dimenzioniranje
created: 2026-06-16
---

# Izračun - Dimenzioniranje in ROI

> Izračun za [[Projekt - Sončna Elektrarna Šentjernej]] — lokacija Gorenja Brezovica 21, Šentjernej (~45,8° S. g. š.)

## Donos na lokaciji

- **1.100 kWh / kWp / leto** (povprečje SLO: ~1.040; Dolenjska nekoliko bolje)
- 1 panel 450 Wp ≈ 0,45 kWp ≈ **~495 kWh/leto**
- Poleti ~3× večji donos kot pozimi — decembra le ~4–6 kWh/dan za 5 kWp

## Postavitev
| Parameter | Vrednost |
|-----------|---------|
| Azimut | **Jug** (±20° V/Z = –2–3 % le) |
| Naklon | **35°** (kompromis letni/zimski donos) |
| Alternativa | 40–45° → boljša zima, –3–5 % letno |

> ⚠️ Brez senčenja! Dimnik, drevje, sosednja streha so kritični pozimi (nizko sonce).

## Poraba vozil (iz vtičnice, +10 % izgube)
| Avto | Neto baterija | Polnjenje/polno | Električni doseg |
|------|-------------|----------------|----------------|
| Touareg R eHybrid | 14,3 kWh | ~16 kWh (do 7,2 kW) | ~35–45 km |
| Passat GTE | ~11–13 kWh | ~12,5 kWh (do 3,6 kW) | ~35–45 km |

**Za profil: 1 polnjenje/avto/dan:**
- Touareg: 16 kWh × 365 = **5.840 kWh/leto**
- Passat: 12,5 kWh × 365 = **4.563 kWh/leto**
- Skupaj: **~10.400 kWh/leto**

## Scenariji glede na frekvenco polnjenja

| Scenarij | Touareg | Passat | Letna potreba | Moč | Paneli (450 Wp) | Površina |
|---------|---------|--------|--------------|-----|----------------|---------|
| **A – oba dnevno** ← tvoj profil | 7×/tedn | 7×/tedn | ~10.400 kWh | 9,4–13,5 kWp | **21–30** | ~42–60 m² |
| B – vsak ~4×/teden | 4× | 4× | ~5.900 kWh | 5,4 kWp | 12 | ~24 m² |
| C – vsak ~3×/teden | 3× | 3× | ~4.450 kWh | 4,0 kWp | 9 | ~18 m² |

**Formula:** `letna potreba = (Touareg-polnjenj × 16 + Passat-polnjenj × 12,5) × 52`
`paneli = letna potreba ÷ 495`

## ROI po scenarijih (z baterijo, 2026)

### Predpostavke
- Montaža PV: ~1.600 €/kWp
- Baterija: ~400 €/kWh
- Cena elektrike (uvoz): **0,216 €/kWh**
- Odkup viškov v omrežje: **0,04 €/kWh** ← net metering ne velja več!
- Z baterijo + pametnim polnjenjem: **~70 % lastne porabe**
- Subvencija Borzen: **40 % naložbe** (z baterijo)
- Vrednost 1 kWh (mešano 70/30): ~0,163 €

| | **A – dnevno** | **B – 4×/teden** | **C – 3×/teden** |
|---|---|---|---|
| Sistem | 13,5 kWp + 20 kWh bat. | 5,4 kWp + 10 kWh | 4,0 kWp + 8 kWh |
| Paneli (450 Wp) | **30** | 12 | 9 |
| Letna proizvodnja | ~14.850 kWh | ~5.940 kWh | ~4.400 kWh |
| Bruto cena | **~29.600 €** | ~12.600 € | ~9.600 € |
| − subvencija (40 %) | −9.100 € | −5.050 € | −3.840 € |
| **Neto naložba** | **~20.500 €** | ~7.600 € | ~5.760 € |
| Letni prihranek | ~2.424 € | ~970 € | ~720 € |
| **ROI** | **~8,5 let** | ~7,8 let | ~8,0 let |
| Dobiček po 25 letih | **~40.000 €** | ~17.000 € | ~12.000 € |

> **Baterija IZBOLJŠA ROI:** Brez baterije (avta čez dan odsotna) lastna poraba le ~30 % → ROI ~12+ let. Z baterijo 70 % → ROI ~8,5 let. Intuicija pravilna.

### Korekcija za zamenjavo baterije
Baterijo boš verjetno enkrat zamenjal (~po 15 letih, ~4.000 €):
- ROI: ~8,5 → **~9,3 let**
- Skupni dobiček: ~40.000 → **~36.000 €** (še vedno odlično)

## Realni pomisleki

1. **Net metering ne velja več** — viške prodaš po 0,04 €, uvoziš po 0,22 €. Splača se porabiti sonce, ko sije.
2. **Avta čez dan odsotna** → brez baterije izvoziš večino sonca za drobiž. Baterija je nujna.
3. **Zima:** 13,5 kWp da decembra ~5–6 kWh/dan — komaj eno polnjenje Touarega. Poletni presežek letno izravna.
4. **Pametno polnjenje** sredi dneva (sonce → avto direktno) dvigne lastno porabo na ~80 % → ROI pod 7 let.

## Povezave
- [[Projekt - Sončna Elektrarna Šentjernej]]
- [[Izračun - Baterija in Polnilnica]]
- [[Vir - Predpisi Sončna Elektrarna Slovenija]]
- [[Solarni Koncentrator]] ← osnove sončne energije

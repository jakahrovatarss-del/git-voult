---
title: RADAR - Osnove
type: concept
category: radar-engineering
created: 2026-06-01
---

# RADAR - Osnove

## Definicija

**RADAR** = Radio Detection and Ranging  
Sistem, ki oddaja elektromagnetne valove in prejema njihove odboje od objektov. Iz časa zakasnitve odboja izračunamo razdaljo; iz Doppler spremembe frekvence izračunamo hitrost.

---

## Osnovni Princip

```
Oddajnik → Signal → Objekt → Odsev → Prejemnik → Obdelava
                                         ↓
                                    Razdalja (range)
                                    Hitrost (Doppler)
                                    Smer (angle)
```

### Tri Ključne Meritve

1. **Range** (razdalja)  
   - Merjena iz zakasnitve signala  
   - Formula: `R = c × Δt / 2` (c = hitrost svetlobe, Δt = delay)

2. **Velocity** (hitrost)  
   - Merjena iz Doppler frekvence  
   - Formula: `v = c × Δf / (2 × f₀)` (f₀ = carrier frequency)

3. **Angle** (smer)  
   - Merjena iz antenske direktnosti  
   - Phased array: elektronski steering ±45°

---

## Radar Enačba

Osnovna enačba, ki veza oddano moč, osvojeno razdaljo in velikost objekta:

```
Pr = (Pt × Gt × Gr × λ² × σ) / [(4π)³ × R⁴]
```

Kjer:
- **Pr** = received power
- **Pt** = transmitted power
- **Gt, Gr** = antenna gains (transmitter, receiver)
- **λ** = wavelength = c / f
- **σ** = radar cross-section (RCS)
- **R** = range

**Posledica**: Moč pada s **četrto** potenco razdalje → dolgo doseganje zahteva veliko moči ali velike antene.

---

## Frekvenske Pasove

| Pas | Frekvenca | Valovna Dolžina | Aplikacija |
|-----|-----------|-----------------|-----------|
| L | 1-2 GHz | 15-30 cm | Orodno, meteorološki |
| S | 2-4 GHz | 7.5-15 cm | Morski, zračni |
| **C** | **4-8 GHz** | **3.75-7.5 cm** | Vremenske radarje |
| **X** | **8-12 GHz** | **2.5-3.75 cm** | **AERIS-10 @ 10.5 GHz** |
| Ku | 12-18 GHz | 1.67-2.5 cm | Satelitski, automobilski |
| Ka | 27-40 GHz | 0.75-1.1 cm | Avtonomni vozili |

**AERIS-10 @ 10.5 GHz**:
- Pas X → dobra резолюција in penetracija
- Dostopna antenska tehnologija
- Manuals dostopne komponente

---

## Vrste Radarskih Signalov

### 1. Pulse Radar (Klasični)
```
┌─┐      ┌─┐      ┌─┐
│ │      │ │      │ │  ← Pulzi
└─┴──────┴─┴──────┴─┘
 100ns   休止 休止
```
- Preprosto, zmogljivo
- Problematiko s Doppler pri počasnim objektih

### 2. CW (Continuous Wave)
```
───────────────────── ← Neprekinjen signal
```
- Odličen Doppler
- Brez range informacije

### 3. **PLFM (Pulse Linear Frequency Modulation)** ← AERIS-10
```
┌────────┐      ┌────────┐
│ ▲      │      │ ▲      │
│  ╲    │      │  ╲    │ ← Chirpi
└────────┘      └────────┘
```
- Kombinira range in Doppler
- Pulse compression → boljša razlika
- Odporen na jamming

---

## Signal Processing Pipeline

```
1. Waveform Generation
   └─ DAC generiraj LFM chirp

2. Transmission
   └─ Up-mix na 10.5 GHz
   └─ PA ojačaj
   └─ Antena

3. Reception
   └─ Antena prejemi signal
   └─ LNA ojačaj
   └─ Mixer down-convert na IF

4. Digital Processing (FPGA)
   ├─ ADC: analog → digitalni
   ├─ I/Q demod: kompleksni signal
   ├─ Decimacija: zmanjšaj sample rate
   ├─ FFT: range bins
   ├─ Pulse compression: matched filter
   ├─ Doppler: frequency analysis
   ├─ MTI: moving target indicator
   └─ CFAR: constant false alarm rate

5. Detection
   └─ Threshold → Target list

6. Tracking & Display
   └─ Python GUI → mapa
```

---

## Ključne Lastnosti

### Range Resolution
Sposobnost razlikovanja dveh objektov na različnih razdaljah.
- Bolj kratko pulse → boljša rezolucija
- PLFM pulse compression → boljša razlika brez zmanjšanja moči

### Velocity Resolution
Sposobnost razlikovanja različnih hitrostih.
- Doppler FFT velikost vpliva na resolucijo
- Daljši čas integracije → boljša rezolucija

### Ambiguity
- **Range ambiguity**: Odboji od prejšnjega pulza
- **Doppler ambiguity**: Aliasing Doppler frekvenc
- Rešitev: PRF (Pulse Repetition Frequency) izbira

### Clutter & Jamming
- **Clutter**: Neželeni signali (tla, čeženje)
- **Rešitev**: MTI (Moving Target Indicator), CFAR
- Jamming: Elektronska vojna zaščita

---

## Polarizacija

- **H (Horizontal)**: Valovi polarizacijski v horizontalni ravnini
- **V (Vertical)**: Valovi polarizacijski v vertikalni ravnini
- **Circular**: Zarotacijski polovi

AERIS-10 tipično uporablja **V ali H** za enostavnost.

---

## Antenske Koncepti

### Smer (Directivity)
- **Beam pattern**: Kako antena severi moč v različne smeri
- **Main lobe**: Osrednja smer
- **Side lobes**: Neželeni signali v stranski smeri
- **Gain**: Ojačanje v smeri maksimalne smer

### Phased Array
- Več antenvnih elementov
- Kontrolira faze med elementi → elektronski steering
- Brez mehanskega gibanja

### Beamforming
- Usmerjanja žarka z regulacijo faza
- AERIS-10: ADAR1000 phase shifterji

---

## Doppler Efekt

Ko se objekt premika proti radarjem:
- Frekvenca se **poveča**
- Valovna dolžina se **skrajša**

Ko se objekt premika stran:
- Frekvenca se **zmanjša**
- Valovna dolžina se **podaljša**

```
Doppler frekvence:
fd = 2 × v × f₀ / c

v = hitrost objekta
f₀ = oddajne frekvence (10.5 GHz za AERIS-10)
c = hitrost svetlobe
```

---

## Praktični Primeri

### Premikajući Avtomobil
- Range: 100 m
- Hitrost: 20 m/s (72 km/h)
- Doppler frekvence: fd = 2 × 20 × 10.5e9 / 3e8 ≈ 1.4 kHz
- Lahko razlikujemo od clutter-ja

### Uletajoči Objekt
- Range: 500 m
- Hitrost: 100 m/s (360 km/h)
- Doppler frekvence: fd ≈ 7 kHz
- Jasna detekcija

### Stacionarni Objekt
- Range: 200 m
- Hitrost: 0 m/s
- Doppler frekvence: 0 Hz
- Težko razlikovati od clutter-ja — potreben MTI!

---

## Naslednji Koraki

1. [[Phased Array Antenna]] — Kako deluje fazni niz
2. [[PLFM Modulacija]] — Kako AERIS-10 modulira signal
3. [[Signal Processing - RADAR]] — Kako obdelamo surove podatke

---

## Povezava

[[Tema - RADAR Inženiring]] | [[Projekt - PLFM RADAR]] | [[Phased Array Antenna]] | [[PLFM Modulacija]]

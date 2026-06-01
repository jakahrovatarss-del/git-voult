---
title: Vir - PLFM RADAR GitHub
type: resource
category: open-source-hardware
created: 2026-06-01
---

# Vir - PLFM RADAR GitHub

## Osnovni Podatki

**Repo**: https://github.com/NawfalMotii79/PLFM_RADAR  
**Avthor**: Nawfal Motii  
**Status**: Active Development (v2.0.2)  
**License**: Hardware (CERN-OHL-P) | Software (MIT)  
**Stars**: 19.7k | **Forks**: 4.7k

---

## Namen

AERIS-10 je open-source, low-cost 10.5 GHz fazni niz radar s PLFM modulacijo. Namenjen je raziskovalcem, razvojcem dronov in SDR navdušencem, ki želijo eksperimentirati z beamforming, pulse compression, Doppler processing in target tracking.

---

## Dva Modela

### AERIS-10N (Nexus)
- **Range**: do 3 km
- **Antenna**: 8×16 patch array
- **Output Power**: ~1W×16 kanali
- **Use Case**: Kratko-dosegne aplikacije, raziskave

### AERIS-10E (Extended)
- **Range**: do 20 km
- **Antenna**: 32×16 slotted waveguide
- **Output Power**: 10W×16 (GaN amplifiers)
- **Use Case**: Dolgo-dosegne aplikacije, profesionalne sisteme

---

## Struktura Repozitorija

| Folder | Vsebina | Napomena |
|--------|---------|----------|
| `1_Project_Description` | Pregled, specifikacije, motivacija | Start here |
| `2_Functional Diagram` | Blokovni diagrami, međusobne povezanosti | Arhitektura |
| `3_Power Management` | Napajalni načrti, sekvencioniranje | Kritično za assembly |
| `4_Schematics & Boards` | Sheme (PDF), PCB layout, production files | Production ready |
| `5_Simulations` | MATLAB, Python simulacije scenarijev | FPGA testing |
| `6_Application Notes` | Priročniki, bring-up guide, troubleshooting | Praktično |
| `7_Components Datasheets` | PDFs — AD9523, ADF4382, ADAR1000, itd. | Referenca |
| `8_Utils` | Mehanske risbe, antenske datoteke, slike | CAD files |
| `9_Firmware` | FPGA (VHDL/Verilog), STM32 (C), Python GUI | Izvršna koda |
| `docs/` | GitHub Pages dokumentacija | Published docs |

---

## Ključne Komponente

### Frekvenska Sinhronizacija
- **AD9523-1**: Clock generator (low jitter) — ključna!
- **ADF4382**: Frequency synthesizer (2×) za RX & TX
- Sinhronizacija zagotavlja phase coherence

### Signal Processing (FPGA)
- **Xilinx XC7A50T**: Čipset (FTG256)
- Obdelava:
  - DAC → PLFM chirp generacija
  - Mixer → IF down-conversion
  - ADC → Raw data capture
  - I/Q demod, decimacija, filtriranje
  - FFT, pulse compression
  - Doppler, MTI, CFAR

### Microcontroller (STM32F746)
- **Nadzor**: Power sequencing, periferike
- **Interfejsi**: AD9523, ADF4382, ADAR1000, GPS, IMU
- **Oddajanje**: Podatkov STM32 → FPGA (USB, SPI)

### Beamforming
- **ADAR1000**: 4-channel phase shifter (4× za RX/TX)
- **ADTR1107**: Low Noise Amp (RX) & Power Amp (TX) — 16× skupaj
- Elektronski steringž ±45° elevacija in azimut

---

## Kako Začeti

### 1. Razumevanje Arhitekture
Preberi: `1_Project_Description/README.md` in `2_Functional Diagram`

### 2. Preučiti Hardware
- Seme: `4_Schematics/4_6_Schematics/`
- Podatkovne liste: `7_Components Datasheets/`
- Production files: `4_Schematics/4_7_Production Files/` (BOM, CPL, Gerber)

### 3. Preučiti Firmware
- FPGA: `9_Firmware/9_2_FPGA/` (VHDL/Verilog)
- STM32: `9_Firmware/9_1_MCU/` (C)
- GUI: `9_Firmware/9_3_GUI/` (Python)

### 4. Simulacije
- `5_Simulations/` — Python/MATLAB skripte
- Testiraj signal processing algoritme

### 5. Dokumentacija
- `docs/` — GitHub Pages (lepo formatiran)
- Brings-up guide, test reports

---

## Licenca

**Hardware (Seme, PCB, mehanske risbe)**:
- **CERN-OHL-P** (Open Hardware Licence v2 Permissive)
- Lahko prodaš produkte — ohrani copyright, deli spremembe
- Bolj primerna za hardware kot MIT

**Software (Firmware, skripte)**:
- **MIT License**
- Polna fleksibilnost

**Zakaj sprememba?**
- Originalno MIT za vse
- Skupnost je opozorila, da MIT nima zaščite za hardware
- CERN-OHL-P je standard v open hardware zajednici

---

## Praktični Koraki za Projektni Vozel

### Za Razvojce FPGA
- Pregledaj `9_Firmware/9_2_FPGA/`
- Razumej signalno obdelavo pipeline
- Testiraj modulete z Python simulacijami

### Za Hardware Inženirje
- Preučiti power management (`3_Power Management`)
- Razumeti clock distribution (`AD9523-1`)
- Analizirati impedance in layout

### Za Firmware/Software Razvojce
- STM32 boot sequence (`9_Firmware/9_1_MCU`)
- I2C/SPI periferike
- USB komunikacija

### Za Raziskovalce
- Simulacije za proof-of-concept
- Beamforming eksperimenti
- Target tracking algoritmi

---

## Ključne Datoteke za Tebe

```
MANDATORY:
├── 1_Project_Description/README.md
├── 2_Functional Diagram/*
├── 4_Schematics/4_6_Schematics/*
├── 9_Firmware/9_2_FPGA/
└── docs/

OPTIONAL (Po Potrebi):
├── 5_Simulations/
├── 6_Application Notes/
└── 7_Components Datasheets/
```

---

## Kaj Boš Naučil

**Koncepti**:
- Fazni nizav in beamforming
- PLFM modulacija
- Signalna obdelava (FFT, Doppler, CFAR)
- Real-time FPGA obdelava

**Skills**:
- Razumevanje radarskih sistemov
- FPGA dizajn & VHDL
- Embedded C (STM32)
- Python signal processing

**Praktična Uporaba**:
- Drone tracking
- Search & rescue radar
- Weather radar
- Autonomous vehicles

---

## Povezave

[[Projekt - PLFM RADAR]] | [[Tema - RADAR Inženiring]] | [[RADAR - Osnove]] | [[FPGA Development]] | [[04_RESOURCES]]

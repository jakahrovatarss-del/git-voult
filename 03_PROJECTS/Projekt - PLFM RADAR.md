---
title: Projekt - PLFM RADAR
type: project-hub
created: 2026-06-01
status: active
---

# Projekt - PLFM RADAR

## Namen

AERIS-10 je open-source, low-cost 10.5 GHz fazni niz radar s Pulse Linear Frequency Modulation (PLFM) tehnologijo. Namen je demokracije radarskega inženiringa za raziskovalce, razvijalce dronov in navdušence SDR tehnologije.

**Tvoj cilj**: Razumeti arhitekturo sistema, signalno obdelavo in praktične aplikacije za beamforming in target tracking.

---

## Ključni Koncepti

- [[RADAR - Osnove]] — kaj je radar in kako deluje
- [[Phased Array Antenna]] — elektronski nadzor žarka
- [[PLFM Modulacija]] — Pulse Linear Frequency Modulation
- [[Signal Processing - RADAR]] — obdelava radarskega signala
- [[Beamforming]] — направa in steuerung žarka
- [[Target Detection]] — kako radarsko odkrijemo cilje

---

## Arhitektura Sistema

Projekt ima modularno strukturo z 9 glavnimi komponentami:

1. **Power Management** — napajanje in sekvencioniranje
2. **Frequency Synthesizer** — takt in referenca (AD9523-1, ADF4382)
3. **Main Board** — DAC, mixerji, phase shifterji, FE čipi
4. **FPGA (Xilinx XC7A50T)** — signalna obdelava v realnem času
5. **Microcontroller (STM32F746)** — nadzor periferije, GPS, IMU
6. **Antenna Array** — 8x16 ali 32x16 patch/slotted waveguide
7. **Power Amplifiers** — 10W GaN ojačevalci (samo AERIS-10E)
8. **Python GUI** — uporabniški vmesnik z mapami
9. **Firmware & Software** — VHDL, STM32 C, Python

---

## Struktura Repozitorija

```
1_Project_Description      — Opis in specifikacije
2_Functional Diagram       — Blokovni diagrami in matrične povezav
3_Power Management         — Napajalni načrti
4_Schematics and Boards    — Sheme in PCB layout
5_Simulations              — MATLAB/simulacijske datoteke
6_Application Notes        — Priročniki in vodniki
7_Components Datasheets    — Podatkovno liste komponent
8_Utils                    — Mehanske risbe, slike, antene
9_Firmware                 — FPGA (VHDL/Verilog) in STM32 (C)
docs/                      — GitHub Pages dokumentacija
```

---

## Glavne Komponente

### Hardware

| Komponenta | Funkcija | Status |
|-----------|----------|--------|
| AD9523-1 | Clock generator | ✓ |
| ADF4382 | Frequency synthesizer (2x) | ✓ |
| XC7A50T | FPGA signal processing | ✓ |
| STM32F746 | Microcontroller management | ✓ |
| ADAR1000 | 4-channel phase shifter (4x) | ✓ |
| ADTR1107 | Front-end amp (16x) | ✓ |
| LTC5552 | Mixer up/down conversion (2x) | ✓ |
| QPA2962 | 10W GaN amplifier (AERIS-10E) | ✓ |

### Signal Processing Pipeline (FPGA)

- DAC → LFM chirp generation
- Mixer → Up/down conversion
- ADC → Raw data capture
- I/Q Demod → Baseband extraction
- Decimation & Filtering → CIC/FIR
- Pulse Compression → Matched filter
- Doppler FFT → Velocity estimation
- MTI & CFAR → Target detection

---

## Učni Koraki

### Faza 1: Osnove (Teden 1-2)
- [ ] Razumeti [[RADAR - Osnove]]
- [ ] Študirati [[PLFM Modulacija]]
- [ ] Preučiti [[Phased Array Antenna]]
- [ ] Pregled ključnih komponent

### Faza 2: Arhitektura (Teden 3-4)
- [ ] Preučiti `1_Project_Description`
- [ ] Analiza power management (`3_Power Management`)
- [ ] Razumeti functional diagram (`2_Functional Diagram`)
- [ ] Študirati FPGA pipeline

### Faza 3: Hardware (Teden 5-6)
- [ ] Pregled shem (`4_Schematics`)
- [ ] PCB layout analiza
- [ ] Komponentne datoteke (`7_Components Datasheets`)
- [ ] Assembly guide

### Faza 4: Software & FPGA (Teden 7-8)
- [ ] VHDL signal processing (`9_Firmware/9_2_FPGA`)
- [ ] STM32 firmware (`9_Firmware/9_1_MCU`)
- [ ] Python GUI (`9_Firmware/9_3_GUI`)

### Faza 5: Simulacije & Testing (Teden 9-10)
- [ ] Simulacije (`5_Simulations`)
- [ ] Application notes (`6_Application Notes`)
- [ ] Praktični testi

---

## Viri

**GitHub Repo**: https://github.com/NawfalMotii79/PLFM_RADAR

**Ključne Datoteke**:
- README.md — Pregled
- docs/ — Dokumentacija
- Contributing.md — Pravila

**Licence**:
- Hardware: CERN-OHL-P
- Software: MIT

---

## Napredek

- **Status**: Active Learning
- **Trenutna Faza**: Osnove
- **Naslednji Korak**: Study Plan za signal processing

---

## Povezave

[[RADAR - Osnove]] | [[Phased Array Antenna]] | [[PLFM Modulacija]] | [[FPGA Development]] | [[06_LEARNING/Learning Hub]]

---
title: Study Plan - RADAR Inženiring
type: study-plan
duration: 10 tednov
created: 2026-06-01
status: active
---

# Study Plan - RADAR Inženiring

## Namen

Strukturiran 10-tedni plan za razumevanje RADAR inženiringa in AERIS-10 sistema. Fokus na kombinaciji teorije in praktične implementacije.

---

## Pregled

| Teden | Tema | Fokus | Projekt |
|-------|------|-------|---------|
| 1-2 | RADAR Osnove | Koncepti, frekvence | - |
| 3-4 | Antene & Beamforming | Phased array, steering | Simulation |
| 5-6 | Signalna Obdelava | FFT, Doppler, CFAR | Python scripts |
| 7-8 | Hardware AERIS-10 | Komponente, arhitektura | Analiza shem |
| 9-10 | FPGA & Integration | VHDL, pipeline | Review kode |

**Skupaj**: ~150 ur aktivnega učenja + 50 ur praktičnega dela

---

## TEDEN 1-2: RADAR Osnove

### Cilji
- [ ] Razumeti kako deluje radar
- [ ] Poznati osnovne enačbe
- [ ] Poznati 10.5 GHz frekvensni pas

### Učna Gradiva
- [[RADAR - Osnove]] (preberi in povzemi)
- Skolnik "Introduction to Radar Systems" — Chapters 1-3
- AERIS-10 README

### Praktične Naloge
- [ ] Skiciraj blokni diagram radarja
- [ ] Izračunaj range iz delay časa
- [ ] Razumej radar equation

### Vprašanja
1. Kako se razlikuje radar od komunikacijskega sistema?
2. Kaj je range resolution?
3. Zakaj AERIS-10 uporablja 10.5 GHz?

### Naslednji Korak
→ Teden 3: Antene

---

## TEDEN 3-4: Antene & Beamforming

### Cilji
- [ ] Razumeti fazne nizove
- [ ] Študirati beamforming matematiko
- [ ] Razumeti ADAR1000 chip

### Učna Gradiva
- [[Phased Array Antenna]] (ključna nota)
- [[Beamforming]] (principi)
- Blaunstein — "Phased Array Antennas"
- ADAR1000 datasheet (`7_Components Datasheets`)

### Praktične Naloge
- [ ] Simuliraj 2D fazni niz v Python
- [ ] Izračunaj phase shift za steering angle
- [ ] Razumej AERIS-10 antenseko konfiguracija (8x16 vs. 32x16)

### Mini Projekt
→ [[Mini Projekt - Phased Array Simulation]]

### Vprašanja
1. Kako phase shifter vpliva na main lobe smer?
2. Kaj je side lobe in kako ga zmanjšamo?
3. Kako ADAR1000 upravlja faze 4 kanalov?

---

## TEDEN 5-6: Signalna Obdelava

### Cilji
- [ ] Razumeti LFM modulacijo
- [ ] Implementirati pulse compression
- [ ] Poznavati FPGA pipeline

### Učna Gradiva
- [[PLFM Modulacija]] (ključna nota)
- [[Signal Processing - RADAR]] (detaljno)
- Stimson — "Introduction to Airborne Radar" — Chapters 4-6
- AERIS-10 `6_Application Notes`

### Praktične Naloge
- [ ] Generiraj LFM chirp v Python
- [ ] Implementiraj matched filter
- [ ] Izračunaj range-Doppler mapo
- [ ] Razumej CIC filter iz shem

### Mini Projekt
→ [[Mini Projekt - LFM Chirp Generator]]

### Vprašanja
1. Kako pulse compression izboljša range resolution?
2. Kaj je Doppler frequency in kako se izmeri?
3. Kako MTI suprira clutter signale?

---

## TEDEN 7-8: Hardware AERIS-10

### Cilji
- [ ] Razumeti glavne komponente
- [ ] Preučiti power management
- [ ] Analizirati signalni tok

### Učna Gradiva
- Projekt dokumetnacija `1_Project_Description`
- Seme in blokovni diagrami `2_Functional Diagram`
- Power management `3_Power Management`
- Seme `4_Schematics`

### Praktične Naloge
- [ ] Skiciraj power tree (napajalne nivoje)
- [ ] Razumej AD9523-1 clock generator
- [ ] Razumej ADF4382 frequency synthesizer
- [ ] Analiziraj mixerja (LTC5552)
- [ ] Preučiti PA (QPA2962) za AERIS-10E

### Analiza Shem
→ [[Analiza - AERIS-10 Main Board Shema]]

### Vprašanja
1. Zakaj je AD9523-1 kritična za timing?
2. Kako se ADF4382 sinhronizira z FPGA?
3. Kaj je razlika med AERIS-10N in AERIS-10E?

---

## TEDEN 9-10: FPGA & Integration

### Cilji
- [ ] Razumeti VHDL/Verilog kodo
- [ ] Preučiti signalno obdelavo FPGA
- [ ] Razumeti STM32 vlogo

### Učna Gradiva
- FPGA firmware `9_Firmware/9_2_FPGA`
- STM32 firmware `9_Firmware/9_1_MCU`
- Vivado design flow
- AERIS-10 docs

### Praktične Naloge
- [ ] Preučiti VHDL FFT modul
- [ ] Razumeti I/Q demodulator
- [ ] Slediti podatkovnemu toku FPGA
- [ ] Razumeti STM32 register configuration
- [ ] Preučiti komunikacijo STM32-FPGA (SPI/I2C)

### Code Review
→ [[Review - AERIS-10 FPGA Pipeline]]

### Vprašanja
1. Kako je FFT implementirana v FPGA?
2. Kaj je razlika med pipelining in parallelizem?
3. Kako se sinhronizira STM32 z FPGA?

---

## Hiter Pregled Dnevno

```
Ponedeljek    | Branje teorije + predavanja
Torek-Četrtek | Praktične naloge
Petek         | Mini projektni korak
Sobota-Nedelja| Povzetek + refleksija
```

**Čas po dnevu**: 3-4 ure učenja, 1-2 uri prakse

---

## Refleksija & Prilagoditve

**Po Tednu 2**: Preveri razumevanje → adjust tempo
**Po Tednu 4**: Preveri beamforming skills → potrebuješ simulacijo?
**Po Tednu 6**: Preveri signal processing kodo → hands-on?
**Po Tednu 8**: Preveri hardware znanje → kaj te zbega?
**Po Tednu 10**: Final assessment → kaj je naprej?

---

## Naslednji Koraki (Po Planu)

- Praktična implementacija na pravo hardware
- Embedded development na STM32
- FPGA board bring-up
- Target detection algoritmi
- Multi-target tracking

---

## Viri v Vaultu

| Nota | Namena |
|------|--------|
| [[RADAR - Osnove]] | Teoretični temelj |
| [[Phased Array Antenna]] | Antenska teorija |
| [[PLFM Modulacija]] | Signalni koncept |
| [[Signal Processing - RADAR]] | Obdelava |
| [[FPGA Development]] | Implementacija |
| [[Projekt - PLFM RADAR]] | Praktični kontekst |

---

## Povezave

[[Tema - RADAR Inženiring]] | [[Skill Tree - RADAR Signalna Obdelava]] | [[Projekt - PLFM RADAR]] | [[06_LEARNING/Learning Hub]]

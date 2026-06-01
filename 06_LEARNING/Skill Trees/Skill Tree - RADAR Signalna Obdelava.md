---
title: Skill Tree - RADAR Signalna Obdelava
type: skill-tree
created: 2026-06-01
---

# Skill Tree - RADAR Signalna Obdelava

## Namen

Vizualizacija progresa pri učenju signalne obdelave za RADAR sisteme. Fokus na praktične veščine za razumevanje AERIS-10 FPGA pipeline.

---

## Nivo 1: Osnove Signalov

**Trajanje**: 5 dni

### Skills
- [ ] Kompleksna števila in I/Q reprezentacija
- [ ] Sampling teorija (Nyquist, aliasing)
- [ ] Diskretna Fourier transformacija (DFT/FFT)
- [ ] Filtriranje (CIC, FIR, IIR)

### Mini Projekt
→ [[Mini Projekt - Python FFT Analiza]]

### Vprašanja za Samopreverjanje
- Kaj je I/Q reprezentacija in zakaj je potrebna?
- Kako Nyquist teorija vpliva na radar sample rate?
- Kaj je razlika med DFT in FFT?

---

## Nivo 2: Radar Signali

**Trajanje**: 7 dni  
**Pogoj**: Nivo 1 ✓

### Skills
- [ ] LFM (Linear Frequency Modulation) chirpi
- [ ] Pulse compression tehnike
- [ ] Matched filter koncept
- [ ] Range resolution koncept

### Mini Projekt
→ [[Mini Projekt - LFM Chirp Generation]]

### Praktična Naloga
- Generiraj LFM chirp v Python
- Simuliraj matched filter
- Izračunaj range resolution

---

## Nivo 3: Doppler & Velocity

**Trajanje**: 7 dni  
**Pogoj**: Nivo 2 ✓

### Skills
- [ ] Doppler efekt in frekvence premikov
- [ ] Velocity estimation iz Doppler
- [ ] Range-Doppler mapa
- [ ] Clutter supreija

### Mini Projekt
→ [[Mini Projekt - Range-Doppler Mapa]]

### Test Vprašanja
- Kako se izračuna hitrost iz Doppler?
- Kaj je ambiguity problem v radarih?
- Kako MTI suprira clutter?

---

## Nivo 4: Detection & CFAR

**Trajanje**: 7 dni  
**Pogoj**: Nivo 3 ✓

### Skills
- [ ] CFAR (Constant False Alarm Rate)
- [ ] Threshold calculation
- [ ] Probability of detection vs. false alarm
- [ ] Radar equation

### Mini Projekt
→ [[Mini Projekt - CFAR Implementacija]]

### Praktična Naloga
- Implementiraj CFAR v Python
- Testiraj z simuliranimi signali
- Optimiziraj za različne scenes

---

## Nivo 5: FPGA Implementacija

**Trajanje**: 14 dni  
**Pogoj**: Nivo 4 ✓

### Skills
- [ ] VHDL basic syntax
- [ ] Pipelining in FPGA
- [ ] Fixed-point arithmetic
- [ ] AERIS-10 FPGA pipeline razumevanje

### Projekt
→ [[Projekt - FPGA Signal Processing]]

### Praktična Naloga
- Preučiti AERIS-10 VHDL kodo
- Implementirati simple FFT modul
- Testirati na hardware

---

## Nivo 6: Full Integration

**Trajanje**: 14 dni  
**Pogoj**: Nivo 5 ✓

### Skills
- [ ] End-to-end radar processing pipeline
- [ ] STM32 mikrokontroler integracija
- [ ] Python GUI kompatibilnost
- [ ] Beamforming & target tracking

### Final Projekt
→ [[Projekt - AERIS-10 Sistem Integracija]]

---

## Trenutni Status

- **Nivo**: 1 (Začetnik)
- **Napredek**: 0%
- **Naslednji Korak**: Kompleksna števila & FFT

---

## Refleksija

Presežki:
- Razumeš osnovne koncepte

Izzivi:
- FPGA je nov terrain
- Real-time obdelava je zahtevna

Kaj Boš Potem Naredil:
- Mini projekti za utrditev
- Praksa s pravim hardware-om

---

## Povezave

[[Tema - RADAR Inženiring]] | [[PLFM Modulacija]] | [[Signal Processing - RADAR]] | [[FPGA Development]] | [[Projekt - PLFM RADAR]]

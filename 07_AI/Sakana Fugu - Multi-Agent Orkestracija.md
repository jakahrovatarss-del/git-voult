---
created: 06/24/2026
categories:
  - "[[07_AI/AI Orkestracija]]"
rating: 7
tags:
  - 1🌲
related-to:
  - "[[06_LEARNING/Solo Ucenje]]"
  - "[[06_LEARNING/Feynmanova Tehnika]]"
---

# Kaj je

**Sakana Fugu** je multi-agent orkestracijski sistem iz Tokia, ki združuje več frontier modelov v en OpenAI-compatible API klic. Namesto enega samega modela, dinamično usmerja naloge na najbolj primernega izmed bazena modelov — in s tem doseže rezultate primerljive z najboljšimi posameznimi modeli (Fable 5, Mythos Preview).

Temelji na dveh raziskavah (ICLR 2026): **TRINITY** (evolved coordinator) in **The Conductor** (RL-treniran workflow design).

# Kako deluje

## Selection head

Lightweight arhitekturni element za hitro izbiro pravega worker modela. Namesto generiranja teksta, izračuna **logite** — surove skorje za vsakega modela:

```
Vprašanje → [LM Backbone] → h (hidden state)
                                  |
               +------------------+------------------+
               |                                     |
          [LM Head]                      [Selection Head]
        (generira tekst)                      |
                                         L logits → argmax → dispatch
```

Logiti so **10-100x hitrejši** kot generiranje teksta → skoraj ničelna latenca. Uči se z **SFT** (KL divergence na mehki tarčni distribuciji) in **SVD adaptacijo** (le majhen nabor parametrov).

## Dva stadija treninga

1. **SFT** — za naloge z znanim odgovorom: softmax iz rewardov workerjev → mehka ciljna distribucija
2. **sep-CMA-ES** — za multi-turn naloge brez vmesnega signala: evolucijska strategija brez gradientov, generira kandidate in jih premika proti najboljšim

## Fugu vs Fugu Ultra

| Karakteristika | Fugu | Fugu Ultra |
|----------------|------|------------|
| Cilj | Hitrost + kakovost | Maksimalna kakovost |
| Delavcev | En | Več (cel workflow) |
| Hitrost | ≈ en model | Počasnejši |
| Za koga | Coding, chatbots | Kaggle, cybersecurity, raziskava |

Fugu Ultra piše celoten **agentic workflow** — za vsak korak določi podnalogo, worker ID in access list. Podpira veriženje, Best-of-N in drevesne strukture.

# Benchmarki

| Benchmark | Fugu Ultra | Fugu | Najboljši konkurent |
|-----------|-----------|------|---------------------|
| **LiveCodeBench** | **93.2** | 92.9 | Fable: 89.8 |
| **GPQA-D** | **95.5** | 95.5 | Mythos: 94.6 |
| **SWE-Bench Pro** | **73.7** | 59.0 | Fable 5: 80.0 |
| **TerminalBench** | **82.1** | 80.2 | Opus 4.8: 74.6 |

Fugu zmagoval na **multi-step kompleksnih nalogah**, zaostaja pa pri **brute-force single-domain reasoning** (kjer so največji standalone modeli še vedno boljši).

# Zakaj je to pomembno

- **Vendor lock-in hedging** — če en model propade, orkestracija preživi
- **Specializacija** — različni modeli najboljši na različnih področjih
- **Compliance** — možnost izločiti providerje iz routanja
- **Cost-performance** — cenejši modeli za enostavne naloge, drage le za težke

# Omejitve

- **Ni na voljo v EU/EEA** — čaka na GDPR compliance
- Proprietarni sistem — kateri modeli se uporabljajo je skrito (IP)
- Notranji orkestracijski tokeni se štejejo v ceno (ne absorbirani)

# Viri

- [Sakana Fugu uradna stran](https://sakana.ai/fugu/)
- [VentureBeat](https://venturebeat.com/orchestration/no-claude-fable-5-no-problem-sakana-achieves-frontier-performance-with-new-fugu-multi-model-auto-synthesis-system)
- [Outcome School Technical Report](https://outcomeschool.com/blog/decoding-sakana-fugu)
- [Paper: arxiv.org/abs/2606.21228](https://arxiv.org/abs/2606.21228)

# Povezano

- [[06_LEARNING/Solo Ucenje]] — kontekst za AI orkestracije
- [[06_LEARNING/Feynmanova Tehnika]] — globoko razumevanje ML konceptov

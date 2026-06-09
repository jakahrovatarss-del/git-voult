---
created: 06/07/2026
tags:
  - 0🌲
related-to:
  - "[[DeepSeek V4 - Infrastruktura]]"
  - "[[MoE]]"
---

# DeepSeek V4 — MoE

V4 uporablja **MoE (Mixture of Experts)** za feed-forward plasti, kar privede do izrednih strokovnih koristih.

## Težave pri MoE

- **Komunikacija je dragokratja:** dispečiranje tokenov na GPU-je in nazaj je dražje od izračuna
- **Bottleneck:** GPU čaka na komunikacijo ali izračun — ne more oba hkrati

## Rešitev

- **Fuzijski mega-kernel:** združuje pipelining, delno prekrivanje operacij in mozaik v en operacijski jedro
- **Fina-granulacija:** obdela majhne batch-e in jih pretaka skozi eksperte brez čakanja

## Rezultat

- Višja prehranskost
- Manjšo zakasnitev
- Manjša raba komunikacijskih kanalov

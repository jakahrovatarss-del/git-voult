---
created: 06/07/2026
tags:
  - 0🌲
related-to:
  - "[[Transformer arhitektura]]"
  - "[[MoE]]"
  - "[[Kvantizacija]]"
  - "[[Attencija]]"
---

# DeepSeek V4 — Infrastruktura

Video **bycloud** (26 min) razlaga, zakaj je DeepSeek V4 učinkovit predvsem zaradi celostne inženirske optimizacije, ne samo novih vzorcev pozornosti. Ključna ideja: pri omejenem compute moraš optimizirati celotno pot, ne samo posamezne komponente.

## Poudarki

- **Omejen compute** privede do ročne implementacije, če obstaja boljša pot
- **CSA + HCA** so samo vidna plat optimizacije; resnica je v uinkovitosti celotne poti pozornosti
- **MoE** odpade zaradi komunikacijskih stroškov, Zato je ključna fuzija kernelov in cevovodov
- **Kvantizacija** do FP4 zmanjšuje KV-cache, ampak zahteva kvantizacijsko-odvisno uenje, sicer pade natančnost
- **Mešana natančnost** v KV-cache: RoPE-občutljive dimenzije v BF16, ostalo v FP4
- **Logit stabilnost** preko RSM normiranja pred pozornostjo, ker so zdrueni vektorji nestabilni

## Koncepti

- [[Transformer arhitektura]] — osnova za V4
- [[MoE]] — Mixed Expert, izbrani experti
- [[Kvantizacija]] — FP4/F8 zmanjšanje velikosti
- [[Attencija]] — Pozornost, CSA, HCA


---
created: 9/2026
categories: []
rating: 4
tags:
  - 0🌲
related-to:
  - "[[Tema - Homelab Računalniki]]"
---

# Moji računalniki — Homelab setup

Pregled vseh naprav in ideje za homelab postavitev. Objavljeno na r/homelab z vprašanjem za nasvete, kaj z njimi.

## Dell XPS 13 9300

**Spec:**
- Intel Core i7-1065G7 (10 Ice Lake, 4C/8T)
- 16 GB RAM
- Intel Iris Plus Graphics G7
- 512 GB NVMe SSD
- Windows 11 Pro

**Ideje:** Majhna poraba, dober za lahki **Proxmox node** ali **Pi-hole/Home Assistant** strežnik. Lahko služi kot jump box za dostop do ostalih naprav.

## Microsoft Surface Pro 7

- Intel Core i7-1065G7 (1.30–3.90 GHz)
- 16 GB RAM
- Intel Iris Plus Graphics
- 512 GB SSD
- 12.3" PixelSense (2736×1824), multitouch
- Fedora Linux

**Status:** Glavni PC, veliko na potovanjih. Ostaja kot osebna naprava, ampak se lahko uporablja za **remote SSH access** v homelab.

## Desktop PC (DESKTOP-OSCTFVI)

**Najmočnejši računalnik:**

- Intel Core i7-9700F (9th Gen Coffee Lake, 8C/8T, **brez HT**)
- 32 GB DDR4-2666 MHz Dual-Channel
- Diskretna grafična karta (model ni naveden)
- 500GB–1TB NVMe SSD + HDD
- Windows 11 Pro

**Status:** V skupni rabi, edini središčni računalnik v pisarni.

**Ideje:** Idealen kandidat za **Proxmox host** ali **TrueNAS** (NAS + VM). 32 GB RAM omogoča več VM-i hkrati. SSD za sisteme, HDD za shranjevanje podatkov.

**Zadržek:** V skupni rabi z drugimi — potrebna komunikacija pred spremembami OS.

## HP 440 G3 AiO

**Najstarejši in najpočasnejši:**

- Intel Core i5-7500T (7th Gen Kaby Lake, 4C, low-power)
- 8 GB DDR4
- Intel HD Graphics 630
- 256 GB SanDisk SSD (SATA)
- 23.8" FHD (1920×1080)
- **Linux Mint 22.3 "Zena"** (Cinnamon)

**Status:** Redka uporaba, nadomesten s tabletom.

**Ideje:** 
- **Dedicated firewall** (OPNsense/pfSense) — predpogoj: dodatni NIC
- **Digital signage / info display** — zaslon za hišne metrike, vreme, koledar
- **Print server** za domači tiskalnik
- **ZFS backup target** — slab SSD, ampak OK za arhivsko shranjevanje

## Komentarji z Reddita

> ramonvanraaij: Vsi bi tekeli Proxmox — naredi čuden, ampak funkcionalen Proxmox cluster. Tretji računalnik naj bo NAS.

> kevinds: Folding@Home.

## Naslednji koraki

1. Preveri ali HP AiO dopušča passthrough v BIOS (za firewall)
2. Razmisli o dodatnem NIC-ju za firewall/router
3. Desktop PC pretvorit v Proxmox + TrueNAS — najprej ogovoriti s sodelavci
4. Dell XPS → Home Assistant ali monitoring stack (Grafana/Prometheus)

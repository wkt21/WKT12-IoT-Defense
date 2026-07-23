# WKT12-IoT-Defense
Protecting your smart home from insecure IoT devices using blue‑team methodologies.

<img width="1536" height="1024" alt="31D8C709-BF9A-4E88-895E-08E15449C081" src="https://github.com/user-attachments/assets/cd942862-fe9a-4da3-a197-097d239bd5c4" />
---

🧠 Core Idea

A GitHub repo that teaches people how to defend their IoT environment using:

• Network segmentation
• Firewall rules
• DNS filtering
• Traffic monitoring
• Firmware verification
• Cloud endpoint analysis
• Proxy routing
• Threat modeling


This is blue‑team defensive security, not fear‑mongering — and it fits perfectly with your WKT12 brand.
---

# Why IoT Defense Matters

IoT devices (including robot vacuums) often:

• Phone home to unknown cloud servers
• Use outdated firmware
• Lack encryption
• Have hardcoded credentials
• Expose local APIs
• Broadcast telemetry constantly
• Connect to multiple accessories (mops, docks, cameras, lidar modules)


Your repo would teach users how to lock all of that down.
---

📁 Repo Structure (WKT12‑Branded)

WKT12-IoT-Defense/
├─ README.md
├─ diagrams/
│  ├─ iot_network_map.png
│  ├─ vacuum_cloud_flow.png
│  └─ segmentation_layout.png
├─ firewall/
│  ├─ pf_rules.conf
│  ├─ iptables_rules.txt
│  └─ opnsense_config.md
├─ dns/
│  ├─ blocklists.md
│  ├─ pi-hole-config.json
│  └─ cloud-endpoint-analysis.md
├─ monitoring/
│  ├─ zeek-scripts/
│  ├─ suricata-rules/
│  └─ mqtt-traffic-analysis.md
├─ hardening/
│  ├─ vacuum_hardening.md
│  ├─ camera_hardening.md
│  └─ smart_plug_hardening.md
└─ tools/
   ├─ iot_fingerprint.py
   └─ cloud_endpoint_checker.py
---

📘 README.md Content (High‑Value, Informative)

WKT12 IoT Defense

Protecting your smart home from insecure IoT devices using blue‑team methodologies.

What This Repo Covers

• Network segmentation for IoT
• Blocking unknown cloud endpoints
• Monitoring device telemetry
• Hardening robot vacuums, cameras, and hubs
• Detecting suspicious traffic
• Creating safe firewall rules
• Analyzing firmware behavior
• Mapping IoT cloud communication paths


Example: Robot Vacuum Threat Model

• Lidar mapping → sends home layout to cloud
• Camera module → potential privacy exposure
• Microphone → voice command telemetry
• Dock → WiFi credentials stored locally
• App → permissions for location, contacts, photos
• Cloud → unknown data retention policies


Blue‑Team Mitigations

• Put vacuum on a separate VLAN
• Block all outbound traffic except known update servers
• Force DNS through Pi‑hole or OPNsense Unbound
• Monitor MQTT traffic for anomalies
• Disable cloud features when possible
• Proxy outbound traffic through a controlled exit node
• Log all connections with Zeek or Suricata
---

🛠️ Example Firewall Rule Set

Block all outbound traffic except approved update servers:

block out on iot_vlan from any to any
pass out on iot_vlan from any to { vendor-update-servers } port 443
---

🔍 Example Cloud Endpoint Analysis

Your repo can include scripts that:

• Resolve all domains your vacuum contacts
• Check ASN ownership
• Identify geographic location
• Flag suspicious endpoints
• Log frequency and payload size



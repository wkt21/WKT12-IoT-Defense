# Robot Vacuum Hardening Guide

1. Place the vacuum on a dedicated IoT VLAN.  
2. Block all outbound traffic except update servers.  
3. Force DNS through Pi-hole or OPNsense.  
4. Disable cloud features when possible.  
5. Monitor MQTT and HTTPS telemetry.  
6. Review firmware update endpoints regularly.

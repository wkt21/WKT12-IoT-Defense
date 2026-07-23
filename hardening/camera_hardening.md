# IoT Camera Hardening Guide

IoT cameras introduce continuous video streams, motion detection telemetry, cloud storage, and mobile app integration. Hardening focuses on preventing unauthorized access and limiting cloud exposure.

## Network Isolation
Place cameras on an isolated VLAN with no access to internal systems.

## Disable P2P Services
Many cameras use peer-to-peer relay services. Disable P2P to prevent external relay connections.

## Local Storage Preference
Use local NVR storage instead of cloud storage. Block outbound video upload endpoints.

## Strong Authentication
Disable default credentials. Enforce long passwords and disable guest viewing modes.

## RTSP/ONVIF Control
Restrict RTSP and ONVIF ports. Allow only known NVR systems to connect.

## Firmware Integrity
Verify firmware signatures. Avoid third-party firmware unless vetted.

## Telemetry Reduction
Block analytics domains. Monitor outbound traffic for unexpected video frame uploads.

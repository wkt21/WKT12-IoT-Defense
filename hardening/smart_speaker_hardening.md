# Smart Speaker Hardening Guide

Smart speakers include microphones, voice recognition, cloud APIs, and home automation integration. Hardening focuses on privacy and limiting cloud dependency.

## Microphone Control
Disable always-on listening modes when possible. Use hardware mute switches.

## Network Isolation
Place speakers on an IoT VLAN. Prevent access to internal systems.

## Cloud Feature Reduction
Disable voice history storage. Block analytics domains.

## Local Control Preference
Use local-only voice processing when supported. Avoid cloud-based routines.

## Firmware Updates
Verify update endpoints. Monitor for unusual update frequency.

## Telemetry Monitoring
Inspect outbound traffic for voice metadata or command logs.

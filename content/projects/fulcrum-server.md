---
title: Fulcrum — Headless Debian Server
date: 2026-01-11
category: Software
summary: A home server running Docker, Immich, Tailscale and a Samba NAS, plus a BME280 feeding fishing conditions over MQTT.
tags: [self-hosted, docker, mqtt]
spec:
  OS: Debian, headless
  Stack: Docker, Immich, Tailscale, Samba
  Sensors: BME280 → Mosquitto MQTT
  Access: Tailscale mesh
---

Fulcrum is the quiet machine everything else leans on: photo backup, file
storage, and a growing set of sensors. A BME280 publishes pressure and
temperature over MQTT, which is slowly becoming a fishing-conditions monitor
for Sandvlei.

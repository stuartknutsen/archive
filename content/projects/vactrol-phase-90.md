---
title: Vactrol Phase 90 Clone
date: 2026-04-02
category: Analog
summary: A four-stage phaser built around LDR/LED vactrols, with an ATtiny85 running a bare-metal PWM LFO.
tags: [analog, guitar-pedal, attiny85]
spec:
  Topology: Four all-pass stages, vactrol-swept
  LFO: ATtiny85, PWM-driven LED
  Optocouplers: Homemade LED/LDR pairs
  Enclosure: 1590B, hand-drilled
---

The sweep comes from homemade optocouplers — an LED and an LDR heat-shrunk
together in the dark — driven by a triangle LFO the ATtiny synthesises in
software. Matching the vactrols by eye and by ear was most of the work.

An LM358 oscillated under capacitive load until the compensation was sorted;
a good reminder that the cheapest op-amp in the drawer has opinions.

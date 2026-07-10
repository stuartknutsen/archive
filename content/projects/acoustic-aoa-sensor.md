---
title: Acoustic Angle-of-Arrival Sensor
date: 2026-05-18
category: Electronics
summary: >
  Two microphones a known distance apart hear the same sound a fraction of a
  millisecond apart. That delay encodes the bearing of the source. A custom
  STM32F405 board measures it with simultaneous dual-ADC sampling and recovers
  direction by cross-correlation.
tags: [embedded, pcb, dsp, stm32]
spec:
  MCU: STM32F405RGT6 · Cortex-M4F · 168 MHz
  Acquisition: Dual ADC, simultaneous mode, single trigger
  Microphones: 2 × MEMS analog, fixed baseline
  Method: Cross-correlation → TDOA → bearing
  Interface: I²C slave (custom firmware)
  Fab: JLCPCB · 4-layer
  Status: Working
---

Measuring the delay precisely enough is the whole project. It means sampling both
microphones at the *same instant* — not nearly the same instant — which on the
STM32F4 means driving two ADCs in simultaneous dual mode off a single trigger,
then running a cross-correlation in firmware fast enough to be useful.

Bring-up was where the datasheet stopped being a suggestion: a floating VDD pin
the schematic implied was internal, and an I²C bus jammed by a known F4 silicon
erratum around the ACK bit. The kind of bugs that do not exist until the hardware
is real, and are then the only thing that exists.

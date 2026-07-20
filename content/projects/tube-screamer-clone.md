---
title: Tube Screamer Clone
date: 2026-06-20
category: Electronics
summary: My take on the classic Ibanez Tube Screamer, but altered to be a bit simpler and tuned to my guitar and amp combo, and taste.
tags: [electric guitar]
spec:
  Topology: Single DIP8 TL072 utilising one stage for gain and diode clipping and another for an output buffer, with a passive tone stack and volume control between them
  Features: Input high pass filter, gain control, diode clipping, output tone control, and volume control
  Enclosure: Hammond 1590B aluminium
---

After seeing Electrosmash's circuit analysis on the Ibanez Tube Screamer, I decided to have a go at building one. I decided to forgo the complicated JFET bypass circuit for two reasons. It looks unesscarily complex and the JFETs required are hard to source in South Africa without paying extreme shipping fees for inexpensive components. An off the shelf stomp switch is a much more elegant solution. I first breadboarded the circuit replacing the BJT input and output buffers with op-amp ones. I really liked the clipping from the diodes, you get that classic rock sound. But I wasn't too happy on how much the output tone cut the highs. So I decided to simplify the circuit.

Firstly I removed the input buffer and instead put a 470K &Omega; between the non inverting input and V~bias~. This way the input impedance is matched to the original tube screamer without needing the extra BJT input buffer. Then I decided to remove the active tone control and just have a passive RC tone controller just like what is already on the guitar. This simply tames the high frequencies and gets rid of the harshness produced by the diode clipping. 

For the components, all the resistors are metal film 1%, all the critical capacitors are polyester film. I chose the TL072 because it works nicely with a single 9V supply and has the required performance for audio requirements. It's jellybean part that's available at most electronics retailers. The diodes are just standard 1N4148s, they are very cheap and available everywhere.

Once I had a finalised circuit, I went to the lab at my university and hooked it up to an oscilloscope. I just wanted to make sure the gain and clipping were working as expected and that I was getting the desired frequency response. Everything looked nice on the scope so I continued with building the circuit. I wanted to try my hand at "dead bug prototyping". Dead bug is where you solder everything together without a pcb. It is a real old style way of doing it. It ended up looking a bit like a rat's nest on the inside but that's okay. Sometimes it's function over form. I have to say, I do like the dead bug look even though it can be a bit tedious if there are multiple connections or if you have made an error in your layout. It is definitely something I will continue to do on non-critical stuff going forward. 

I bought a Hammond 1590B aluminium enclosure from Communica. The 1590B is the standard go to for DIY guitar pedals. I made a simple drilling template in Onshape and drilled out all of the nesscary holes on my drill press. Drilling through the alumium was easy and the holes finished up nicely with a deburring tool. I am not a huge fan of the black paint as it is a little boring but Communica didn't have the bare aluminium one in stock. I plan to give it a custom paint job in the future, not too sure what, but for now it does the job.

I sourced all the components from Communica and Mantech.

Overall this project was a really nice way to get into guitar pedal making. It's quite simple and does more on the inside than say a fuzz pedal or just a tone stack. I certainly learned a lot from it
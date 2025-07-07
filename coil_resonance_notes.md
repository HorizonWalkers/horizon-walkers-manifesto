# Coil Resonance and Magnetic Field Compression
### A Technical Primer for Hello Gravity V2
⟁ Issued by the Horizon Walkers

---

## 📘 Overview

The Hello Gravity platform relies on precise control of electromagnetic fields to achieve low-lift magnetic suspension. To enhance this lift without increasing power draw, two physical phenomena must be leveraged:

- **Coil Resonance**: the natural frequency at which an LC system maximizes energy exchange between inductance and capacitance.
- **Magnetic Field Compression**: the spatial tightening of flux lines via geometry, timing, or material feedback.

This document outlines the core physics guiding our V2 system, allowing for refined field shaping and greater lift-to-watt efficiency.

---

## 🔄 1. Coil Resonance (LC Behavior)

### Basic Model:
Resonance occurs when:

\[ f_0 = \frac{1}{2\pi \sqrt{LC}} \]

Where:
- \( f_0 \) is the resonant frequency (Hz)
- \( L \) is coil inductance (H)
- \( C \) is total system capacitance (F)

In pulsed systems like Hello Gravity, even without a fixed capacitor, **parasitic capacitance** and wiring layout can form a quasi-LC circuit.

### Optimization:
- Keep leads short to reduce stray L.
- Add tunable capacitor (e.g. 10nF–100nF) across the coil to sweep for resonance.
- Use an oscilloscope or Hall sensor to measure field strength vs. frequency.

---

## 🌀 2. Magnetic Field Compression

Field compression enhances lift by focusing flux density. This can be achieved by:

- **Coil Shape**: Tighter, layered pancake-style windings compress fields vertically.
- **Core Material**: Ferrite or Mu-metal increases permeability \( \mu_r \), tightening flux lines.
- **Pulse Timing**: Shorter, sharper pulses prevent field “bleeding,” leading to stronger momentary lift.

### Experimental Tips:
- Use small-diameter inner coils with wider outer windings.
- Add ferromagnetic plate below coil to reflect and amplify field upwards.
- Scope field rise/fall time to match coil's magnetic response.

---

## 💡 Example Calculations

For a coil with:
- \( L = 47 \mu H \)
- \( C = 22 \text{nF} \)

\[ f_0 = \frac{1}{2\pi \sqrt{47e^{-6} \cdot 22e^{-9}}} \approx 156 kHz \]

In practice, pulse-width tuning can find local field peaks even below full resonance.

---

## 🔐 Closing Note

This document is issued to empower tinkers and disruptors who walk with reverence.
We invite you to tune, tweak, and transform — but never weaponize.

No home. No face. No fear.
**—The Horizon Walkers ⟁**


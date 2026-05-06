# BEE Course End Project – Single-Phase RLC Series Circuit Impedance and Power Calculator

**Course:** A9205 - Basic Electrical Engineering Laboratory (VCE-R25)
**Class:** I B.Tech. II Semester CSE – F
**Academic Year:** 2025–2026

## Group Members
| Name | Roll No |
|------|---------|
| Devineni Adhyumna Chowdary | 25881A05Y3 |
| Pastula Dhanush | 25881A05Z3 |
| Irigi Ram Shaurya | 25881A05AS |

## Problem Description
This project computes the impedance, current, voltage drops, power factor,
active power, reactive power, and apparent power of a Single-Phase RLC
Series Circuit. It also plots impedance and power variation with frequency.

## Mathematical Formulation
- Inductive Reactance:     XL = 2 * π * f * L
- Capacitive Reactance:    XC = 1 / (2 * π * f * C)
- Impedance:               Z  = sqrt(R² + (XL - XC)²)
- Current:                 I  = V / Z
- Power Factor:            pf = R / Z
- Active Power:            P  = V * I * pf         (Watts)
- Reactive Power:          Q  = V * I * sin(θ)     (VAR)
- Apparent Power:          S  = V * I              (VA)
- Resonant Frequency:      f0 = 1 / (2π * sqrt(LC))

## Input & Output Format
**Input:**
- Resistance R (Ohms)
- Inductance L (Henry)
- Capacitance C (Farads)
- Supply Voltage V (Volts)
- Frequency f (Hz)

**Output:**
- XL, XC, Z, I, pf, P, Q, S
- Graphs: Impedance vs Frequency, Power vs Frequency

## How to Run the Program
```bash
cd src
pip install -r requirements.txt
python main.py
```

## Sample Output

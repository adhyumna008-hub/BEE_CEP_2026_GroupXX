# ============================================================
# Project  : Single-Phase RLC Series Circuit Analyzer
# Course   : A9205 - Basic Electrical Engineering Lab
# Class    : I B.Tech II Sem CSE-F, VCE (2025-2026)
# Group    : Devineni Adhyumna Chowdary (25881A05Y3)
#            Pastula Dhanush            (25881A05Z3)
#            Irigi Ram Shaurya          (25881A05AS)
# ============================================================

import math
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# FUNCTION: Get validated positive float input
# ─────────────────────────────────────────────
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  [Error] Value must be greater than zero. Try again.")
            else:
                return value
        except ValueError:
            print("  [Error] Invalid input. Please enter a numeric value.")

# ─────────────────────────────────────────────
# FUNCTION: Compute RLC circuit parameters
# ─────────────────────────────────────────────
def compute_rlc(R, L, C, V, f):
    XL = 2 * math.pi * f * L                          # Inductive Reactance (Ω)
    XC = 1 / (2 * math.pi * f * C)                    # Capacitive Reactance (Ω)
    Z  = math.sqrt(R**2 + (XL - XC)**2)               # Impedance (Ω)
    I  = V / Z                                         # Current (A)
    theta = math.atan2((XL - XC), R)                  # Phase angle (radians)
    pf = math.cos(theta)                               # Power Factor
    P  = V * I * pf                                    # Active Power (W)
    Q  = V * I * math.sin(theta)                       # Reactive Power (VAR)
    S  = V * I                                         # Apparent Power (VA)
    f0 = 1 / (2 * math.pi * math.sqrt(L * C))         # Resonant Frequency (Hz)
    return XL, XC, Z, I, theta, pf, P, Q, S, f0

# ─────────────────────────────────────────────
# FUNCTION: Display results
# ─────────────────────────────────────────────
def display_results(R, L, C, V, f, XL, XC, Z, I, theta, pf, P, Q, S, f0):
    nature = "lagging" if (XL > XC) else ("leading" if XC > XL else "unity")
    print("\n" + "="*45)
    print("     RLC Series Circuit Analysis Results")
    print("="*45)
    print(f"  Resistance          R  = {R} Ω")
    print(f"  Inductance          L  = {L} H")
    print(f"  Capacitance         C  = {C} F")
    print(f"  Supply Voltage      V  = {V} V")
    print(f"  Frequency           f  = {f} Hz")
    print("-"*45)
    print(f"  Inductive Reactance XL = {XL:.4f} Ω")
    print(f"  Capacitive Reactance XC = {XC:.4f} Ω")
    print(f"  Impedance           Z  = {Z:.4f} Ω")
    print(f"  Current             I  = {I:.4f} A")
    print(f"  Phase Angle         θ  = {math.degrees(theta):.4f}°")
    print(f"  Power Factor        pf = {pf:.4f} ({nature})")
    print(f"  Active Power        P  = {P:.4f} W")
    print(f"  Reactive Power      Q  = {Q:.4f} VAR")
    print(f"  Apparent Power      S  = {S:.4f} VA")
    print(f"  Resonant Frequency  f0 = {f0:.4f} Hz")
    print("="*45)

# ─────────────────────────────────────────────
# FUNCTION: Plot graphs
# ─────────────────────────────────────────────
def plot_graphs(R, L, C, V):
    # Frequency range: 1 Hz to 1000 Hz
    freqs = [i for i in range(1, 1001)]

    Z_vals, P_vals, Q_vals, S_vals, I_vals = [], [], [], [], []

    for f in freqs:
        XL = 2 * math.pi * f * L
        XC = 1 / (2 * math.pi * f * C)
        Z  = math.sqrt(R**2 + (XL - XC)**2)
        I  = V / Z
        theta = math.atan2((XL - XC), R)
        Z_vals.append(Z)
        I_vals.append(I)
        P_vals.append(V * I * math.cos(theta))
        Q_vals.append(V * I * math.sin(theta))
        S_vals.append(V * I)

    # ── Graph 1: Impedance vs Frequency ──
    plt.figure(figsize=(8, 5))
    plt.plot(freqs, Z_vals, color='blue', linewidth=2)
    plt.title('Impedance vs Frequency – RLC Series Circuit')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Impedance Z (Ω)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../screenshots/impedance_vs_frequency.png')
    plt.show()

    # ── Graph 2: Current vs Frequency ──
    plt.figure(figsize=(8, 5))
    plt.plot(freqs, I_vals, color='green', linewidth=2)
    plt.title('Current vs Frequency – RLC Series Circuit')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Current I (A)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../screenshots/current_vs_frequency.png')
    plt.show()

    # ── Graph 3: Power vs Frequency ──
    plt.figure(figsize=(8, 5))
    plt.plot(freqs, P_vals, label='Active Power P (W)',    color='red',    linewidth=2)
    plt.plot(freqs, Q_vals, label='Reactive Power Q (VAR)',color='orange', linewidth=2)
    plt.plot(freqs, S_vals, label='Apparent Power S (VA)', color='purple', linewidth=2)
    plt.title('Power vs Frequency – RLC Series Circuit')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (W / VAR / VA)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../screenshots/power_vs_frequency.png')
    plt.show()

    print("\n  [✔] Graphs saved to /screenshots folder.")

# ─────────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────────
def main():
    print("\n" + "="*45)
    print("  Single-Phase RLC Series Circuit Analyzer")
    print("  BEE Lab CEP | VCE 2025-2026")
    print("="*45)
    print("\nEnter Circuit Parameters:\n")

    R = get_positive_float("  Resistance     R (Ω)  : ")
    L = get_positive_float("  Inductance     L (H)  : ")
    C = get_positive_float("  Capacitance    C (F)  : ")
    V = get_positive_float("  Supply Voltage V (V)  : ")
    f = get_positive_float("  Frequency      f (Hz) : ")

    XL, XC, Z, I, theta, pf, P, Q, S, f0 = compute_rlc(R, L, C, V, f)
    display_results(R, L, C, V, f, XL, XC, Z, I, theta, pf, P, Q, S, f0)

    print("\n  Generating graphs...")
    plot_graphs(R, L, C, V)

if __name__ == "__main__":
    main()

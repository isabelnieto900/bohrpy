"""Ejemplo de uso de bohrpy con el hidrógeno y el He+.

Desde la raíz del repositorio:

    python examples/ejemplo_uso.py

Las figuras quedan en examples/figuras/.
"""

from pathlib import Path

from bohrpy import BohrAtom


def _imprimir_niveles(atomo, niveles):
    print(f"Z = {atomo.Z}")
    for n in range(1, niveles + 1):
        energia = atomo.energy_level(n)
        radio_angstrom = atomo.orbit_radius(n) * 1e10
        print(f"  n = {n}:  E = {energia:8.3f} eV    r = {radio_angstrom:7.4f} Å")


def _imprimir_transicion(atomo, n_inicial, n_final):
    resultado = atomo.transition(n_inicial, n_final)
    print(
        f"Transición n = {n_inicial} -> n = {n_final} ({resultado['type']})"
    )
    print(f"  ΔE = {resultado['delta_E_eV']:.4f} eV")
    print(f"  f  = {resultado['frequency_Hz']:.6e} Hz")
    print(f"  λ  = {resultado['wavelength_m'] * 1e9:.2f} nm")


def main():
    salida = Path(__file__).resolve().parent / "figuras"
    salida.mkdir(exist_ok=True)

    hidrogeno = BohrAtom(Z=1)
    print("Hidrógeno")
    _imprimir_niveles(hidrogeno, 5)
    print()
    _imprimir_transicion(hidrogeno, 3, 2)
    print()
    _imprimir_transicion(hidrogeno, 1, 2)

    hidrogeno.plot_energy_levels(
        max_n=5,
        show=False,
        save_path=salida / "niveles_hidrogeno.png",
    )
    hidrogeno.plot_orbits(
        max_n=4,
        show=False,
        save_path=salida / "orbitas_hidrogeno.png",
    )

    helio = BohrAtom(Z=2)
    print()
    print("He+")
    _imprimir_niveles(helio, 3)
    helio.plot_energy_levels(
        max_n=4,
        show=False,
        save_path=salida / "niveles_he_plus.png",
    )

    print()
    print(f"Figuras guardadas en {salida}")


if __name__ == "__main__":
    main()

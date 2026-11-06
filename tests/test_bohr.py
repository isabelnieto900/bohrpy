"""Pruebas del modelo de Bohr: energías, radios, transiciones y gráficas."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest

from bohrpy import A_0, BohrAtom
from bohrpy.constants import C_LIGHT, E_CHARGE, H_PLANCK


def test_energia_del_estado_fundamental_del_hidrogeno():
    atomo = BohrAtom(Z=1)
    assert atomo.energy_level(1) == pytest.approx(-13.605693)


def test_la_energia_crece_con_el_cuadrado_de_z():
    hidrogeno = BohrAtom(Z=1)
    helio = BohrAtom(Z=2)
    assert helio.energy_level(1) == pytest.approx(4 * hidrogeno.energy_level(1))


def test_la_energia_cae_con_el_cuadrado_de_n():
    atomo = BohrAtom()
    assert atomo.energy_level(2) == pytest.approx(atomo.energy_level(1) / 4)
    assert atomo.energy_level(3) == pytest.approx(atomo.energy_level(1) / 9)


def test_rechaza_nivel_y_numero_atomico_invalidos():
    with pytest.raises(ValueError):
        BohrAtom().energy_level(0)
    with pytest.raises(ValueError):
        BohrAtom(Z=0)
    with pytest.raises(ValueError):
        BohrAtom(Z=1.5)


def test_radio_de_bohr_y_su_dependencia_con_n_y_z():
    hidrogeno = BohrAtom(Z=1)
    assert hidrogeno.orbit_radius(1) == pytest.approx(A_0)
    assert hidrogeno.orbit_radius(2) == pytest.approx(4 * A_0)

    helio = BohrAtom(Z=2)
    assert helio.orbit_radius(1) == pytest.approx(A_0 / 2)


def test_transicion_lyman_alfa_es_emision():
    atomo = BohrAtom()
    resultado = atomo.transition(2, 1)

    delta_e = abs(atomo.energy_level(2) - atomo.energy_level(1))
    frecuencia = delta_e * E_CHARGE / H_PLANCK

    assert resultado["type"] == "emisión"
    assert resultado["delta_E_eV"] == pytest.approx(delta_e)
    assert resultado["frequency_Hz"] == pytest.approx(frecuencia)
    assert resultado["wavelength_m"] == pytest.approx(C_LIGHT / frecuencia)
    # La línea Lyman-alfa del hidrógeno está cerca de 121.6 nm.
    assert resultado["wavelength_m"] * 1e9 == pytest.approx(121.6, abs=1.0)


def test_transicion_de_absorcion_y_niveles_iguales():
    resultado = BohrAtom().transition(1, 3)
    assert resultado["type"] == "absorción"
    assert resultado["delta_E_eV"] > 0

    with pytest.raises(ValueError):
        BohrAtom().transition(2, 2)


def test_grafica_de_niveles_marca_energias_y_longitudes_de_onda():
    fig, ax = BohrAtom().plot_energy_levels(max_n=4, show=False)
    textos = [texto.get_text() for texto in ax.texts]

    assert any(texto.startswith("n = 1") for texto in textos)
    assert any("nm" in texto for texto in textos)
    assert ax.get_ylabel() == "Energía (eV)"
    plt.close(fig)


def test_grafica_de_orbitas_conserva_la_escala():
    fig, ax = BohrAtom(Z=1).plot_orbits(max_n=3, show=False)

    assert ax.get_aspect() in ("equal", 1.0)
    assert len(ax.lines) == 3
    plt.close(fig)


def test_las_graficas_rechazan_un_nivel_maximo_invalido():
    with pytest.raises(ValueError):
        BohrAtom().plot_energy_levels(max_n=0, show=False)
    with pytest.raises(ValueError):
        BohrAtom().plot_orbits(max_n=False, show=False)


def test_se_puede_guardar_la_figura(tmp_path):
    destino = tmp_path / "niveles.png"
    fig, _ = BohrAtom().plot_energy_levels(max_n=3, show=False, save_path=destino)

    assert destino.is_file()
    assert destino.stat().st_size > 0
    plt.close(fig)

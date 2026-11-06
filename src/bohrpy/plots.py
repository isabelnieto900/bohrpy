"""Gráficas del modelo de Bohr: niveles de energía y órbitas."""

import matplotlib.pyplot as plt
import numpy as np

# Nombre y color de cada serie, según el nivel inferior de la transición.
SERIES = {
    1: ("Lyman", "#1f77b4"),
    2: ("Balmer", "#d62728"),
    3: ("Paschen", "#2ca02c"),
    4: ("Brackett", "#9467bd"),
    5: ("Pfund", "#8c564b"),
}
"""Nombre y color de cada serie, según el nivel inferior de la transición."""


def _validar_max_n(max_n):
    """Comprueba que el nivel máximo sea un entero mayor o igual que 1."""
    if not isinstance(max_n, int) or isinstance(max_n, bool) or max_n < 1:
        raise ValueError("max_n debe ser un entero mayor o igual que 1.")
    return max_n


def _estilo_serie(n_final):
    """Devuelve el nombre y el color de la serie que termina en n_final."""
    if n_final in SERIES:
        return SERIES[n_final]
    return (f"hacia n={n_final}", "#7f7f7f")


def _guardar_o_mostrar(fig, show, save_path):
    """Guarda la figura si hay ruta y la muestra si show es verdadero."""
    if save_path is not None:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    if show:
        plt.show()


def plot_energy_levels(atom, max_n=5, show=True, save_path=None):
    """Dibuja los niveles de energía y las transiciones de emisión.

    Cada línea horizontal es un nivel n. Las flechas bajan del nivel
    inicial al final y se agrupan por serie (Lyman, Balmer, Paschen...).
    Junto a cada flecha va la longitud de onda del fotón, en nanómetros.

    Parameters
    ----------
    atom : BohrAtom
        Átomo hidrogenoide cuyos niveles se van a dibujar.
    max_n : int
        Nivel más alto que entra en la figura.
    show : bool
        Si es verdadero, abre la ventana de la gráfica.
    save_path : str o Path, opcional
        Ruta donde se guarda la imagen. Si es None, no se guarda.

    Returns
    -------
    tuple
        La figura y los ejes de Matplotlib.
    """
    _validar_max_n(max_n)

    fig, ax = plt.subplots(figsize=(8, 8))
    energia_minima = atom.energy_level(1)

    for n in range(1, max_n + 1):
        energia = atom.energy_level(n)
        ax.hlines(energia, 0, 1, colors="#1f4e79", linewidth=2)
        ax.text(
            1.04,
            energia,
            f"n = {n}    {energia:.2f} eV",
            va="center",
            fontsize=9,
        )

    # Cada transición ocupa su propia x. Las más largas van a la izquierda,
    # donde hay más espacio vertical para la etiqueta.
    transiciones = [
        (n_inicial, n_final)
        for n_final in range(1, max_n)
        for n_inicial in range(n_final + 1, max_n + 1)
    ]
    transiciones.sort(
        key=lambda niveles: atom.energy_level(niveles[0]) - atom.energy_level(niveles[1])
    )
    caja = {"boxstyle": "round,pad=0.12", "fc": "white", "ec": "none", "alpha": 0.9}

    for indice, (n_inicial, n_final) in enumerate(transiciones):
        _, color = _estilo_serie(n_final)
        x = 0.06 + 0.88 * (indice + 0.5) / len(transiciones)
        energia_inicial = atom.energy_level(n_inicial)
        energia_final = atom.energy_level(n_final)
        ax.annotate(
            "",
            xy=(x, energia_final),
            xytext=(x, energia_inicial),
            arrowprops={"arrowstyle": "-|>", "color": color, "lw": 1.4},
        )
        transicion = atom.transition(n_inicial, n_final)
        longitud_nm = transicion["wavelength_m"] * 1e9
        salto = abs(energia_inicial - energia_final)
        if salto < 0.08 * abs(energia_minima):
            y_texto = energia_inicial + 0.045 * abs(energia_minima)
            va = "bottom"
        else:
            y_texto = (energia_inicial + energia_final) / 2
            va = "center"
        ax.text(
            x,
            y_texto,
            f"{longitud_nm:.0f} nm",
            color=color,
            fontsize=7,
            ha="center",
            va=va,
            bbox=caja,
        )

    for n_final in range(1, max_n):
        nombre, color = _estilo_serie(n_final)
        ax.plot([], [], color=color, label=nombre)

    ax.set_xlim(-0.05, 1.62)
    ax.set_ylim(energia_minima * 1.12, abs(energia_minima) * 0.08)
    ax.set_xticks([])
    ax.set_ylabel("Energía (eV)")
    ax.set_title(f"Niveles de energía y transiciones (Z = {atom.Z})")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.legend(title="Serie", loc="lower right", frameon=True)
    fig.tight_layout()
    _guardar_o_mostrar(fig, show, save_path)
    return fig, ax


def plot_orbits(atom, max_n=4, show=True, save_path=None):
    """Dibuja las órbitas circulares del modelo de Bohr en el plano.

    El núcleo queda en el origen. El radio se muestra en ångströms
    para que la escala sea legible, y un punto marca al electrón
    sobre el eje x de cada órbita.

    Parameters
    ----------
    atom : BohrAtom
        Átomo hidrogenoide cuyas órbitas se van a dibujar.
    max_n : int
        Nivel más alto que entra en la figura.
    show : bool
        Si es verdadero, abre la ventana de la gráfica.
    save_path : str o Path, opcional
        Ruta donde se guarda la imagen. Si es None, no se guarda.

    Returns
    -------
    tuple
        La figura y los ejes de Matplotlib.
    """
    _validar_max_n(max_n)

    fig, ax = plt.subplots(figsize=(7.2, 7))
    angulo = np.linspace(0, 2 * np.pi, 400)
    colores = plt.cm.viridis(np.linspace(0.15, 0.9, max_n))

    ax.scatter(
        [0],
        [0],
        s=130,
        c="#c0392b",
        zorder=5,
        label=f"Núcleo (Z = {atom.Z})",
    )

    for n, color in zip(range(1, max_n + 1), colores):
        radio_angstrom = atom.orbit_radius(n) * 1e10
        ax.plot(
            radio_angstrom * np.cos(angulo),
            radio_angstrom * np.sin(angulo),
            color=color,
            linewidth=1.8,
            label=f"n = {n}    r = {radio_angstrom:.3f} Å",
        )
        ax.scatter([radio_angstrom], [0], s=30, color=color, zorder=4)

    ax.set_aspect("equal")
    ax.set_xlabel("x (Å)")
    ax.set_ylabel("y (Å)")
    ax.set_title(f"Órbitas del modelo de Bohr (Z = {atom.Z})")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)
    fig.tight_layout()
    _guardar_o_mostrar(fig, show, save_path)
    return fig, ax

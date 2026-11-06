# hola 
import matplotlib.pyplot as plt
import numpy as np
from .constants import H_PLANCK, C_LIGHT, E_CHARGE, A_0

class BohrAtom:
    """
    Clase que representa un átomo hidrogenoide según el modelo de Bohr.
    Encapsula los parámetros físicos y métodos para cálculos y gráficos.
    """
    
    def __init__(self, Z=1):
        """
        Inicializa el átomo con un número atómico Z.
        Por defecto, Z=1 (Hidrógeno).
        """
        if not isinstance(Z, int) or Z < 1:
            raise ValueError("El número atómico Z debe ser un entero positivo.")
        self.Z = Z
        # Energía del estado fundamental del Hidrógeno en eV (aprox -13.6 eV)
        self.E1_H = -13.605693

    def energy_level(self, n):
        """
        Calcula la energía del electrón en el nivel n en electrón-voltios (eV).
        """
        if n < 1:
            raise ValueError("El número cuántico principal n debe ser >= 1.")
        return self.E1_H * (self.Z**2) / (n**2)

    def orbit_radius(self, n):
        """
        Calcula el radio de la órbita para el nivel n en metros (m).
        """
        if n < 1:
            raise ValueError("El número cuántico principal n debe ser >= 1.")
        return A_0 * (n**2) / self.Z

    def transition(self, n_initial, n_final):
        """
        Calcula la transición electrónica entre dos niveles.
        Retorna la diferencia de energía (eV), la frecuencia (Hz) y la longitud de onda (m) del fotón emitido o absorbido.
        """
        if n_initial == n_final:
            raise ValueError("Los niveles inicial y final deben ser diferentes.")

        e_i = self.energy_level(n_initial)
        e_f = self.energy_level(n_final)
        
        # Diferencia de energía en eV y conversión a Julios
        delta_E_eV = abs(e_f - e_i)
        delta_E_J = delta_E_eV * E_CHARGE
        
        # Frecuencia: f = E / h
        frequency = delta_E_J / H_PLANCK
        
        # Longitud de onda: lambda = c / f
        wavelength = C_LIGHT / frequency
        
        return {
            "delta_E_eV": delta_E_eV,
            "frequency_Hz": frequency,
            "wavelength_m": wavelength,
            "type": "emisión" if n_initial > n_final else "absorción"
        }

    def plot_energy_levels(self, max_n=5):
        """
        Representa gráficamente los niveles de energía y posibles transiciones hasta el nivel max_n.
        """
        plt.figure(figsize=(6, 8))
        for n in range(1, max_n + 1):
            E = self.energy_level(n)
            plt.axhline(y=E, color='b', linestyle='-', alpha=0.6)
            plt.text(0.5, E + 0.1, f'n={n} (E={E:.2f} eV)', ha='center', va='bottom', color='black', fontsize=10)
        
        plt.title(f'Niveles de energía para átomo hidrogenoide (Z={self.Z})')
        plt.ylabel('Energía (eV)')
        plt.xticks([])  # Ocultar eje X ya que no representa nada físico aquí
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()

    def plot_orbits(self, max_n=4):
        """
        Dibuja de manera simplificada las órbitas electrónicas circulares en el plano 2D.
        """
        fig, ax = plt.subplots(figsize=(7, 7))
        theta = np.linspace(0, 2*np.pi, 100)
        
        # Graficar el Núcleo
        ax.plot(0, 0, 'ro', markersize=12, label=f'Núcleo (Z={self.Z})')
        
        for n in range(1, max_n + 1):
            # Convertir radio a Angstroms (1e10) para que la gráfica sea más legible
            r_angstrom = self.orbit_radius(n) * 1e10  
            x = r_angstrom * np.cos(theta)
            y = r_angstrom * np.sin(theta)
            ax.plot(x, y, label=f'n={n} (r={r_angstrom:.2f} Å)')
        
        ax.set_aspect('equal')
        plt.title(f'Órbitas del modelo de Bohr (Z={self.Z})')
        plt.xlabel('Distancia X (Å)')
        plt.ylabel('Distancia Y (Å)')
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()
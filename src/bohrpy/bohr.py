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

    def plot_energy_levels(self, max_n=5, show=True, save_path=None):
        """
        Representa los niveles de energía y las transiciones hasta max_n.

        El dibujo vive en plots.py. Este método solo expone esa gráfica
        desde el átomo.
        """
        from .plots import plot_energy_levels

        return plot_energy_levels(self, max_n=max_n, show=show, save_path=save_path)

    def plot_orbits(self, max_n=4, show=True, save_path=None):
        """
        Dibuja las órbitas electrónicas en el plano hasta el nivel max_n.

        El dibujo vive en plots.py. Este método solo expone esa gráfica
        desde el átomo.
        """
        from .plots import plot_orbits

        return plot_orbits(self, max_n=max_n, show=show, save_path=save_path)
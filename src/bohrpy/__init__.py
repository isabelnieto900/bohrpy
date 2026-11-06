"""
bohrpy: Una librería en Python para el modelo del átomo de Bohr.
Desarrollada para calcular niveles de energía, radios, transiciones electrónicas 
y representaciones gráficas de átomos hidrogenoides.
"""

# Importamos la clase principal para facilitar su acceso
from .bohr import BohrAtom

# Importamos las constantes físicas
from .constants import H_PLANCK, C_LIGHT, E_CHARGE, M_ELECTRON, A_0

# Definición de la versión de la librería (ideal para publicar en PyPI)
__version__ = "0.1.0"

# Limitamos qué se importa cuando alguien usa 'from bohrpy import *'
__all__ = ["BohrAtom", "H_PLANCK", "C_LIGHT", "E_CHARGE", "M_ELECTRON", "A_0"]
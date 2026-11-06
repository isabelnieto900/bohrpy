# bohrpy

Librería en Python del modelo atómico de Bohr para el hidrógeno y átomos hidrogenoides. Calcula niveles de energía, radios de órbita y transiciones electrónicas, y dibuja esos resultados.

## Instalación

Desde la raíz del repositorio:

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[test]"
```

El paquete pide estas versiones, que son las usadas en el proyecto:

- `numpy==1.26.4`
- `matplotlib==3.6.3`
- `pytest==9.2.0` para las pruebas

## Uso básico

```python
from bohrpy import BohrAtom

hidrogeno = BohrAtom(Z=1)

print(hidrogeno.energy_level(1))    # energía del nivel n, en eV
print(hidrogeno.orbit_radius(1))    # radio de la órbita, en metros

transicion = hidrogeno.transition(3, 2)
print(transicion["delta_E_eV"])
print(transicion["frequency_Hz"])
print(transicion["wavelength_m"])
print(transicion["type"])           # "emisión" o "absorción"

hidrogeno.plot_energy_levels(max_n=5)
hidrogeno.plot_orbits(max_n=4)
```

`Z` es el número atómico. Con `Z=1` se obtiene el hidrógeno y con `Z=2` el He+.

Para guardar una figura sin abrir una ventana:

```python
hidrogeno.plot_energy_levels(max_n=5, show=False, save_path="niveles.png")
hidrogeno.plot_orbits(max_n=4, show=False, save_path="orbitas.png")
```

## Ejemplo

```bash
python examples/ejemplo_uso.py
```

Imprime los niveles del hidrógeno, la línea de Balmer n = 3 → n = 2 y una absorción n = 1 → n = 2. También guarda las figuras en `examples/figuras/`.

## Pruebas

```bash
pytest
```

## Autores

- Isabel Nieto
- Kevin Osorio

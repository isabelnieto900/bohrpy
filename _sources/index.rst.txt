bohrpy
======

Librería en Python del modelo atómico de Bohr para el hidrógeno y los átomos hidrogenoides. Calcula niveles de energía, radios de órbita y transiciones electrónicas, y dibuja esos resultados.

El punto de entrada es la clase :class:`bohrpy.BohrAtom`. El argumento ``Z`` es el número atómico: ``1`` corresponde al hidrógeno y ``2`` al He+.

.. code-block:: python

   from bohrpy import BohrAtom

   hidrogeno = BohrAtom(Z=1)
   print(hidrogeno.energy_level(2))
   print(hidrogeno.orbit_radius(2))
   print(hidrogeno.transition(3, 2))

.. toctree::
   :maxdepth: 2
   :caption: Contenido

   instalacion
   uso
   api

Autores
-------

- Isabel Nieto
- Kevin Osorio

Índice
------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

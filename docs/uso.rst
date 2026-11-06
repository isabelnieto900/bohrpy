Uso
===

Energía de un nivel
-------------------

:meth:`bohrpy.BohrAtom.energy_level` devuelve la energía en electronvoltios:

.. math::

   E_n = -13.605693\,\frac{Z^2}{n^2}\ \mathrm{eV}

``n`` es un entero mayor o igual que 1. En el hidrógeno, el nivel 1 vale −13.605693 eV. Al aumentar ``n``, la energía se acerca a cero.

.. code-block:: python

   atomo = BohrAtom(Z=1)
   atomo.energy_level(1)   # -13.605693
   atomo.energy_level(2)   # la cuarta parte

Para el He+ (``Z=2``) la energía del mismo nivel es cuatro veces la del hidrógeno.

Radio de la órbita
------------------

:meth:`bohrpy.BohrAtom.orbit_radius` devuelve el radio en metros:

.. math::

   r_n = a_0\,\frac{n^2}{Z}

``a_0`` es el radio de Bohr, :data:`bohrpy.A_0`. En el hidrógeno, el nivel 1 mide 0.529 Å y el nivel 2 el cuádruple. Para pasarlo a ångströms se multiplica por ``1e10``.

Transiciones
------------

:meth:`bohrpy.BohrAtom.transition` resta las energías de dos niveles y calcula el fotón. Devuelve un diccionario:

.. list-table::
   :header-rows: 1

   * - Clave
     - Contenido
   * - ``delta_E_eV``
     - Diferencia de energía, en eV
   * - ``frequency_Hz``
     - Frecuencia, en Hz
   * - ``wavelength_m``
     - Longitud de onda, en metros
   * - ``type``
     - ``"emisión"`` si el electrón baja de nivel, ``"absorción"`` si sube

La frecuencia y la longitud de onda salen de :math:`f = E / h` y :math:`\lambda = c / f`, con la energía pasada a julios.

.. code-block:: python

   linea = BohrAtom().transition(3, 2)
   linea["type"]                 # "emisión"
   linea["wavelength_m"] * 1e9   # 656.11 nm, la línea H-alfa

Si los dos niveles son iguales, el método lanza ``ValueError``.

Gráficas
--------

:meth:`bohrpy.BohrAtom.plot_energy_levels` dibuja cada nivel y las flechas de emisión. El color corresponde a la serie (Lyman, Balmer, Paschen, Brackett o Pfund) y cada flecha lleva la longitud de onda en nanómetros.

:meth:`bohrpy.BohrAtom.plot_orbits` dibuja el núcleo y las órbitas circulares, con el radio en ångströms.

``show=False`` evita abrir una ventana. ``save_path`` guarda la imagen:

.. code-block:: python

   hidrogeno = BohrAtom(Z=1)
   hidrogeno.plot_energy_levels(max_n=5, show=False, save_path="niveles.png")
   hidrogeno.plot_orbits(max_n=4, show=False, save_path="orbitas.png")

Las dos funciones también se pueden llamar directamente:

.. code-block:: python

   from bohrpy import plot_energy_levels, plot_orbits

Instalación
===========

Hace falta Python 3.12 o superior.

Desde PyPI:

.. code-block:: bash

   pip install bohrpy

El paquete instala estas versiones:

- ``numpy==2.5.4``
- ``matplotlib==3.11.2``

Desde el repositorio, con las pruebas y esta documentación:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate
   pip install -e ".[test,docs]"

Para generar la página en local:

.. code-block:: bash

   sphinx-build -b html docs docs/_build/html

El ejemplo incluido en el repositorio imprime niveles y transiciones, y guarda las figuras en ``examples/figuras/``:

.. code-block:: bash

   python examples/ejemplo_uso.py

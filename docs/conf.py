"""Configuración de Sphinx para la documentación de bohrpy."""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "bohrpy"
author = "Isabel Nieto y Kevin Osorio"
release = "0.1.1"
version = "0.1.1"
language = "es"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = "bohrpy"
html_static_path = ["_static"]

autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
}
napoleon_numpy_docstring = True

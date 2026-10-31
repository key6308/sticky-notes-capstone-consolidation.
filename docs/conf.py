"""Sphinx configuration for the Sticky Notes project."""

import os
import sys

import django

sys.path.insert(0, os.path.abspath(".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sticky_notes.settings")
django.setup()

project = "Sticky Notes App"
copyright = "2026, Keshawn Edwards"
author = "Keshawn Edwards"
release = "1.0"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"

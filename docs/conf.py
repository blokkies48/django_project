import os
import sys
import django

sys.path.insert(0, os.path.abspath('../political_project'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'political_project.settings'
django.setup()
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'capstone-3-1'
copyright = '2022, Jonathan'
author = 'Jonathan'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
                'sphinx.ext.autodoc',
                'sphinx.ext.viewcode',
                'sphinx.ext.napoleon'\
            ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

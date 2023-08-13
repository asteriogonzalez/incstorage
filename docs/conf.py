#!/usr/bin/env python
#
# incstorage documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import incstorage  # noqa: E402

extra_paths = list(incstorage.__path__)

# add virtual env
for top in incstorage.__path__:
    for root, folers, files in os.walk(os.path.dirname(top)):
        for name in folers:
            if name in ('site-packages',):
                print(f">>> {root}/{name}")
                extra_paths.append(os.path.join(root, name))

for path in extra_paths:
    sys.path.insert(0, os.path.abspath(path))

# for path in sys.path:
# print(path)


# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    # "sphinx.ext.todo",
    "sphinx.ext.coverage",
    # "sphinx.ext.inheritance_diagram",
    #'sphinx.ext.imgmath',
    # "sphinx.ext.mathjax",
    # "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    # "sphinx.ext.graphviz",
    "sphinxcontrib.mermaid",
    "recommonmark",
    # PDF support
    "rst2pdf.pdfbuilder",
]
autodoc_default_options = {
    "members": True,
    "private-members": True,
}
autodoc_typehints = "description"

autosummary_generate = True

autoapi_dirs = ['../incstorage']

inheritance_graph_attrs = dict(
    rankdir="TD",
    fontsize=8,
    # ratio="compress",
    size='"6.0, 8.0"'
    # rankdir="TD", size='"3.0, 4.0"', fontsize=10, ratio="compress"
)
inheritance_node_attrs = dict(
    # shape="rounded", fontsize=10, height=0.75, color="dodgerblue1", style="filled"
    # shape="ellipse",
    # shape="egg",
    # shape="plain",
    shape="rectangle",
    fontsize=8,
    height=0.75,
    color="dodgerblue1",
    style="filled",
)

mathjax_config = {
    "extensions": ["tex2jax.js"],
    "jax": ["input/TeX", "output/HTML-CSS"],
}
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = 'Incremental Storage'
copyright = "2023, Asterio Gonzalez"
author = "Asterio Gonzalez"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = incstorage.__version__
# The full version, including alpha/beta/rc tags.
release = incstorage.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "EN"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "build",
    "_build",
    "_templates",
    "_autosummary",
    "Thumbs.db",  # or won't detect the autogenerated files
    ".DS_Store",
    "*.log",
    ".*",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
html_theme = "furo"
# html_theme = 'traditional'
# html_theme = 'press'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# alabaster
html_theme_options = {
    # "logo": "logo.png",
    # "github_user": "asteriogonzalez",
    # "github_repo": "python-coding-challenge",
    # "font_family": "Arial",
    # "body_max_width": "75%",
    # "page_width": "75%",
    #'page_width': 'auto',
    # "font_size": "12px",
    # "base_bg": "#fff",
}
# furo
html_title = project
html_theme_options = {
    # "light_logo": "logo-light-mode.png",
    # "dark_logo": "logo-dark-mode.png",
    "light_logo": "logo.jpeg",
    "dark_logo": "logo.jpeg",
    "announcement": "<em>Documentation in progress</em>",
    "source_repository": "https://github.com/pradyunsg/furo/",
    "source_branch": "main",
    "source_directory": "docs/",
    # prefers-color-scheme: dark
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
    # "index": "your-custom-landing-page.html"
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_favicon = "_static/favicon.ico"
# html_css_files = [
#     "custom.css",
# ]

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'incstoragedoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'incstorage.tex',
        'Incremental Storage Documentation',
        'Asterio Gonzalez',
        'manual',
    ),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        'incstorage',
        'Incremental Storage Documentation',
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'incstorage',
        'Incremental Storage Documentation',
        author,
        'incstorage',
        'One line description of project.',
        'Miscellaneous',
    ),
]


# -- Options for PDF output ----------------------------------------

pdf_documents = [
    ("index", "rst2pdf", 'incstorage', "Asterio"),
]

# def setup(app):
#     app.add_css_file("custom.css")  # may also be an URL

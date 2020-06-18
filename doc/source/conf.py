# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Imports and Path setup ---------------------------------------------------

import sys, os, re
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))
# Root of the reg_generator package
sys.path.insert(
    1, os.path.abspath("{}/reg_generator/pkg".format(os.getenv("PYTHONSOURCE")))
)
# Root of the reg_interface package
sys.path.insert(
    1, os.path.abspath("{}/reg_interface/pkg".format(os.getenv("PYTHONSOURCE")))
)

if os.getenv("USE_DOXYREST"):
    # path for doxyrest sphinx extensions
    sys.path.insert(
        1, "{:s}/share/doxyrest/sphinx".format(os.getenv("DOXYREST_PREFIX"))
    )

    import doxyrest

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# General information about the project.

# List all authors here
authorlist = [
    "Mykhailo Dalchenko",
    "Evaldas Juska",
    "Robert King",
    "Andrew Peck",
    "Jared Sturdy",
]

project = u"reg_utils"
authors = ", ".join(authorlist)
copyright = u"2018—{:d} {:s}".format(datetime.date.today().year, authors)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = os.popen("git describe --abbrev=6 --dirty --always --tags").read().strip()
try:
    release = re.sub("^v", "", release,)  #'1.0.0'
    # The short X.Y version.
    version = "{0}.{1}".format(*release.split("."))  #'1.0'
except Exception as e:
    print(e)
    version = "untagged-{0}".format(release)
    pass  # release = "0.0.0"

print("Version {}".format(version))
print("Release {}".format(release))


# -- General configuration ----------------------------------------------------

# # Tell sphinx what the primary language being documented is.
# primary_domain = "cpp"

# # Tell sphinx what the pygments highlight language should be.
# highlight_language = "cpp"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Extension configuration --------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    ## sphinx extensions
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.imgmath",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    ## sphinxcontrib
    "sphinxcontrib.napoleon",
    "sphinxcontrib.srclinks",
    ## sphinx external
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinx_tabs.tabs",
    "m2r",
]

extensions += ["autoapi.extension"]
extensions += ["breathe", "exhale"]
if os.getenv("USE_DOXYREST"):
    extensions += ["doxyrest", "cpplexer"]

## -- autoapi python configuration --------------------------------------------

autoapi_type = "python"
autoapi_python_use_implicit_namespaces = True
autoapi_dirs = [
    "{}/reg_generator/pkg".format(os.getenv("PYTHONSOURCE")),
    "{}/reg_interface/pkg".format(os.getenv("PYTHONSOURCE")),
]
autoapi_add_toctree_entry = False
autoapi_keep_files = True
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
    "special-members",
    "show-inheritance-diagram",
    "show-module-summary",
]
autoapi_ignore = ["*migrations*", "*conf.py", "*setup.py"]
autoapi_template_dir = "_templates/autoapi"

## -- Breathe+Exhale configuration --------------------------------------------

breathe_projects = {
    "rwreg_x86": "../doxybuild/xml",
    "rwreg": "../exhalebuild/xml",
}

breathe_default_project = "rwreg"
## https://github.com/svenevs/exhale/issues/86
## work around issue where documentation is done in implementation files rather than headers as per conventions
breathe_implementation_filename_extensions = []
# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder": "./exhale-api",
    "rootFileName": "api.rst",
    "rootFileTitle": "API documentation for the rwreg library",
    "doxygenStripFromPath": "{}".format(os.path.abspath("../../rwreg/x86_64/")),
    # Suggested optional arguments
    # "lexerMapping": {r".*\.md": "md",},
    "createTreeView": True,
    # "afterTitleDescription": "",
    # "fullApiSubSectionTitle": "",
    # "afterBodySummary": "",
    # "unabridgedOrphanKinds": [""],
    "fullToctreeMaxDepth": 1,
    # TIP: if using the sphinx-bootstrap-theme, you need
    "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin": """
PROJECT_NAME = rwreg
PROJECT_NUMBER = {}
PROJECT_BRIEF = "Read/write register library for the CTP7 Zynq"
REPEAT_BRIEF = YES
INHERIT_DOCS = YES
MARKDOWN_SUPPORT = YES
AUTOLINK_SUPPORT = YES
SUBGROUPING = YES
EXTRACT_LOCAL_CLASSES = YES
CASE_SENSE_NAMES = YES
SHOW_INCLUDE_FILES = YES
GENERATE_HTML = YES
INLINE_INFO = YES
SORT_MEMBER_DOCS = YES
GENERATE_DEPRECATEDLIST= YES
SHOW_USED_FILES = YES
SHOW_FILES = YES
SHOW_NAMESPACES = YES
USE_MDFILE_AS_MAINPAGE = ../../README.md
INPUT = ../../README.md \
        ../../rwreg/x86_64/src \
        ../../rwreg/x86_64/include
PREDEFINED+= DOXYGEN_IGNORE_THIS
""".format(
        release
    ),
}


## -- other extension configuration -------------------------------------------

# Disable numpy docstrings for Napoleon, because they eat headers such as
# "Examples"
napoleon_numpy_docstring = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output --------------------------------------------------

html_context = {
    "display_github": True,
    "github_host": "github.com",
    "github_user": "cms-gem-daq-project",
    "github_repo": "reg_utils",
    "github_version": "release/legacy-1.1",
    "conf_py_path": "/doc/source/",
    "last_updated": "{}".format(os.popen("date -u +'%a %b %d %Y %T %Z'").read().strip()),
    "commit": "{}".format(os.popen("git describe --abbrev=8 --dirty --always").read().strip()),
}

html_show_sourcelink = True

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "reg_utils: Register Utilities for GEM Electronics"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "reg_utils"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

## Show only the logo at the top of the sidebar
# logo_only

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "navigation_depth": 50,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_extra_path = ["../build/html"]

# Custom CSS
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "{}/css/rtd-custom.css".format(os.getenv("GEM_DOCS_URL")),
]

# Custom JavaScript
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_js_files = [
    # # enable for arrow key navigation
    # "{}/scripts/js/guides-navigation.js".format(os.getenv("GEM_DOCS_URL")),
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, the index is split into individual pages for each letter.
# html_split_index = False


# -- Options for HTMLHelp output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "reg_utils-doc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "reg_utils.tex", u"reg\\_utils Documentation", authors, "manual",),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "reg_utils", u"reg_utils Documentation", [authors], 1,)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "reg_utils",
        u"reg_utils Documentation",
        authors,
        "reg_utils",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# This config value contains the locations and names of other projects that
# should be linked to in this documentation.
intersphinx_mapping = {
    "cmsgemos": (os.getenv("EOS_SITE_URL") + "/docs/api/cmsgemos/latest", None,),
    "gemplotting": (os.getenv("EOS_SITE_URL") + "/docs/api/gemplotting/latest", None,),
    "vfatqc": (os.getenv("EOS_SITE_URL") + "/docs/api/vfatqc/latest", None,),
    "ctp7_modules": (
        os.getenv("EOS_SITE_URL") + "/docs/api/ctp7_modules/latest",
        None,
    ),
    "xhal": (os.getenv("EOS_SITE_URL") + "/docs/api/xhal/latest", None,),
}

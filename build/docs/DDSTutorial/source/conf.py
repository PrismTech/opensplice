# -*- coding: utf-8 -*-
#
# OpenSplice DDS Tutorial build configuration file, created by
# ReST Editor on 24-Mar-2015
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import time
# import liteconfig

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['sphinx.ext.todo']
#extensions = ['sphinx.ext.todo', 'numfig']

extensions = ['sphinx.ext.todo', 'sphinx.ext.ifconfig']

def setup(app):
    app.add_config_value('rmi_languages', '', True)

#rmi_languages = 'C++ and Java'
rmi_languages = 'C++'
#rmi_languages = 'Java'
rst_prolog = """
.. |rmi_langs| replace:: C++
.. |product_name| replace:: OpenSplice
"""

#.. |rmi_langs| replace:: C++ and Java





# Add any paths that contain templates here, relative to this directory.
templates_path = [u'_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = u'utf-8-sig'

# The master toctree document.
master_doc = u'index'

# General information about the project.
project = u'The Data Distribution Service Tutorial'

#copyright = u'2015, PrismTech'
this_year = time.strftime( '%Y' )
copyright = u'{y}, PrismTech'.format( y = this_year )
print 'Copyright string is:', copyright

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = u's'
#version = liteconfig.version
#version = u'6.x'

# The full version, including alpha/beta/rc tags.
#release = u's'
#release = version
#release = u'.0'
#print 'Short version string is:', version
#print 'Full version string is:', release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = u'en'


# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# Force blank date with today = ' ' (space, not empty string)
today = ' '
# ***************
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = u'sphinxdoc'
html_theme = u'vortextheme'
html_theme_path = ['../../.']

#build theme directory in lite using environment variable, so shared amongst books
# insight team can delete,
#html_theme_path = [os.environ['VL_HOME'] + '/build/docs']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'The Data Distribution Service Tutorial'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'DDS Tutorial'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = './images/Vortex_logo_2014.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []
html_static_path = [u'_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'The Data Distribution Service Tutorial'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = u'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = u'10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', 'OpenSplice_DDSTutorial.tex', u'The DDS Tutorial', u'', 'manual', True)]
# Note 'author' field empty
# Added 'True' to end of generated line to suppress 'Index & Tables'

# A dictionary that contains LaTeX snippets that override those Sphinx usually 
# puts into the generated .tex files.
latex_elements = { 'babel': '\\usepackage[english]{babel}' }

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
latex_logo = 'images/Vortex-Cover.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# THIS GETS RID OF BLANK PAGES AT ENDS OF CHAPTERS & ToC
latex_elements = {
  'classoptions': ',openany, oneside',
  'babel': '\\usepackage[english]{babel}'
}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', 'DDS_Tutorial', u'DDS_Tutorial Documentation', [u'PrismTech'], 1)]

# -- Additional options --------------------------------------------------------

todo_include_todos = True

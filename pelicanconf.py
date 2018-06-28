#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

#PLUGIN_PATHS = ['pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup'
#    'tipue_search'
]

# For Tipue Search Plugin
DIRECT_TEMPLATES = ('index','tags','categories','authors','archives','search')

I18N_TEMPLATES_LANG = 'en'

AUTHOR = 'Sundar Nadimpalli'
SITENAME = 'Stories by Sundar'
SITEURL = ''

# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']

# Top Menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'America/Cancun'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/SunNadimpalli'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}


# S3 End Point = stories.sundarnadimpalli.com.s3-website.ca-central-1.amazonaws.com

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

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# S3 End Point = stories.sundarnadimpalli.com.s3-website.ca-central-1.amazonaws.com


#<link rel="apple-touch-icon" sizes="57x57" href="/apple-icon-57x57.png">
#<link rel="apple-touch-icon" sizes="60x60" href="/apple-icon-60x60.png">
#<link rel="apple-touch-icon" sizes="72x72" href="/apple-icon-72x72.png">
#<link rel="apple-touch-icon" sizes="76x76" href="/apple-icon-76x76.png">
#<link rel="apple-touch-icon" sizes="114x114" href="/apple-icon-114x114.png">
#<link rel="apple-touch-icon" sizes="120x120" href="/apple-icon-120x120.png">
#<link rel="apple-touch-icon" sizes="144x144" href="/apple-icon-144x144.png">
#<link rel="apple-touch-icon" sizes="152x152" href="/apple-icon-152x152.png">
#<link rel="apple-touch-icon" sizes="180x180" href="/apple-icon-180x180.png">
#<link rel="icon" type="image/png" sizes="192x192"  href="/android-icon-192x192.png">
#<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
#<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
#<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
#<link rel="manifest" href="/manifest.json">
#<meta name="msapplication-TileColor" content="#ffffff">
#<meta name="msapplication-TileImage" content="/ms-icon-144x144.png">
#<meta name="theme-color" content="#ffffff">

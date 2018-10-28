#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Red Cabbage'
SITENAME = 'The Dream of Cabbage'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/' ),
         )

# Social widget
SOCIAL = (('LinkedIn of Red Cabbage', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/home/cabbage/RCDevWS/saladworks/devenv/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n'],
        }

# Specify theme

THEME = "/home/cabbage/RCDevWS/saladworks/devenv/saladworks/themes/pelican-bootstrap3"

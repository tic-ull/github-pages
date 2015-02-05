#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Universidad de La Laguna'
SITENAME = u'<site_name>'
SITEURL = '<site_url>'

PATH = 'content'

TIMEZONE = 'Atlantic/Canary'

DEFAULT_LANG = u'en'

# Disable link generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ULL_CSS_URL = 'http://static.ull.es/v3/dist/css/ull.min.css'

# Blogroll
LINKS = (('Universidad de La Laguna (ULL)', 'http://www.ull.es/'),)

# Social widget
"""
SOCIAL = (('Facebook', '<facebook_url>'),
          ('Twitter', '<twitter_url>'),
          ('Google plus', '<google_plus_url>'),
          ('Youtube', '<youtube_url>'),)
"""

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='themes/pelican-bootstrap3'
#JUMBOTRON_IMAGE_URL='images/banner.jpg'

STATIC_PATHS = ['images', 'css', 'js', 'php']
# Uncomment to be able to use the contact form
# CUSTOM_JS='js/app.js'

# Páginas
PAGE_ORDER_BY = 'sortorder'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# Panel de financiadores
"""
WORK_SUPPORTED_BY_HTML = (('This work is being supported by <suporter>'),
                          ('<You can put here html, like an image>'),)
"""

# Licencia
"""
LICENSE = (('License url'), ('License image'),)
"""

# Desactivar elementos propios de un blog
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_ARCHIVES_ON_MENU = False

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARTICLE_SAVE_AS = ''

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


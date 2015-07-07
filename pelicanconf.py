#!/usr/bin/env python
#-*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Paulo Miranda Moreira'
SITENAME = 'Eu, Paulo'
SITESUBTITLE = 'Programa\xe7\xe3o, estat\xedstica e vida...'
SITEURL = ''
GITHUB_URL = 'http://github.com/EuPaulo'
LOCALE = 'pt_BR.utf8'
THEME = "iris"
TWITTER_USERNAME = 'paulomiramor'
EMAIL = 'paulomiramor@gmail.com'

SUMMARY_MAX_LENGTH = 20

PATH = 'content'


STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

#LOAD_CONTENT_CACHE = False

RELATIVE_URLS = True


TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'


DEFAULT_CATEGORY = 'Artigos'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

TYPOGRIFY = True
SLUGIFY_SOURCE = 'title'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
 #        ('Python.org', 'http://python.org/'),
  #       ('Jinja2', 'http://jinja.pocoo.org/'),
   #      ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/paulomiramor'),
          ('linkedin', 'https://br.linkedin.com/pub/paulo-moreira/9a/868/81'),
          ('github', 'https://github.com/EuPaulo'),
          )

DEFAULT_PAGINATION = 5

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from hashlib import md5
from os import getenv

AUTHOR = 'Mazk'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
SITENAME = "MazkCorner"
SITEURL = '//' + getenv("SITEURL", default='localhost:8000')
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
LOCALE = u'zh_CN.utf8'

DEFAULT_DATE_FORMAT = u"%y年%m月%d日"

DISQUS_SITENAME = 'mazk'
DISQUS_DISPLAY_COUNTS = True
#GOOGLE_ANALYTICS = 'UA-29540705-1'


TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

TWITTER_USERNAME = 'MaZhengke'

DEFAULT_PAGINATION = 8

STATIC_PATHS = ['extra','images','extra/robot.txt','extra/readme.md','images/favicon.ico']

import os
EXTRA_PATH_METADATA = {
    os.path.join('images','favicon.ico'): {'path': 'favicon.ico'},
    os.path.join('images','favicon.ico'): {'path': 'images/favicon.ico'},
    os.path.join('extra','robot.txt'): {'path': 'robot.txt'},
    os.path.join('extra','readme.md'): {'path': 'readme.md'}
}

IGNORE_FILES = ['readme.md']
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = (".git","readme.md","robot.txt","favicon.ico")
PLUGIN_PATHS = ['pelican-plugins']
THEME = "pelican-bootstrap3"


I18N_SUBSITES = { }

I18N_UNTRANSLATED_ARTICLES = "remove"

PLUGINS = ["i18n_subsites",
           "better_codeblock_line_numbering",
           "plantuml",
           "youku",
           "youtube",
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           'twitter_bootstrap_rst_directives',
           "render_math",
           'extract_toc',
           "sitemap",
           'summary']

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Theme options

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
MD_EXTENSIONS = ['admonition','toc','codehilite(css_class=highlight)','extra']


DOCUTIL_CSS = True
TYPOGRIFY = False
PYGMENTS_STYLE = 'pygments'
GITHUB_USER = 'Mazk'
GITHUB_SHOW_USER_LINK = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
DISPLAY_TAGS_INLINE = True
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.rst'

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives',
                     'tags'))

#TWITTER_USERNAME = 'farseerfc'
#TWITTER_WIDGET_ID = "538997172142759936"

AVATAR = 'images/avatar.jpg'
ABOUT_PAGE = "pages/about.html"
ABOUT_ME = """<h3 style="text-align:center">
<a href="https://twitter.com/MaZhengke"                  target="_blank">
<i class="fa fa-twitter" style="text-align:center"></i></a>
<a href="https://github.com/mazk"                   target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="http://weibo.com/mazk1996"                     target="_blank">
<i class="fa fa-weibo" style="text-align:center"></i></a>
<a href="http://www.facebook.com/mazk96"              target="_blank">
<i class="fa fa-facebook" style="text-align:center"></i></a>
<a href="https://plus.google.com/u/0/110727594920348174240/posts" target="_blank">
<i class="fa fa-google-plus" style="text-align:center"></i></a>
</h3>
"""


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
        },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
        }
    }
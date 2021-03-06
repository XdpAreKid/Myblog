# -*- coding: utf-8 -*-

import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ''
DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.blog.context_processors.theme',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'apps.blog',
    'simditor',
    'compressor',
    'django_comments_xtd',
    'django_comments',
]

SITE_ID = 1
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

COMMENTS_APP='django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_CONFIRM_EMAIL=False

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True
USE_L10N = True
USE_TZ = False

GOOGLE_ANALYTICS_ID = 'you google analytics id'
DISQUS_NAME = "YOU DISQUE SHORT NAME"

SIMPLEMDE_OPTIONS = {
    'placeholder': 'haha',
    'status': False,
    'autosave': {
        'enabled': True
    }
}


SIMDITOR_UPLOAD_PATH = 'uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'

SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown', 'emoji'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload'
    },
    'emoji': {
        'imagePath': '/static/simditor/images/emoji/'
    }
}

# ---------------------------------------------------------------
# 主题配置
# ---------------------------------------------------------------
SITE_TITLE = "Xdp's Notes"
SITE_SUBTITLE = u"一样的世界，不一样的眼光"
KEYWORDS = "DeepLearning, Python"

# ---------------------------------------------------------------
# Menu Settings
# ---------------------------------------------------------------
MENU = OrderedDict(sorted({"home": {"label": u"首页", "path": "/", "icon": "home", "position": 1},
                           "categories": {"label": u"分类", "path": "/categories", "icon": "th", "position": 3},
                           "archives": {"label": u"归档", "path": "/archives", "icon": "archive", "position": 2},
                           "tags": {"label": u"标签", "path": "/tags", "icon": "tags", "position": 4},
                           "about": {"label": u"关于", "path": "/about", "icon": "user", "position": 5},
                           }.items(),
                          key=lambda t: t[1]['position']))

SCHEME = "Pisces"

SOCIAL = OrderedDict(
    sorted({"GitHub": {"label": u"GitHub", "link": "https://github.com/XdpAreKid", "social_icons": "github",
                       "position": 1},
            "Zhihu": {"label": u"知乎", "link": "https://www.zhihu.com/people/xu-mao-74", "social_icons": "",
                      "position": 5},
            "Glances": {"label": u"glances", "link": "http://glances.xdp.space", "social_icons": "area-chart",
                                  "position": 2},
            "jupyter": {"label": u"jupyter", "link": "http://jupyter.xdp.space", "social_icons": "list-alt",
                                  "position": 3},

            }.items(), key=lambda t: t[1]['position']))


SIDEBAR = {"position": "left",
           "display": "post"
           }

GOOGLE_SITE_VERIFICATION = "your google site verification"
GOOGLE_ANALYTICS = "you google analytics id"
USE_MOTION = True
FANCYBOX = True
RSS = '/rss'
VERSION = '5.0.1'
ALIPAY = STATIC_URL+"pay/alipay.jpg"
WECHATPAY = STATIC_URL+"pay/wechat_pay.jpg"


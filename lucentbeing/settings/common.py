'''Common settings for lucentbeing.com.'''

import os

# Paths and URLs.
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__)))
)

ADMINS = (
    ('P.C. Shyamshankar', 'sykora@lucentbeing.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Asia/Calcutta'

LANGUAGE_CODE = 'en-us'

USE_I18N = False
USE_L10N = False

SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    'django.contrib.syndication',
    'django.contrib.sitemaps',

    'south',

    'djournal',
    'ripwrap',
    'taggit',
)

ROOT_URLCONF = 'lucentbeing.urls'

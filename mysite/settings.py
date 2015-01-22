# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ndd%s(70+b^yf2)7)+ji6_n4d_y23%%y0fo_&$f8pbco!j8wl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Одна проблема
# Папку templates и файл myview.html мы создали самостоятельно,
# а значит Django о них ничего не знает
# необходимо добавить каталог с шаблонами в settings.py нашего проекта
# Читаем доки https://docs.djangoproject.com/en/1.6/ref/settings/#template-dirs
# 
# Вот мой полный путь к шаблонам:/home/nik/django-developer/env16/mysite/templates

# TEMPLATE_DIRS - это кортеж, состоящий из каталогов где Django необходимо искать наши шаблоны
# Используются абсолютные пути!


TEMPLATE_DIRS = (
    '/home/nik/django-developer/env16/mysite/templates',
# == Урок 6. Сюда хуйнули это, чтобы ебать знало
    '/home/nik/django-developer/env16/mysite/article/templates',

)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
# Встроенное в Django приложение, отвечает за манипуляцию статичных файлов
    'django.contrib.staticfiles',
    'article',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db-nik-yobana.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# Эта строка отвечает за обработку статичных файлов
# Базовый каталог, на который джанго будет ссылаться при поиске статичных файлов он должен начинаться на static
STATIC_URL = '/static/'


# Урок 7. Static files dirs нужно использовать в том случае, если нам статик фалс должны быть доступны не внутри приложения, а в самом проекте.
# Эти файлы доступны глобально по всему нашему проекту
STATICFILES_DIRS = (
    ('static', '/home/nik/django-developer/env16/mysite/static'),
)
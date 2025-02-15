"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5$$a&@_c*e=ybe7$r_kt06l$gg$q8&kjrj4_diplp133axeh17'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# We also add the whitelist to allow the cors.
# Alternatively we can add CORS_ORIGIN_ALLOW_ALL = True, but its risky for deployment
# This also provides a security level, so people who try to access to the "backend ip" would be denied

CORS_ORIGIN_WHITELIST = [
     'http://localhost:5173',
     'http://127.0.0.1:5173',
    #  NGROK LINK FRONT
     'https://6943-186-78-252-47.ngrok-free.app'
]



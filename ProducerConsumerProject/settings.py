"""
Django settings for ProducerConsumerProject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '$$p!yrh)$1mw&h!dmvaxsswwhq)*7$rg38q09j+s^)+r@6vynr'

INSTALLED_APPS = [
    'producer.apps.ProducerConfig'
]

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'entries.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'entries',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Number of entries to generate by the producer
X = 10

# Tolerance for number of entries to generate. Final number will be between X - ALLOWANCE and X + ALLOWANCE
ALLOWANCE = 3

RABBITMQ_HOST = 'localhost'

# Notification message the consumer waits for to process entries
NOTIFICATION_MESSAGE = 'created'
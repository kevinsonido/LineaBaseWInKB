from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []





# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#DATABASES = {
 #   'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
 #  }
#}

#    'USER':'root',
#'PASSWORD': 'Java5922',
#   'localhost',

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
       'NAME':'db_prueba',
        'USER':'admin',
        'PASSWORD': 'Java5922',
          'HOST':'databasedjango.cbcjerlsrxnm.us-east-2.rds.amazonaws.com',
       'PORT':'3306',
  }
}

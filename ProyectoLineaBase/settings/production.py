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


DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
       'NAME':'db_prueba',
        'USER':'root',
        'PASSWORD': 'Java5922',
       'HOST':'localhost',
       'PORT':'3306',
  }
}


import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nv)=_h7=(#+dn7hk2#n17v406lzs#2-)l8kepd#y(u2g)g5_%-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['emmanuelbangwen.onrender.com','EmmanuelBangwen.onrender.com', 
                 '127.0.0.1', 'localhost', 'emmanuelbangwen.com',
                 '127.0.0.1', 'localhost', 'emmanuelbangwen.com/',
                 'bangwen_emmanuel.onrender.com','EmmanuelBangwen.com', 
                 'https://www.emmanuelbangwen.com/', 'https://www.emmanuelbangwen.com',
                 'https://www.EmmanuelBangwen.com/', 'https://www.EmmanuelBangwen.com',
                 'www.EmmanuelBangwen.com', 'www.EmmanuelBangwen.com/','bangri-agtech.com',
                 'bangri.onrender.com','bangri.com', 'bangri-agritech.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Base', 
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
# Si tu as un répertoire 'static' dans ton projet racine (par exemple, /quizapp/static/)

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = '/static/'
MEDIA_URL='/images/'

STATICFILES_DIRS=[
  os.path.join(BASE_DIR, 'static')  
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


EMAIL_HOST_USER = 'bikoyemmanuel531@gmail.com'
EMAIL_HOST_PASSWORD = 'ywvm uols wmhe jymi'
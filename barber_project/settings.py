import os # Importamos os para manejar variables de entorno
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: En producción, es mejor usar variables de entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-907$w0kyu^4@)59m)l-k*+wtki9*%9131ff%-e5ggci6@+ul!w')

# SEGURIDAD: DEBUG debe ser False en producción para no mostrar datos técnicos
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Aquí agregamos la URL que te dio Render y mantenemos local para pruebas
ALLOWED_HOSTS = ['barberiajhonnyboy.onrender.com', 'localhost', '127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ventas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # AGREGADO: Para manejar archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'barber_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.processors.auth',
                'django.contrib.messages.processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'barber_project.wsgi.application'

# Base de Datos: Por ahora mantenemos SQLite, pero Render lo borrará cada que reinicies.
# Si vas a rentarlo, pronto debemos cambiar a PostgreSQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración para Tijuana / México
LANGUAGE_CODE = 'es-mx' # Cambiado a Español
TIME_ZONE = 'America/Tijuana' # Cambiado a tu zona horaria
USE_I18N = True
USE_TZ = True

# Archivos Estáticos (CSS, JS, Imágenes)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directorio donde Render guardará los estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
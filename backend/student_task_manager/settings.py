import os
from pathlib import Path
import dj_database_url # Import this

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Get SECRET_KEY from env, fallback to insecure key for dev only
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-your-dev-key')

# SECURITY: False in production, True locally
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS: Allow Render URL
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # <--- ADD THIS
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # <--- ADD THIS (Must be top)
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <--- ADD THIS (For Admin static files)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ... rest of your middleware
]

# CORS CONFIGURATION
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://127.0.0.1:5500').split(',')
CORS_ALLOW_CREDENTIALS = True

# DATABASE CONFIGURATION (Auto-switch SQLite <-> Postgres)
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}

# STATIC FILES (Required for Admin Panel on Render)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
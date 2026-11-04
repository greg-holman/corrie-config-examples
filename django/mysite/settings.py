"""Django settings read from environment variables.

Start the app with the Corrie Config launcher so the variables come from config.corrie.io:
    CORRIE_CONFIG_KEY=cfg_... sh launch.sh -- gunicorn mysite.wsgi
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Django's own settings. SECRET_KEY has no default on purpose: the app refuses to start without it.
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.environ.get("DEBUG") == "true"
ALLOWED_HOSTS = [h.strip() for h in os.environ.get("ALLOWED_HOSTS", "localhost").split(",") if h.strip()]

# Your app's settings.
API_URL = os.environ.get("API_URL", "")
FEATURE_NEW_CHECKOUT = os.environ.get("FEATURE_NEW_CHECKOUT") == "true"
DB_HOST = os.environ.get("DB_HOST", "")
DB_POOL = int(os.environ.get("DB_POOL", "5"))

INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware", "django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "mysite.urls"
WSGI_APPLICATION = "mysite.wsgi.application"

# SQLite keeps the example self-contained. With PostgreSQL, build DATABASES from DB_HOST and friends.
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True

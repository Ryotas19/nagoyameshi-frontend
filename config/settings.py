from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure--7a-4dq259)u9q*l)lkv%93g^3$w-z6j3t$2kxz2l%v!+(f&h+"
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.151.187'] # IPアドレスはご自身の環境に合わせてください
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.sites','rest_framework','corsheaders','allauth','allauth.account','allauth.socialaccount','dj_rest_auth','dj_rest_auth.registration','django_filters','accounts','api',]
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware','allauth.account.middleware.AccountMiddleware',]
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend','allauth.account.auth_backends.AuthenticationBackend',]
ROOT_URLCONF = "config.urls"
TEMPLATES = [ { "BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True, "OPTIONS": { "context_processors": [ "django.template.context_processors.request", "django.contrib.auth.context_processors.auth", "django.contrib.messages.context_processors.messages", ], }, }, ]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = { "default": { "ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3", } }
AUTH_PASSWORD_VALIDATORS = [ { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", }, { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", }, { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", }, ]
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = 'accounts.CustomUser'
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', 'rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter',],}
SIMPLE_JWT = { 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), }
REST_USE_JWT = True
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none' # 開発を簡単にするため 'none' に変更
REST_AUTH = {'TOKEN_MODEL': None, 'USE_JWT': True, 'JWT_AUTH_HTTPONLY': False,}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CORS_ALLOWED_ORIGINS = [ "http://localhost:3000", "http://127.0.0.1:3000", "http://192.168.151.187:3000", ]
FRONTEND_URL = 'http://192.168.151.187:3000'
import os
from pathlib import Path
import environ
import dj_database_url  # Import dj-database-url
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Inisialisasi django-environ. Kita akan gunakan os.environ.get untuk beberapa hal
# agar tidak bentrok dengan sistem environment Render.
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# ==============================================================================
# PENGATURAN INTI UNTUK PRODUKSI
# ==============================================================================

# Ambil SECRET_KEY dari environment variable. JANGAN PERNAH menaruhnya langsung di sini.
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG akan False di production, kecuali diatur secara eksplisit ke 'True'
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS akan mengambil dari environment variable.
# Render secara otomatis menyediakan RENDER_EXTERNAL_HOSTNAME.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ==============================================================================
# APLIKASI DAN MIDDLEWARE
# =================================================Guna=============================

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # WhiteNoise untuk menyajikan file statis
    'django.contrib.staticfiles',
    'tinymce',
    'Tampilanutama_app',
    'pendaftaran_app',
    'chatbot_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware WhiteNoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_pendaftaran.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'project_pendaftaran.wsgi.application'

# ==============================================================================
# DATABASE
# ==============================================================================

# Menggunakan dj_database_url untuk membaca DATABASE_URL dari environment
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600  # Waktu koneksi tetap terbuka (dalam detik)
    )
}

# ==============================================================================
# VALIDASI PASSWORD DAN INTERNASIONALISASI
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'id' # Ganti ke Bahasa Indonesia
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# STATIC & MEDIA FILES
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# Konfigurasi storage untuk WhiteNoise agar efisien
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==============================================================================
# PENGATURAN LAIN-LAIN
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Konfigurasi Email (menggunakan SendGrid) ---
# Pastikan variabel ini diatur di environment hosting Anda
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# --- Konfigurasi Gemini AI ---
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# --- Konfigurasi Login/Logout ---
LOGIN_REDIRECT_URL = 'dashboard_pendaftar'
LOGIN_URL = 'login_pendaftar'

# --- JAZZMIN SETTINGS ---
# Kode JAZZMIN_SETTINGS Anda sudah cukup baik, yang diperbaiki hanya duplikasi 'sidebar_links'
JAZZMIN_SETTINGS = {
    "site_title": "Admin PK IMM FTIK",
    "site_header": "Sistem Pendaftaran",
    "site_brand": "Admin PK IMM FTIK",
    "welcome_sign": "Selamat Datang di login, website PK IMM FTIK",
    "site_logo": "img/logo_IMM.png",
    "login_logo": "img/logo_IMM.png",
    "site_logo_classes": "img-responsive",
    "favicon": "favicon/favicon.ico",
    "logout_url": "admin:logout",
    "copyright": "PK IMM FTIK | MEDKOM ",
    "show_version": False,
    "show_ui_builder": True,
    "topmenu_links": [
        {"name": "Beranda", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Situs Web", "url": reverse_lazy("tampilan_utama_app:home"), "new_window": True},
        {"model": "auth.User"},
    ],
    "sidebar_links": [
        {"name": "Dashboard", "url": "admin:index", "icon": "fas fa-th-large"},
        {
            "name": "Pendaftaran App", "url": "#", "icon": "fas fa-folder",
            "children": [
                {"name": "Berkas Pendaftaran", "url": "admin:pendaftaran_app_berkaspendaftaran_changelist", "icon": "fas fa-file-alt"},
                {"name": "Field Ekstraksi AI", "url": "admin:pendaftaran_app_basispengetahuan_changelist", "icon": "fas fa-brain"},
                {"name": "File PDF", "url": "admin:pendaftaran_app_filepdf_changelist", "icon": "fas fa-file-pdf"},
                {"name": "Konfigurasi Unggah", "url": "admin:pendaftaran_app_konfigurasiunggah_changelist", "icon": "fas fa-cogs"},
                {"name": "Pas Foto", "url": "admin:pendaftaran_app_pasfoto_changelist", "icon": "fas fa-image"},
            ]
        },
        {
            "name": "Chatbot App", "url": "#", "icon": "fas fa-robot",
            "children": [
                {"name": "Aturan Chatbot", "url": "admin:chatbot_app_aturanchatbot_changelist", "icon": "fas fa-comments"},
                {"name": "Chat Sessions", "url": "admin:chatbot_app_chatsession_changelist", "icon": "fas fa-history"},
                {"name": "Entri Basis Pengetahuan", "url": "admin:chatbot_app_basispengetahuan_changelist", "icon": "fas fa-book"},
            ]
        },
        {
            "name": "Autentikasi dan Otorisasi", "url": "#", "icon": "fas fa-users-cog",
            "children": [
                {"model": "auth.User", "icon": "fas fa-user"},
                {"model": "auth.Group", "icon": "fas fa-users"},
            ]
        },
    ],
    "icons": {
        "auth.user": "fas fa-user", "auth.group": "fas fa-users", "admin.index": "fas fa-th-large",
        "admin.auth": "fas fa-users-cog", "chatbot_app.ChatbotRule": "fas fa-scroll",
        "chatbot_app.chatsession": "fas fa-history", "chatbot_app.KnowledgeBaseEntry": "fas fa-book-open",
        "pendaftaran_app.berkaspendaftaran": "fas fa-file-alt", "pendaftaran_app.BasisPengetahuan": "fas fa-brain",
        "pendaftaran_app.filepdf": "fas fa-file-pdf", "pendaftaran_app.konfigurasiunggah": "fas fa-cogs",
        "pendaftaran_app.pasfoto": "fas fa-image", "tampilanutama_app.newsarticle": "fas fa-newspaper",
        "tampilanutama_app.ketuainfo": "fas fa-user-tie", "tampilanutama_app.menuitem": "fas fa-bars",
        "tampilanutama_app.siteconfiguration": "fas fa-sliders-h", "tampilanutama_app.JumbotronSlide": "fas fa-images",
    },
    "show_sidebar": True, "navigation_expanded": True, "hide_apps": [], "hide_models": [],
    "custom_css": "css/admin_custom.css", "custom_js": "js/custom_login.js",
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "vertical_tabs", "auth.group": "vertical_tabs"},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True, "footer_small_text": True, "body_small_text": False, "brand_small_text": False,
    "brand_colour": "navbar-danger", "accent": "accent-primary", "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": False, "navbar_fixed": True, "layout_boxed": False, "footer_fixed": True,
    "sidebar_fixed": True, "sidebar": "sidebar-dark-danger", "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True, "sidebar_nav_child_indent": True, "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True, "sidebar_nav_flat_style": True, "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary", "secondary": "btn-secondary", "info": "btn-info",
        "warning": "btn-warning", "danger": "btn-danger", "success": "btn-success"
    }
}

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px", "width": "100%", "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}
import os
from pathlib import Path
import environ 
import datetime
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Inisialisasi django-environ dan muat file .env
env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, True) # DEBUG default ke True jika tidak ada di .env
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env')) # Membaca file .env


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='django-insecure-7+#jiqi5h19)s=!w%t4ejp()z79rug5f+uw+wmi50!$qb(o71r'
DEBUG = True # Ambil DEBUG dari .env

ALLOWED_HOSTS = [] # Akan diatur secara dinamis di bawah jika DEBUG False

STATIC_URL = '/static/'


# Application definition
INSTALLED_APPS = [
    'jazzmin', # HARUS di atas django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'Tampilanutama_app',
    'pendaftaran_app',
    'chatbot_app',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Pastikan ini sudah ada
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


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_imm',         # Nama database baru Anda
        'USER': 'postgres',                # User postgres Anda
        'PASSWORD': 'Rizkysatrio2002',  # Ganti dengan password Anda
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tambahkan ini untuk memberitahu Django mencari static files di folder 'static' di root project
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files (for uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Konfigurasi Email (menggunakan SendGrid) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net' # PASTIKAN INI ADALAH 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# --- Konfigurasi Gemini AI ---
GEMINI_API_KEY = env('GEMINI_API_KEY')


# --- Konfigurasi Login/Logout ---
LOGIN_REDIRECT_URL = 'dashboard_pendaftar'
LOGIN_URL = 'login_pendaftar'


# --- JAZZMIN SETTINGS ---
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
    "custom_css": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
    "copyright": "PK IMM FTIK | MEDKOM ",
    "show_version": False,
    "show_ui_builder":True,

    # ### PERBAIKAN: Sidebar Links untuk kontrol penuh menu sidebar ###
    # Ini akan menggantikan perilaku default Jazzmin untuk menampilkan aplikasi di sidebar
    "sidebar_links": [
        {"name": "Dashboard", "url": "admin:index", "icon": "fas fa-th-large"}, # Item Dashboard

        # ### INI ADALAH DEFINISI DROPDOWN UNTUK "Pendaftaran App" DI SIDEBAR ###
        {
            "name": "Pendaftaran App", # Nama yang akan muncul sebagai menu parent di sidebar
            "url": "#", # URL induk, bisa juga '#' jika hanya untuk dropdown
            "icon": "fas fa-folder", # Icon untuk menu parent "Pendaftaran App"
            "children": [
                {"name": "Berkas Pendaftaran", "url": "admin:pendaftaran_app_berkaspendaftaran_changelist", "icon": "fas fa-file-alt"},
                {"name": "Field Ekstraksi AI", "url": "admin:pendaftaran_app_basispengetahuan_changelist", "icon": "fas fa-brain"},
                {"name": "File PDF", "url": "admin:pendaftaran_app_filepdf_changelist", "icon": "fas fa-file-pdf"},
                {"name": "Konfigurasi Unggah", "url": "admin:pendaftaran_app_konfigurasiunggah_changelist", "icon": "fas fa-cogs"},
                {"name": "Pas Foto", "url": "admin:pendaftaran_app_pasfoto_changelist", "icon": "fas fa-image"},
            ]
        },

        # Untuk Chatbot App, tambahkan juga di sini (sesuaikan nama modelnya)
        {
            "name": "Chatbot App",
            "url": "#",
            "icon": "fas fa-robot",
            "children": [
                {"name": "Aturan Chatbot", "url": "admin:chatbot_app_aturanchatbot_changelist", "icon": "fas fa-comments"},
                {"name": "Chat Sessions", "url": "admin:chatbot_app_chatsession_changelist", "icon": "fas fa-history"},
                {"name": "Entri Basis Pengetahuan", "url": "admin:chatbot_app_basispengetahuan_changelist", "icon": "fas fa-book"},
            ]
        },

        # Autentikasi dan Otorisasi (juga dibuat dropdown)
        {"name": "Autentikasi dan Otorisasi", "url": "#", "icon": "fas fa-users-cog", "children": [
            {"model": "auth.User", "icon": "fas fa-user"},
            {"model": "auth.Group", "icon": "fas fa-users"},
        ]},
    ],

    # ### PERBAIKAN: Hapus order_with_respect_to dan topmenu_links yang duplikat/tidak perlu ###
    # "order_with_respect_to": ["pendaftaran_app", "auth"], # Dihapus/dikomentari karena sidebar_links sudah mengambil alih

    # ### PERBAIKAN: topmenu_links dioptimalkan untuk menu atas saja, tidak perlu dropdown app di sini ###
    "topmenu_links": [
        {"name": "Beranda", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Situs Web", "url": reverse_lazy("tampilan_utama_app:home"), "new_window": True},
        {"model": "auth.User"},
        # ### PASTIKAN TIDAK ADA LAGI {"app": "pendaftaran_app"}, DI SINI ###
        # ### DAN TIDAK ADA DEFINISI DROPDOWN "Pendaftaran App" DI SINI ###
    ],

    # ### PERBAIKAN KUNCI: Definisi Menu Sidebar Secara Eksplisit ###
    # Ini akan menimpa perilaku default Jazzmin untuk menampilkan aplikasi
    "sidebar_links": [
        # Item Dashboard (biasanya paling atas)
        {"name": "Dashboard", "url": "admin:index", "icon": "fas fa-th-large"},

        # Definisi Dropdown "Pendaftaran App"
        {
            "name": "Pendaftaran App", # Ini adalah teks yang akan muncul sebagai parent yang bisa diklik
            "url": "#", # URL induk, '#' berarti hanya sebagai folder/toggle
            "icon": "fas fa-folder", # Icon untuk parent ini (seperti folder)
            "children": [
                {"name": "Berkas Pendaftaran", "url": "admin:pendaftaran_app_berkaspendaftaran_changelist", "icon": "fas fa-file-alt"},
                {"name": "Field Ekstraksi AI", "url": "admin:pendaftaran_app_basispengetahuan_changelist", "icon": "fas fa-brain"},
                {"name": "File PDF", "url": "admin:pendaftaran_app_filepdf_changelist", "icon": "fas fa-file-pdf"},
                {"name": "Konfigurasi Unggah", "url": "admin:pendaftaran_app_konfigurasiunggah_changelist", "icon": "fas fa-cogs"},
                {"name": "Pas Foto", "url": "admin:pendaftaran_app_pasfoto_changelist", "icon": "fas fa-image"},
            ]
        },

        # Definisi Dropdown "Chatbot App"
        {
            "name": "Chatbot App",
            "url": "#",
            "icon": "fas fa-robot",
            "children": [
                {"name": "Aturan Chatbot", "url": "admin:chatbot_app_aturanchatbot_changelist", "icon": "fas fa-comments"},
                {"name": "Chat Sessions", "url": "admin:chatbot_app_chatsession_changelist", "icon": "fas fa-history"},
                {"name": "Entri Basis Pengetahuan", "url": "admin:chatbot_app_basispengetahuan_changelist", "icon": "fas fa-book"},
            ]
        },

        # Definisi Dropdown "Autentikasi dan Otorisasi"
        {
            "name": "Autentikasi dan Otorisasi",
            "url": "#",
            "icon": "fas fa-users-cog",
            "children": [
                {"model": "auth.User", "icon": "fas fa-user"},
                {"model": "auth.Group", "icon": "fas fa-users"},
            ]
        },

        # Anda bisa tambahkan link lain di sidebar di sini jika diperlukan
    ],
    # ### PERBAIKAN: Ikon untuk model di sidebar dan menu lainnya ###
   "icons": {
    # --- Ikon untuk auth & admin ---
    "auth.user": "fas fa-user",
    "auth.group": "fas fa-users",
    "admin.index": "fas fa-th-large",
    "admin.auth": "fas fa-users-cog",

    # --- Ikon untuk Chatbot_App ---
    "chatbot_app.ChatbotRule": "fas fa-scroll", # Diubah agar lebih sesuai (aturan=gulungan)
    "chatbot_app.chatsession": "fas fa-history",
    "chatbot_app.KnowledgeBaseEntry": "fas fa-book-open", # Diubah agar lebih sesuai (entri=buku terbuka)

    # --- Ikon untuk Pendaftaran_App ---
    "pendaftaran_app.berkaspendaftaran": "fas fa-file-alt",
    "pendaftaran_app.BasisPengetahuan": "fas fa-brain", # Nama model disesuaikan
    "pendaftaran_app.filepdf": "fas fa-file-pdf",
    "pendaftaran_app.konfigurasiunggah": "fas fa-cogs",
    "pendaftaran_app.pasfoto": "fas fa-image",

    # --- TAMBAHAN UNTUK Tampilanutama_App ---
    "tampilanutama_app.newsarticle": "fas fa-newspaper",
    "tampilanutama_app.ketuainfo": "fas fa-user-tie",
    "tampilanutama_app.menuitem": "fas fa-bars",
    "tampilanutama_app.siteconfiguration": "fas fa-sliders-h",
    "tampilanutama_app.JumbotronSlide": "fas fa-images",
},

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [], # Pastikan ini kosong
    "hide_models": [], # Pastikan ini kosong
    "custom_css": "css/admin_custom.css", # Pastikan path ini benar jika Anda punya custom CSS
    "custom_js": "js/custom_login.js",
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "vertical_tabs", "auth.group": "vertical_tabs"},
    # "theme": "superhero",
    # "dark_mode_listener": True,
}

# --- JAZZMIN UI TWEAKS ---
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-danger",
    "accent": "accent-primary",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# --- KONFIGURASI TINYMCE RICH TEXT EDITOR ---
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}
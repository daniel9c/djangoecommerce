# coding=utf-8

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# EMAIL_BACKEND: Opcao para envio de email em desenvolvimento,
# Pega todo o conteudo do email e joga para dentro do teminal.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path, re_path
from . import views

'''Nota: a url pai esta dentro de djangoecommerce/urls.py. La dentro é declarado
    a url path('core/'.) que em seguida chama este arquivo url.
    Tudo que for declarado aqui ja vai ser dentro de core/algumacoisaaqui'''
urlpatterns = [

    path('mensagem/', views.email_send_message, name='email_message'),
]

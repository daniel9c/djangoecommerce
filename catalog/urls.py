# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path, re_path
from . import views

'''Nota: a url pai esta dentro de djangoecommerce/urls.py. La dentro é declarado
    a url path('catalogo/'.) que em seguida chama este arquivo url.
    Tudo que for declarado aqui ja vai ser dentro de catalogo/algumacoisaaqui'''
urlpatterns = [
    path('', views.product_list, name='product_list'),

    # [\w_-]+ = quaisquer caracteres alpha numerico depois da barra
    # ?P<slug> = passando exatamente para a variavel slug na declaracao da view
    re_path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]

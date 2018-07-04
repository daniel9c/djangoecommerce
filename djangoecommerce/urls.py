# -*- coding: utf-8 -*-

"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *

urlpatterns = [
    # Com a propriedade name, podemos manter o nome sempre fixo nas chamadas dentro do html, mesmo que o arquivo relacionado mude.
    path('', index, name='index'),
    path('contato/', contact, name='contact'),    

    # Referenciando o urls.py do app catalog, o namespace ajuda caso tenha urls com o
    #mesmo nome em apps diferentes, ai dentro do html vai usa o namespace na frente da url
    #Ex: <a href="{% url 'catalog:product_list' %}"></a>
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),

    path('core/', include(('core.urls', 'core'), namespace='core')),

    path('admin/', admin.site.urls),
]

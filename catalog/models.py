# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100);

    #Nota: auto_now_add cria a primeira vez a data automaticamente e nao muda mais
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    #representacao string para quando for printado o objeto
    def __str__(self):
        return self.name


    """Retorna a url usando reverse:
    passando o nome da url e os parametros, o reverse vai retornar a url absoluta.
    catalog:category este 'catalog:' na frente da url é o namespace criado dentro de urls.py main
    para referenciar que esta usando uma view dentro do app catalog.
    Ja o category é a url declarada dentro de urls.py na pasta catalog, onde tem o parametro slug declarado
    Com este metodo, o proprio modelo sabe qual é a sua url dentro do site, isso vai habilitar dentro do
    admin uma opcao para clicar na categoria cadastrada e abrir diretamente o site.
    E dentro do html, em vez de chamar a url toda, como: <a href="{% url 'catalog:category' slug=category.slug %}">
    vai simplesmente chamar este metodo, ficando assim: <a href="{{category.get_absolute_url}}"> """
    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})

class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100);
    category = models.ForeignKey('catalog.Category', on_delete='models.PROTECT', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    #representacao string para quando for printado o objeto
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})

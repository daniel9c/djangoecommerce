# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name'] #category__name = filtrando pelo nome da categoria usando o lookup '__' + nome do field
    list_filter = ['created', 'modified', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

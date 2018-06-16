# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import Category, Product

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

#recebendo o paramentro da url ex: http://localhost:8000/produtos/photoshop/. Ver Urls.py
#o 'photoshop' esta sendo passado dentro de slug
def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category':  category,
        'product_list': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/category.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

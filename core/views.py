# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product

def index(request):
    #return HttpResponse('Helo World')

    # texts_arr = ['Item1', 'item2', 'item3']
    # context = {
    #     'var_title': 'django e-commerce daniel',
    #     'var_texts_arr': texts_arr
    # }

    # context = {
    #     'categories_arr': Category.objects.all()
    # }
    #return render(request, 'index.html', context)

    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# def product(request):
#     return render(request, 'product.html')

# def product_list(request):
#     return render(request, 'product_list.html')

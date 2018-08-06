# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Category, Product


# def product_list(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html', context)

#A genericView generic.ListView já faz o trabalho de pegar todos os produtos
#jogar para o template em forma de lista.
class ProductListView(generic.ListView):

        model = Product #pode ser tambem: queryset = Product.objects.all()
        template_name = 'catalog/product_list.html'
        #Se não for nomeado o nome da variavel que vai receber a lista e
        #passar para o template, ele pega o Nome da classe 'Product' e coloca 'list' no final: product_list.
        #Mas caso eu queira nomear, só usar:
        context_object_name = 'products'

product_list = ProductListView.as_view()

#recebendo o paramentro da url ex: http://localhost:8000/produtos/photoshop/. Ver Urls.py
#o 'photoshop' esta sendo passado dentro de slug
def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category':  category,
        'product_list': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/category.html', context)

#recebendo o paramentro da url ex: http://localhost:8000/produtos/photoshop/. Ver Urls.py
#o 'photoshop' esta sendo passado dentro de slug
class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list' #nome da variavel que a query do get_queryset sera armazenada

    #sobrescrevendo o get_queryset para customizar fazendo ele filtrar por slug.
    def get_queryset(self):
        #Buscando os produtos que estejam associados a uma (cageteria com o slug tal), desta forma nao eh mais necessario fazer as linhas abaixo:
        #category = Category.objects.get(slug=slug)
        #'product_list': Product.objects.filter(category=category)
        return Product.objects.filter(category__slug=self.kwargs['slug'])# category__slug > usando o lookup para pegar o parametro slug da categoria

    #sobrescrevendo o get_context_data para adicionar mais um paramentro no contexto, sendo que context_object_name ja esta preenchido.
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs) #<somente declarando o super.
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug']) #adicionando o novo parametro do contexto.
        return context

category = CategoryListView.as_view()

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

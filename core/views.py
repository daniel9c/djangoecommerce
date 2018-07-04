# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def email_send_message(request):
    return render(request, 'email_send_message.html')

def contact(request):
    success = False

    #(POST or None)Se nao tiver o request post, vai criar o formulario vazio.
    form = ContactForm(request.POST or None)
    #se vei conteudo dentro do post e os campos estao validos
    if form.is_valid():
        #chamando o metodo send_mail_contact_form criado dentro da classe forms.py em ContactForm
        form.send_mail_contact_form()
        success = True

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #Chamando a view email_message de dentro do urls.py do app core
        return HttpResponseRedirect(reverse('core:email_message'))


    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

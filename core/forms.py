# -*- coding: utf-8 -*-

from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget = forms.Textarea())

    #Trata os dados do formulario e envia o email
    def send_mail_contact_form(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        #Criando uma variavel que recebe um texto formatado
        message = 'Nome: {0}\nE-mail: {1}\nMensagem: {2}'.format(name,email,message)

        #Usando a funcao send_mail do django. passando os paramentros:
        #titulo, mensagem, email de envio, e email de destino
        send_mail(
            'Email de contato do site',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['daniel9c@gmail.com']
        )

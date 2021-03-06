# FORMULÁRIO PADRÃO DO DJANGO E ALTERAÇÕES DIVERSAS

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

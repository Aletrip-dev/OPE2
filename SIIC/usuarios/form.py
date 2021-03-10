# FORMULÁRIO PADRÃO DO DJANGO E ALTERAÇÕES DIVERSAS

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    # campo para personalização do formulário padrão
    nome_completo = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'password1']
        
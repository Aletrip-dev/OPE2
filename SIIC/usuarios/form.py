# FORMULÁRIO PADRÃO DO DJANGO E ALTERAÇÕES DIVERSAS

# from SIIC.usuarios.models import Perfil
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class UsuarioForm(UserCreationForm):
    # campo para personalização do formulário padrão
    # nome_completo = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']

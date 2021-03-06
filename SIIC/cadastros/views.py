from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Usuario, Pedido
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

# Create your views here.

# CONTROLE DE LOGIN
from django.contrib.auth.mixins import LoginRequiredMixin


# ##################################### CREATE #################################


class UsuarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['nome_usuario', 'funcao_usuario',
              'nivel_usuario', 'senha_usuario']
    template_name = 'cadastros/form_user.html'
    success_url = reverse_lazy('inicio')


class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['valor_pedido', 'usuario_pedido']
    template_name = 'cadastros/form_pedidos.html'
    success_url = reverse_lazy('listar-pedidos')


# ##################################### UPDATE #################################


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['nome_usuario', 'funcao_usuario',
              'nivel_usuario', 'senha_usuario']
    template_name = 'cadastros/form_user.html'
    success_url = reverse_lazy('inicio')


class PedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['valor_pedido', 'usuario_pedido']
    template_name = 'cadastros/form_pedido.html'
    success_url = reverse_lazy('listar-pedidos')


# ##################################### DELETE #################################


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')


class PedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pedidos')


# #########################LISTAR OBJETOS DE UM BANCO ##########################


class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/usuarios.html'


class PedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

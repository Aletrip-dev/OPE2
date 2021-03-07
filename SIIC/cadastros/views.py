from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


# lista de usuarios django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from .models import Usuario, Pedido

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
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Cadastro de pedidos"
        context["subtitulo"] = "Cadastro de pedidos para compra de produdos"
        context["botao"] = "Cadastrar"

        return context


# ##################################### UPDATE #################################


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    fields = ['username', 'email',]
    template_name = 'cadastros/form_user.html'
    success_url = reverse_lazy('inicio')


class PedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['valor_pedido', 'usuario_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar pedidos"
        context["subtitulo"] = "Editar pedidos cadastrados no SIIC"
        context["botao"] = "Editar"

        return context


# ##################################### DELETE #################################


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = User
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
    model = User
    template_name = 'cadastros/listas/usuarios.html'


class PedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

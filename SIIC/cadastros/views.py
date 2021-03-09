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
from .models import Pedido

# Create your views here.
# CONTROLE DE LOGIN
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# ##################################### CREATE #################################


class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['valor_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    # metodo para registrar o usuário que realiza o pedido
    def form_valid(self, form):
        # referencia o usuário da clásse no models
        form.instance.usuario_pedido = self.request.user
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado

        # self.object.valor += "[qualquercoisa]"
        # self.object.save()

        return url

    # efetua a substituição no HTML dos termos constantes nos argumentos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Cadastro de pedidos"
        context["subtitulo"] = "Cadastro de pedidos para compra de produdos"
        context["botao"] = "Cadastrar"

        return context


# ##################################### UPDATE #################################


class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = User
    fields = ['username', 'email', ]
    template_name = 'cadastros/form_user.html'
    success_url = reverse_lazy('inicio')


class PedidoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
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

    login_url = reverse_lazy(GroupRequiredMixin, LoginRequiredMixin, 'login')
    group_required = u"Adm"
    model = User
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')


class PedidoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pedidos')


# #########################LISTAR OBJETOS DE UM BANCO ##########################


class UsuarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = User
    template_name = 'cadastros/listas/usuarios.html'


class PedidoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Ger"]
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

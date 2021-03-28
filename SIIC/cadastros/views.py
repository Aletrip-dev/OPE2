from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from usuarios.models import Usuario

# Create your views here.

# lista de usuarios django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import Pedido

# Controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# ##################################### CREATE #################################


class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['data_fechamento', 'nota_fiscal', 'pedido_ususario', 'status_pedido', 'tipo_movimentacao', 'frete', 'valor_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    # Metodo para registrar o usuário que realiza o pedido
    def form_valid(self, form):
        # referencia o usuário da clásse no models
        form.instance.usuario_pedido = self.request.user
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado
        # Adicionar um texto ao campo
        # self.object.valor += "[qualquercoisa]"
        # self.object.save()
        return url

    # Efetua a substituição no HTML dos termos constantes nos argumentos
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
    model = Usuario
    fields = ['username', 'email', 'nome_completo', 'cpf', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = 'Atualizar dados do usuário'
        context["botao"] = 'atualizar'
        return context

class PedidoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['valor_pedido']
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
    model = Usuario
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
    model = Usuario
    template_name = 'cadastros/listas/usuarios.html'


class PedidoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

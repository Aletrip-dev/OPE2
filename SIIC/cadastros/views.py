from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Usuario, Pedido
# Create your views here.

# ##################################### CREATE #################################


class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome_usuario', 'funcao_usuario',
              'nivel_usuario', 'senha_usuario']
    template_name = 'cadastros/form_user.html'
    success_url = reverse_lazy('inicio')


class PedidoCreate(CreateView):
    model = Pedido
    fields = ['valor_pedido', 'usuario_pedido']
    template_name = 'cadastros/form_pedidos.html'
    success_url = reverse_lazy('listar-pedidos')


# ##################################### UPDATE #################################


class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['nome_usuario', 'funcao_usuario',
              'nivel_usuario', 'senha_usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


class PedidoUpdate(UpdateView):
    model = Pedido
    fields = ['valor_pedido', 'usuario_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')


# ##################################### DELETE #################################


class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')


class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pedidos')


# #########################LISTAR OBJETOS DE UM BANCO ##########################


class UsuarioList(ListView):
    model = Usuario
    template_name = 'cadastros/listas/usuarios.html'


class PedidoList(ListView):
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

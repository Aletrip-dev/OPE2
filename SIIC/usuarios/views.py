from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.urls import reverse_lazy
from .models import Perfil
from django.shortcuts import get_object_or_404

# Create your views here.

# criar usuários no django


class UsuarioCreate(CreateView):
    template_name = "cadastros/form_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # cria o usuario no grupo correspondente
        grupo = get_object_or_404(Group, name="Padrão")
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado
        self.object.groups.add(grupo)
        self.object.save()

        # criando perfil
        Perfil.objects.create(usuario=self.object)
        return url

    # método que pode ser utilizado em formulários padrão para passar o título
    # personalizado
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registro de novo usuário'
        return context


class PerfilUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = Perfil
    fields = ['nome_completo', 'funcao', 'data_registro', 'data_exclusao']
    success_url = reverse_lazy('inicio')

    # metodo para pegart o usuário sem ser pelo pk na url
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = 'Dados pessoais'
        context["botao"] = 'atualizar'

        return context

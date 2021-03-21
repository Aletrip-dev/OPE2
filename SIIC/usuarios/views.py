from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin
# from .models import Perfil

# Create your views here.


class UsuarioCreate(CreateView):
    # group_required = u"Adm"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # cria o usuario no grupo correspondente
        # grupo = get_object_or_404(Group, name="Padrão")
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado
        # self.object.groups.add(grupo)
        self.object.save()

        # criando perfil
        # Perfil.objects.create(usuario=self.object)
        return url

    # método que pode ser utilizado em formulários padrão para passar o título
    # personalizado
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registro de novo usuário'
        return context


# class PerfilUpdate(UpdateView):
#     template_name = 'cadastros/form.html'
#     model = Perfil
#     fields = ['nome_completo', 'primeiro_nome', 'sobrenome', 'funcao']
#     success_url = reverse_lazy('inicio')

#     # metodo para selecionar o usuário sem ser pelo pk na url
#     def get_object(self, queryset=None):
#         self.object = get_object_or_404(Perfil, usuario=self.request.user)
#         return self.object

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context["titulo"] = 'Dados pessoais'
#         context["botao"] = 'atualizar'

#         return context

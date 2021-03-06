from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .form import UsuarioForm
from django.urls import reverse_lazy

# Create your views here.

# criar usuários no django


class UsuarioCreate(CreateView):
    template_name = "cadastros/form_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')

# método que pode ser utilizado em formulários padrão para passar o título
# personalizado
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Registro de novo usuário'
        return context

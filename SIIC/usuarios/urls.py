from django.urls import path
# MÓDUDO PARA AUTENTICAÇÃO DE USUÁRIOS
# (passar um alias para não conflitar com a views da aplicação)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form_login.html'
    ), name='login'),
    # path('logout/', auth_views.logout.as_view(), name='logout'),
]

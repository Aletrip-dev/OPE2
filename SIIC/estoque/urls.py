from django.db import models
from django.urls.conf import path
from .views import estoque_entrada_list, estoque_itens_detalhes


urlpatterns = [
    path('estoque/listar_entradas', estoque_entrada_list,
         name='estoque_entrada_list'),
    path('item_detalhe/<int:pk>/', estoque_itens_detalhes, name='detalhar-itens'),
]

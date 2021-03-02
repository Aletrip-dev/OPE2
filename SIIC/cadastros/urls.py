from django.urls import path
from .views import UsuarioCreate, PedidoCreate
from .views import UsuarioUpdate, PedidoUpdate
from .views import UsuarioDelete, PedidoDelete


# from .views import IndexView


urlpatterns = [
    path('cadastrar/usuario', UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('cadastrar/pedido', PedidoCreate.as_view(), name='cadastrar-pedido'),

    # UPDATE -- OBTEM O ID ATRAVÉS DA URL

    path('editar/usuario/<int:pk>/',
         UsuarioUpdate.as_view(), name='editar-usuario'),
    path('editar/pedido/<int:pk>/', PedidoUpdate.as_view(),  name='editar-pedido'),

    # DELETE -- OBTEM O ID ATRAVÉS DA URL

    path('excluir/usuario/<int:pk>/',
         UsuarioDelete.as_view(), name='excluir-usuario'),
    path('excluir/pedido/<int:pk>/',
         PedidoDelete.as_view(),  name='excluir-pedido'),
]

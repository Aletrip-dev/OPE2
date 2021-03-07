from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# classe que define os atributos dos campos
# conforme o atributo da classe também valida os campos
# cada classe representa uma tabela na base de dados


class Pedido(models.Model):
    valor_pedido = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name="Valor do pedido"
    )
    data_pedido = models.DateField(auto_now=True)
    # chave estrangeira protegida quando há dependências
    usuario_pedido = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Usuário responsável"
    )

    # metodo para pegar o valor do campo para imprimir
    def __str__(self):
        return "User: {}, Dt: {} --> Total: R$ {}".format(
            self.usuario_pedido, self.data_pedido, self.valor_pedido
        )

# conforme diagrama de classes

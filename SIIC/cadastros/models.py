from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Usuario


# Create your models here.
# classe que define os atributos dos campos
# conforme o atributo da classe também valida os campos
# cada classe representa uma tabela na base de dados


class StatusPedido(models.Model):
    status_pedido = models.CharField(
        max_length=50, verbose_name='Status do pedidos')


class TipoMovimentacao(models.Model):
    tipo_movimentacao = models.CharField(
        max_length=50, verbose_name="Tipo de movimentação")


class CorProduto(models.Model):
    cor_produto = models.CharField(
        max_length=50, verbose_name='Cor do produto')


class TamanhoProduto(models.Model):
    tamanho_produto = models.CharField(
        max_length=50, verbose_name='Tamanho do produto')


class Pedido(models.Model):
    valor_pedido = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name="Valor do pedido"
    )
    data_pedido = models.DateField(
        auto_now=True, verbose_name='Data da abertura')
    data_fechamento = models.DateField(verbose_name='Data do fechamento')
    frete = models.DecimalField(
        decimal_places=2, max_digits=2, verbose_name='Valor do frete')
    nota_fiscal = models.IntegerField(verbose_name='Numero da nota fiscal')
    pedido_ususario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    status_pedido = models.ForeignKey(
        StatusPedido, on_delete=models.PROTECT, verbose_name='Status')
    tipo_movimentacao = models.ForeignKey(
        TipoMovimentacao, on_delete=models.PROTECT, verbose_name='Movimentação')



    # chave estrangeira protegida quando há dependências
    # usuario_pedido = models.ForeignKey(
    #      Usuario, on_delete=models.PROTECT)

    # metodo para pegar o valor do campo e imprimir na tela
    def __str__(self):
        return "Usuário: {}".format(
            self.pedido_usuario
        )

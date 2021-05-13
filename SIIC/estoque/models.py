from django.db.models.expressions import Value
from usuarios.models import Usuario
from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Produto
from django.urls.base import reverse_lazy
from django import forms
from .manager import EstoqueEntradaManager, EstoqueSaidaManager
from django.db.models import F, ExpressionWrapper, DecimalField, Max, Sum, Avg, Min
from decimal import Decimal
from django.db.models import Sum
# Create your models here.

# classe para obter data e hora da criação e modificação

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now=False, auto_now_add=True)

    modified = models.DateTimeField(
        'modificado em', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(
        Usuario, verbose_name="Usuário", on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Nota Fiscal')
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{}.{}.{}'.format(self.pk, self.nf, self.created.strftime('%d%m%Y'))
        return '{}.0000.{}'.format(self.pk, self.created.strftime('%d%m%Y'))

    def nota_formatada(self):
        if self.nf:
            return str(self.nf).zfill(6)
        return '---'


# cria tabela virtual somente com as entradas


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


# cria tabela virtual somente com as saidas


class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saida'
        verbose_name_plural = 'estoque saida'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, verbose_name='Produto: ')
    quantidade = models.PositiveIntegerField(verbose_name='Qtd.: ')
    saldo = models.PositiveIntegerField(verbose_name='Estoque: ')
    preco_unit = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True, verbose_name='R$/Unid.')
    valor_item = models.DecimalField(
        max_digits=9, decimal_places=2, default=0)
    valor_item_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)

    # realiza o calcula do valor do item e atribui ao campo
    def calcula_total(self, *args, **kwargs):
        self.total = round(self.preco_unit * self.quantidade, 2)
        self.valor_item = self.total
        return super(EstoqueItens, self).save(*args, **kwargs)

    # def calcula_total_geral_item(self, *args, **kwargs):
    #     self.soma = 0
    #     for item in self.valor_item:
    #         self.soma = self.valor_item
    #         self.valor_item_total += self.soma
    #     return super(EstoqueItens, self).save(*args, **kwargs)


def total_geral_item(*args, **kwargs):
    total_geral = EstoqueItens.objects.values('valor_item').aggregate(Sum('valor_item'))
    valor_item_total = total_geral.values()
    return print(valor_item_total)
    # self.total_geral = EstoqueItens.objects.annotate(valor_item_total=Sum('valor_item'))
    # # self.total = EstoqueItens.objects.aggregate(Sum('valor_item')).values
    # self.valor_item_total = self.total_geral[0].
    # return print(super(EstoqueItens, self).save(*args, **kwargs))

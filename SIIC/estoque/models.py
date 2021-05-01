from usuarios.models import Usuario
from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Produto
# Create your models here.

# classe para obter data e hora da criação e modificação

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida')
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
        Usuario, verbose_name="Usuário", on_delete=models.CASCADE)
    nf = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Nota Fiscal')
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk)


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)

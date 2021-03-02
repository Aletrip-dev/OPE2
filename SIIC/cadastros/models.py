from django.db import models

# Create your models here.

# classe que define os atributos dos campos
# conforme o atributo da classe também valida os campos
# cada classe representa uma tabela na base de dados


class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descricão")

    # metodo para pegar o valor do campo para imprimir
    def __str__(self):
        return "{}, ({})".format(self.nome, self.descricao)


class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descricão")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)
    # chave estrangeira protegida quando há dependências
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    # metodo para pegar o valor do campo para imprimir
    def __str__(self):
        return "{} - {}, ({})".format(self.numero, self.descricao, self.campo)

# inclusão de classes especificas para as tabelas relacionais
# conforme diagrama de classes

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfil(models.Model):
    nome_completo = models.CharField(
        max_length=255, null=True, verbose_name='Nome completo'
    )
    funcao = models.CharField(max_length=50, verbose_name='Função')
    data_registro = models.DateField(null=True)
    data_exclusao = models.DateField(null=True, blank=True)
    # relação um pra um com o usuário do sistema
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

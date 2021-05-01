from django.contrib import admin
from .models import EstoqueItens, Estoque

# Register your models here.


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'funcionario', 'nf', 'movimento',)
    search_fields = ('nf',)
    date_hierarchy = 'created'


@admin.register(EstoqueItens)
class EstoqueItensAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'estoque', 'produto', 'quantidade', 'saldo',)
    search_fields = ('produto',)

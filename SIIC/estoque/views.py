from django.shortcuts import render
from .models import Estoque, EstoqueItens


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)


def estoque_itens_detalhes(request, pk):
    obj = Estoque.objects.get(pk=pk)
    template_name = 'estoque_entrada_detalhes.html'
    context = {'object': obj}
    return render(request, template_name, context)

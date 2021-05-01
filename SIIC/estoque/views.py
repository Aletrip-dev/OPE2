from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Estoque, EstoqueForm, EstoqueIntensForm, EstoqueItens


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)


def estoque_entrada_detalhes(request, pk):
    obj = Estoque.objects.get(pk=pk)
    template_name = 'estoque_entrada_detalhes.html'
    context = {'object': obj}
    return render(request, template_name, context)


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueIntensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            url = 'detalhar-itens'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)

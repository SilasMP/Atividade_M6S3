from django.shortcuts import render
from base.forms import ContatoForm
from base.models import Contato

def inicio(request):
    return render(request, 'index.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'sucesso': sucesso,
        'form': form,
    }
    
    return render(request, 'contato.html', contexto)
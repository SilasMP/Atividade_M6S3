from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm
from base.models import Contato, Reserva

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

def reserva(request):
    sucesso = False
    form_reserva = ReservaForm(request.POST or None)
    if form_reserva.is_valid():
        form_reserva.save()
        sucesso = True
    contexto = {
        'sucesso': sucesso,
        'form': form_reserva
    }  

    return render(request, 'reserva.html', contexto)
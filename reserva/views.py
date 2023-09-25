from django.shortcuts import render
from reserva.forms import ReservaForm
from reserva.models import Reserva

def criar_reserva(request):
    sucesso = False
    form_reserva = ReservaForm(request.POST or None)
    
    if form_reserva.is_valid():
        form_reserva.save()
        sucesso = True
    contexto = {
        'sucesso': sucesso,
        'form': form_reserva,
        'reserva': Reserva(),
    }  

    return render(request, 'reserva.html', contexto)

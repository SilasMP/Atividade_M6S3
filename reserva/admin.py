from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data', 'turno']
    search_fields = ['nome', 'nome_pet']
    list_filter = ['data', 'turno']

    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banhos'
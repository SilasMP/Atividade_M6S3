from django.db import models

class Reserva(models.Model):

    TAMANHO_OPCOES = {
        (0, 'Pequeno'),
        (1, 'Médio'),
        (2, 'Grande'),
    }

    TURNO_OPCOES = {
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    }

    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    nome_pet = models.CharField('Nome do Pet', max_length=80)
    data = models.DateField('Data', help_text='dd/mm/aaaa')
    turno = models.CharField('Turno', max_length=10, choices= TURNO_OPCOES)
    tamanho = models.IntegerField('Tamanho', choices= TAMANHO_OPCOES)
    observacoes = models.TextField('Observações', max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
    
    class Meta:
        verbose_name = 'Reserva Banho'
        verbose_name_plural = 'Reservas de Banho'
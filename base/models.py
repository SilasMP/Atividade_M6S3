from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

class Reserva(models.Model):
    nome_pet = models.CharField('Nome do Pet', max_length=80)
    telefone = models.CharField('Telefone', max_length=15)
    dia_reserva = models.DateField('Escolha um dia')
    observacoes = models.TextField('Observações', max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
from django import forms
from base.models import Contato, Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder':'Informe o Nome Completo'
                }
                ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Informe o E-mail'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder':'Escreva sua mensagem'
                }
            ),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']

        widgets = {
            'nome_pet': forms.TextInput(
                attrs={
                    'placeholder':'Informe o nome do seu Pet'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder':'Informe um Telefone de contato'
                }
            ),
            'dia_reserva': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'observacoes': forms.Textarea(
                attrs={
                    'placeholder':'Escreva aqui observações relevantes para a reserva'
                }
            ),
        }
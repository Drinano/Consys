from django import forms
from .models import Cliente, ReservaVaga, ReservaSalao, Garagem

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'rg', 'ap']

class ReservaVagaFrom(forms.ModelForm):
    class Meta:
        model = ReservaVaga
        fields = ['id', 'data_inicio', 'data_termino', 'obs', 'status']

class ReservaSalaoFrom(forms.ModelForm):
    class Meta:
        model = ReservaSalao
        fields = ['id', 'data_inicio', 'data_termino', 'obs', 'status']

class GaragemFrom(forms.ModelForm):
    class Meta:
        model = Garagem
        fields = ['id', 'vaga', 'status']

class StatusFrom(forms.ModelForm):
    class Meta:
        model = ReservaVaga
        fields = ['status']

class StatusSalaoFrom(forms.ModelForm):
    class Meta:
        model = ReservaSalao
        fields = ['status']

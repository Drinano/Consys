from django.contrib import admin
from .models import Cliente, ReservaVaga, ReservaSalao, Garagem

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'status', 'cpf', 'telefone', 'email']

@admin.register(ReservaVaga)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data_inicio', 'data_termino', 'tipo', 'obs']

@admin.register(ReservaSalao)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'data_inicio', 'data_termino', 'tipo', 'obs']

@admin.register(Garagem)
class GaragemAdmin(admin.ModelAdmin):
    list_display = ['id', 'vaga']



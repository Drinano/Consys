from django.contrib import admin
from .models import Cliente, Reserva


# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_cliente', 'status', 'cpf_cliente', 'telefone_cliente', 'email_cliente']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'cliente', 'modificacado_em', 'status', 'data_inicio','data_termino']
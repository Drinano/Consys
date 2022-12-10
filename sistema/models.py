from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User # Importa tabela de usuários do Django

# Create your models here.
class Cliente(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    nome_cliente = models.CharField(max_length=200)
    cpf_cliente = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone_cliente = models.CharField(max_length=20)
    email_cliente = models.EmailField()
    rg_cliente = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        if self.cpf_cliente:
            return self.nome_cliente + ' - ' + self.cpf_cliente


class Reserva(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    TIPO_CHOICES = (('Reserva', 'Reserva'), ('Saída', 'Saída'))
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    usuario =  CurrentUserField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Ativo')
    def __str__(self):
        inicio, fim = str(self.data_inicio), str(self.data_termino)
        return self.cliente.nome_cliente + ' | ' + inicio + '/' + fim

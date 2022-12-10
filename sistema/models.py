from django.db import models
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Cliente(models.Model):
    STATUS_CHOICES = (('Ativo', 'Ativo'), ('Inativo', 'Inativo'))
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    rg = models.CharField(max_length=50)
    ap = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

class Garagem(models.Model):
    STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível'),
    )

    NUM_VAGA = (
        ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'),
        ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'),
        ('115', '115'), ('116', '116'), ('117', '117'), ('119', '119'), ('120', '120'), ('201', '201'), ('202', '202'),
        ('203', '203'), ('204', '204'), ('205', '205'), ('206', '206'), ('207', '207'), ('208', '208'), ('209', '209'),
        ('210', '210'), ('211', '211'), ('212', '212'), ('213', '213'), ('214', '214'), ('215', '215'), ('216', '216'),
        ('217', '217'), ('218', '218'), ('219', '219'), ('220', '220'), ('301', '301'), ('302', '302'), ('303', '303'),
        ('304', '304'), ('305', '305'), ('306', '306'), ('307', '307'), ('308', '308'), ('309', '309'), ('310', '310'),
        ('311', '311'), ('312', '312'), ('313', '313'), ('314', '314'), ('315', '315'), ('316', '316'), ('317', '317'),
        ('318', '318'), ('319', '319'), ('320', '320'), ('401', '401'), ('402', '402'), ('403', '403'), ('404', '404'),
        ('405', '405'), ('406', '406'), ('407', '407'), ('408', '408'), ('409', '409'), ('410', '410'), ('411', '411'),
        ('412', '412'), ('413', '413'), ('414', '414'), ('415', '415'), ('416', '416'), ('417', '417'), ('418', '418'),
        ('419', '419'), ('420', '420'),
    )

    vaga = models.CharField(choices=NUM_VAGA, max_length=50)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Disponível')

class ReservaVaga(models.Model):
    STATUS_CHOICES = (('Aprovado', 'Aprovado'), ('Aguardando Aprovação', 'Aguardando Aprovação'))

    vaga = models.CharField(max_length=50)
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    obs = models.CharField(max_length=100)
    tipo = models.CharField(max_length=12, default='Garagem')
    usuario = CurrentUserField()
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Aguardando Aprovação')

class ReservaSalao(models.Model):
    STATUS_CHOICES = (('Aprovado', 'Aprovado'), ('Aguardando Aprovação', 'Aguardando Aprovação'))
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    obs = models.CharField(max_length=100)
    tipo = models.CharField(max_length=12, default='Salão de Festas')
    vaga = models.CharField(max_length=10, default='SN')
    usuario = CurrentUserField()
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Aguardando Aprovação')

class Permissoes(models.Model):
    ...

    class Meta:
        permissions = (
            ('reservar_vaga', 'Pode reservar vagas'),
            ('reservar_salao', 'Pode reservar salao'),
        )

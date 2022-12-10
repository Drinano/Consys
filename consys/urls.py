from django.contrib import admin
from django.urls import path
from sistema import views
from sistema.views import cadastrar, cadsReserva, delete_cliente, update_cliente, exibir_cliente, mostrar_cliente, \
    perfil, reservar_salao, sem_permissao, cadsReservaSalao, exibir_vaga, delete_reserva, \
    update_reserva, update_reserva_salao, delete_reserva_salao, exibir_salao, cadastrar_usuario, list_garagem, \
    new_cliente, list_cliente, list_reserva, aprovar

urlpatterns = [

    # ADMIN, LOGIN, LOGOUT
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

    #PÁGINA INICIAL
    path('', views.index, name='index'),

    # CADASTRO USUÁRIOS, ALTERAÇÃO SENHA, DADOS DO USUÁIO
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('perfil/', perfil, name='perfil'),


    # CADASTRO DE CLIENTE, VISUALIZAR CLIENTE
    path('newcliente', new_cliente, name='newcliente'),
    path('cadastrar', cadastrar),
    path('listarclientes/', list_cliente, name='listcliente'),


    # CRUD CLIENTE
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
    path('exibir/<int:id>/', exibir_cliente, name='exibir_cliente'),
    path('mostrar/<int:id>/', mostrar_cliente, name='mostrar_cliente'),

    # RESERVAS, APROVAÇÃO DE RESERVAS
    path('reservar_vaga', list_garagem, name='reservar_vaga'),
    path('cadsReserva', cadsReserva, name='cadsReserva'),
    path('reservar_salao', reservar_salao, name='reservar_salao'),
    path('cadsReservaSalao', cadsReservaSalao, name='cadsReservaSalao'),
    path('aprovar/', aprovar, name='aprovar'),
    path('listar_reservas/', list_reserva, name='listreserva'),

    # CRUD VAGA
    path('exibirVaga/<int:id>/', exibir_vaga, name='exibir_vaga'),
    path('vagaDelete/<int:id>/', delete_reserva, name='vaga_delete'),
    path('vagaUpdate/<int:id>/', update_reserva, name='vaga_update'),

    #CRUD SALÃO
    path('exibirSalao/<int:id>/', exibir_salao, name='exibir_salao'),
    path('salaoDelete/<int:id>/', delete_reserva_salao, name='salao_delete'),
    path('salaoUpdate/<int:id>/', update_reserva_salao, name='salao_update'),

    #USUÁRIO SEM PERMISSÃO
    path('sem_permissao', sem_permissao, name='sem_permissao'),
]

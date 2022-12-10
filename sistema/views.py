from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from .models import Cliente, ReservaVaga, ReservaSalao , Garagem
from .forms import ClienteForm, ReservaVagaFrom, StatusFrom, StatusSalaoFrom, ReservaSalaoFrom

#Login / Acesso Sistema
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e Senha invalido, favor tentar novamente.')
    return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')

# Principal
@login_required(login_url='/login/')
def index(request):
    garagemI = Garagem.objects.all()
    return render(request,'index.html', {'garagemI': garagemI})

# Cadastro Usuário no Django
@permission_required('administradores')
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro_usuario.html', {'form_usuario': form_usuario})

# Mostra informações do usuário (perfil)
@login_required
def perfil(request):
    dados = User.objects.get(id=request.user.id)
    return render(request, 'perfil.html', {'form': dados})

#Alterar Senha
@login_required(login_url='/login/')
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})

# Exibe a tela de cadastro de novo cliente
@permission_required('administradores')
@login_required(login_url='/login/')
def new_cliente(request):
    return render(request, 'newcliente.html')

# Cadastrar Cliente
@permission_required('administradores')
def cadastrar(request):
    cliente = Cliente()

    cliente.nome = request.POST['nome']
    cliente.email = request.POST['email']
    cliente.telefone = request.POST['telefone']
    cliente.rg = request.POST['rg']
    cliente.cpf = request.POST['cpf']
    cliente.ap = request.POST['ap']
    cliente.save()

    return render(request, 'index.html', {'cliente': cliente})

# Exibe uma lista com todos os  Cliente Cadastrados
@permission_required('administradores')
def list_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'listarclientes.html', {'clientes': clientes})

# Atualiza dados do cliente quando é editado
@permission_required('administradores')
def update_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('/listarclientes/')

    return render(request, 'cliente_update.html', {'form': form, 'cliente': cliente})

#Exibe os dados do cliente na tela de alteração
@permission_required('administradores')
def mostrar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('/listarclientes/')

    return render(request, 'cliente_exibir.html', {'form': form, 'cliente': cliente})

# Detalhamento do cliente quando utiliza o menu exibir
@permission_required('administradores')
def exibir_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('/listarclientes/')

    return render(request, 'cliente_update.html', {'form': form, 'cliente': cliente})

# Apaga o cliente do sistema
@permission_required('administradores')
def delete_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('/listarclientes/')

    return render(request, 'cliente-delete-confirm.html', {'cliente': cliente})

# Exibe a tela de reservar vaga
def reservar_vaga(request):
    return render(request,'reservar_vaga.html')

# Criar as reservas de vaga
def cadsReserva(request):
    reserva = ReservaVaga()
    reserva.data_inicio = request.POST['data_inicio']
    reserva.data_termino = request.POST['data_termino']
    reserva.obs = request.POST['obs']
    reserva.vaga = request.POST['vaga']
    reserva.usuario = User.objects.get(id=request.user.id)

    reserva.save()
    return render(request, 'index.html', {'reserva': reserva})

# Listar garagens cadastradas
def list_garagem(request):
    vagas = Garagem.objects.all()
    return render(request, 'reservar_vaga.html', {'vagas': vagas})

# Altera o status do Banco das reservas de vaga, quando for apagada uma reserva
@permission_required('administradores')
def delete_reserva(request, id):
    reserva = ReservaVaga.objects.get(id=id)

    if reserva.status == 'Aprovado':
        Garagem.objects.filter(vaga=reserva.vaga).update(status='Disponivel')

    if reserva.status == 'Aguardando Aprovação':
        Garagem.objects.filter(vaga=reserva.vaga).update(status='Indisponivel')

    if request.method == 'POST':
        reserva.delete()
        return redirect('/aprovar/')

    return render(request, 'vaga_delete.html', {'reserva': reserva})

# Exibe todas as informações de uma vaga selecionada
@permission_required('administradores')
def exibir_vaga(request, id):
    vaga = ReservaVaga.objects.get(id=id)
    form = ReservaVagaFrom(request.POST or None, instance=vaga)

    if form.is_valid():
        form.save()
        return redirect('/aprovar/')

    return render(request, 'exibir_vaga.html', {'form': form, 'vaga': vaga})

# Altera o status do Banco das reservas de vaga. Para aprovação da vaga com os Status: Disponiveis / Indisponiveis
@permission_required('administradores')
def update_reserva(request, id):

    status = ReservaVaga.objects.get(id=id)

    if status.status == 'Aprovado':
        Garagem.objects.filter(vaga=status.vaga).update(status='Disponivel')

    if status.status == 'Aguardando Aprovação':
        Garagem.objects.filter(vaga=status.vaga).update(status='Indisponivel')

    form = StatusFrom(request.POST or None, instance=status)

    if form.is_valid():
        form.save()

        return redirect('/aprovar/')

    return render(request, 'vaga_update.html', {'form': form, 'status': status})


# Exibe a tela de reservar salão
def reservar_salao(request):
    return render(request,'reservar_salao.html')

# Cria as reservas do Salão
def cadsReservaSalao(request):
    salao = ReservaSalao()
    salao.data_inicio = request.POST['data_inicio']
    salao.data_termino = request.POST['data_termino']
    salao.obs = request.POST['obs']
    salao.usuario = User.objects.get(id=request.user.id)

    salao.save()
    return render(request, 'index.html', {'salao': salao})

# Exibe todas as informações de uma reserva de salão selecionada
@permission_required('administradores')
def exibir_salao(request, id):
    salao = ReservaSalao.objects.get(id=id)
    form = ReservaSalaoFrom(request.POST or None, instance=salao)

    if form.is_valid():
        form.save()
        return redirect('/aprovar/')

    return render(request, 'exibir_salao.html', {'form': form, 'salao': salao})

# Altera o status do Banco das reservas de salao. Para aprovação do salão com os Status: Disponiveis / Indisponiveis
@permission_required('administradores')
def update_reserva_salao(request, id):
    status = ReservaSalao.objects.get(id=id)
    form = StatusSalaoFrom(request.POST or None, instance=status)

    if form.is_valid():
        form.save()
        return redirect('/aprovar/')

    return render(request, 'salao_update.html', {'form': form, 'status': status})

# Apaga uma reserva de Salão do Banco
@permission_required('administradores')
def delete_reserva_salao(request, id):
    reserva = ReservaSalao.objects.get(id=id)

    if request.method == 'POST':
        reserva.delete()
        return redirect('/aprovar/')

    return render(request, 'salao_delete.html', {'reserva': reserva})

# Lista todas as reservas de Salão e Vaga com o Status Aprovado
@permission_required('administradores')
def list_reserva (request):
    reservas = ReservaVaga.objects.all()
    salao = ReservaSalao.objects.all()
    return render(request, 'listar_reserva.html', {'reservas': reservas, 'salao': salao})

# Lista todas as reservas de Salão e Vaga com o Status À aprovar
@permission_required('administradores')
def aprovar(request):
    reservas = ReservaVaga.objects.all()
    salao = ReservaSalao.objects.all()
    return render(request, 'aprovar.html', {'reservas': reservas, 'salao': salao})

# Exibe a tela usuário sem permissão
def sem_permissao(request):
    return render(request,'sem_permissao.html')

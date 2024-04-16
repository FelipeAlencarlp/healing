from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')

            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter mais de 6 digitos')

            return redirect('/usuarios/cadastro')

        # filtra o usuário pelo username
        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, 'O nome de usuário já existe')

            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )

        user.save()

        return redirect('/usuarios/login')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # verifica se o usuário existe no banco
        user = auth.authenticate(request, username=username, password=senha)

        if user is not None:
            # pega o usuário e atrela a requisição
            auth.login(request, user)
            return redirect('/pacientes/home')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')

        return redirect('/usuarios/login')


def logout_view(request):
    auth.logout(request)

    return redirect('/usuarios/login')

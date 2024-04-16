from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico
from django.contrib import messages
from django.contrib.messages import constants

def cadastro_medico(request):
    # verifica se tem um usuário médico
    if is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Você já é um médico')

        return redirect('/medico/abrir_horario')


    if request.method == "GET":
        especialidades = Especialidades.objects.all()

        return render(request, 'cadastro_medico.html', {'especialidades': especialidades})

    elif request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim')
        rg = request.FILES.get('rg')
        foto = request.FILES.get('foto')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            cedula_identidade_medica=cim,
            rg=rg,
            foto=foto,
            especialidade_id=especialidade,
            descricao=descricao,
            valor_consulta=valor_consulta,
            user=request.user
        )

        dados_medico.save()

        messages.add_message(request, constants.SUCCESS, 'Médico cadastrado com sucesso!')

        return redirect('/medico/abrir_horario')

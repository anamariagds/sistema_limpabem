from django.shortcuts import render, HttpResponse, redirect
from .models import Atendente

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def validando_acesso(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        #return HttpResponse(f'{email}, {senha}')
    
        funcionario = Atendente.objects.filter(email=email).filter(senha=senha)

        if len(funcionario) == 0:
            return redirect('/sistema/login/?status=1')
        elif len(funcionario) >0:
            request.session['funcionario'] = funcionario[0].id #variavel global
            return redirect('/atendimento/ver_atendimentos/') #pagina solicitação de serviço

def sair(request):
    request.session.flush()
    return redirect('/sistema/login/')
    

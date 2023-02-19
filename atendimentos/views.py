from django.shortcuts import render, HttpResponse, redirect
from funcionarios.models import Atendente
from .models import Atendimento
from .forms import atendimentoForm


def ver_atendimentos(request):
    if request.session.get('funcionario'):
        funcionario = Atendente.objects.get(id= request.session['funcionario'])
        atendimentos = Atendimento.objects.filter(atendente=funcionario)
        return render(request, "ver_atendimentos.html", {'atendimentos': atendimentos,
                                                         'funcionario': funcionario})
    else:
        return redirect('/sistema/login/?status=2')
    
def novo_atendimento(request):
    form = atendimentoForm(request.POST or None) #instancia do formulario
    if form.is_valid():
        form.save()
        return redirect('/atendimento/ver_atendimentos/') #redirect evita repetir
    
    return render(request, 'novo_atendimento.html', {'form': form})

def atendimento_detalhes(request, id):   
    if request.method == "GET":
        atendimento = Atendimento.objects.get(id=id)
        return render(request, 'atendimento_detalhes.html', {'atendimento': atendimento})
    
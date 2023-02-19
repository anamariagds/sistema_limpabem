from django.forms import ModelForm
from .models import Atendimento

class atendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        fields = [ 'servico', 'data_agendada', 'status', 'nome_cliente', 'fone_cliente', 'atendente', 'helper']

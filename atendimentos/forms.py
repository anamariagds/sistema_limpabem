from django import forms
from .models import Atendimento

class atendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = [ 'servico', 'data_agendada', 'status', 'nome_cliente', 'fone_cliente','bairro', 'rua', 'casa', 'atendente', 'helper']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['atendente'].widget = forms.HiddenInput()
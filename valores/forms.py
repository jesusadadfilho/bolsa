from django.forms import ModelForm, TextInput, DateInput
from .models import *

class EmpresaForm(ModelForm):

    class Meta:
        model = Empresa
        fields = ['nome']

        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': "Nome da empresa"}),
        }

        error_messages = {
            'nome': {
                'max_length': ("This writer's name is too long."),
            },
        }

class AcaoForm(ModelForm):

    class Meta:
        model = Acao
        fields = '__all__'

        widgets = {
            'sigla': TextInput(attrs={'class': 'form-control', 'placeholder': "Sigla"}),
            'dt_inicio': DateInput(attrs={'type': "date"}),


        }

        error_messages = {
            'sigla': {
                'max_length': ("This writer's name is too long."),
            },
        }

class CotacaoForm(ModelForm):

    class Meta:
        model = Cotacao
        fields = '__all__'

        widgets = {
            'dt_valor': DateInput(attrs={'type': "date"}),
            'valor':  TextInput(attrs={'class': 'form-control', 'placeholder': "Valor"}),


        }

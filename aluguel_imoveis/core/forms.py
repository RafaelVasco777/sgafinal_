# core/forms.py
from django import forms
from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'

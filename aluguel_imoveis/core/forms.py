from django import forms
from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': 'XXXXX-XXX'}),
            'estado': forms.TextInput(attrs={'placeholder': 'UF'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        }

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX'}),
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
        }
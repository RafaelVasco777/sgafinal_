from django.contrib import admin

from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento, Corretor, Imobiliaria

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'cidade', 'estado', 'tipo', 'preco')

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'data_inicio', 'data_fim', 'valor')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'data_pagamento', 'valor', 'metodo_pagamento')

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'creci', 'telefone')

@admin.register(Imobiliaria)
class ImobiliariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')
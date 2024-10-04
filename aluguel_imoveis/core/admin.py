from django.contrib import admin
from .models import Proprietario, Cliente, Imovel, Contrato, Pagamento

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'telefone', 'email')
    search_fields = ('nome', 'cpf')
    list_filter = ('data_nascimento',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'telefone', 'email')
    search_fields = ('nome', 'cpf')
    list_filter = ('data_nascimento',)

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'endereco', 'cidade', 'estado', 'cep', 'tipo', 'preco', 'proprietario')
    search_fields = ('endereco', 'cidade', 'estado', 'tipo')
    list_filter = ('estado', 'tipo')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'imovel', 'cliente', 'proprietario', 'data_inicio', 'data_fim', 'valor', 'status')
    search_fields = ('cliente__nome', 'imovel__endereco', 'status')
    list_filter = ('status',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'data_pagamento', 'valor', 'metodo_pagamento', 'data_vencimento')
    search_fields = ('contrato__id', 'metodo_pagamento')
    list_filter = ('data_pagamento',)

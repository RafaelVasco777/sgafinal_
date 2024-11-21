from django.contrib import admin
from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento, Corretor, Imobiliaria

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 1

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
    inlines = [ContratoInline]

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
    fields = ('imovel', 'cliente', 'proprietario', 'data_inicio', 'data_fim', 'tipo', 'valor', 'status')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'data_pagamento', 'valor', 'metodo_pagamento', 'data_vencimento')
    search_fields = ('contrato__id', 'metodo_pagamento')
    list_filter = ('data_pagamento', 'metodo_pagamento')

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'email', 'creci', 'imobiliaria')
    search_fields = ('nome', 'cpf', 'creci')
    list_filter = ('imobiliaria',)

@admin.register(Imobiliaria)
class ImobiliariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'telefone', 'email', 'site')
    search_fields = ('nome', 'cnpj')
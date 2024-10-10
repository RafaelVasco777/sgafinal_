from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14,
        validators=[RegexValidator(regex=r'\d{9}-\d{2}', message=_('Formato do CPF deve ser XXX.XXX.XXX-XX'))],
        unique=True
    )
    data_nascimento = models.DateField()
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'\(\d{2}\) \d{4,5}-\d{4}', message=_('Formato do telefone deve ser (XX) XXXXX-XXXX'))]
    )
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=14,
        validators=[RegexValidator(regex=r'\d{9}-\d{2}', message=_('Formato do CPF deve ser XXX.XXX.XXX-XX'))],
        unique=True
    )
    data_nascimento = models.DateField()
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'\(\d{2}\) \d{4,5}-\d{4}', message=_('Formato do telefone deve ser (XX) XXXXX-XXXX'))]
    )
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=2,
        validators=[RegexValidator(regex=r'[A-Z]{2}', message=_('Formato do estado deve ser UF, ex: SP'))]
    )
    cep = models.CharField(
        max_length=9,
        validators=[RegexValidator(regex=r'\d{5}-\d{3}', message=_('Formato do CEP deve ser XXXXX-XXX'))]
    )
    tipo = models.CharField(max_length=50)
    descricao_detalhada = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='imoveis')
    imagens = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return f'{self.tipo} em {self.endereco}'


class Contrato(models.Model):
    class TipoContrato(models.TextChoices):
        ALUGUEL = 'aluguel', _('Aluguel')
        VENDA = 'venda', _('Venda')

    class StatusContrato(models.TextChoices):
        ATIVO = 'ativo', _('Ativo')
        ENCERRADO = 'encerrado', _('Encerrado')

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='contratos')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo = models.CharField(max_length=50, choices=TipoContrato.choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=20, choices=StatusContrato.choices, default=StatusContrato.ATIVO)

    def __str__(self):
        return f'Contrato de {self.cliente} para {self.imovel}'


class Pagamento(models.Model):
    class MetodoPagamento(models.TextChoices):
        CARTAO = 'cartao', _('Cartão')
        TRANSFERENCIA = 'transferencia', _('Transferência')
        BOLETO = 'boleto', _('Boleto')

    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    metodo_pagamento = models.CharField(max_length=50, choices=MetodoPagamento.choices)
    data_vencimento = models.DateField()

    def __str__(self):
        return f'Pagamento de {self.valor} para {self.contrato}'
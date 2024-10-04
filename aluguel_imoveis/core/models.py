from django.db import models

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  # Formato: XXX.XXX.XXX-XX
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  # Formato: XXX.XXX.XXX-XX
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Ex: SP, RJ
    cep = models.CharField(max_length=10)  # Formato: XXXXX-XXX
    tipo = models.CharField(max_length=50)
    descricao_detalhada = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='imoveis')
    imagens = models.ImageField(upload_to='imagens/', blank=True, null=True)  # Para o upload da imagem

    def __str__(self):
        return f'{self.tipo} em {self.endereco}'


class Contrato(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo = models.CharField(max_length=50)  # Ex: aluguel, venda
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)  # Ex: ativo, encerrado

    def __str__(self):
        return f'Contrato de {self.cliente} para {self.imovel}'


class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50)  # Ex: cartão, transferência
    data_vencimento = models.DateField()

    def __str__(self):
        return f'Pagamento de {self.valor} para {self.contrato}'

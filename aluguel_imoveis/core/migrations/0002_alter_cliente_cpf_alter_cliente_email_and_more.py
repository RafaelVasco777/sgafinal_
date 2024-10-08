# Generated by Django 5.1.1 on 2024-10-08 14:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Formato do telefone deve ser (XX) XXXXX-XXXX', regex='\\(\\d{2}\\) \\d{4,5}-\\d{4}')]),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='core.imovel'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='core.proprietario'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='status',
            field=models.CharField(choices=[('ativo', 'Ativo'), ('encerrado', 'Encerrado')], default='ativo', max_length=20),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='tipo',
            field=models.CharField(choices=[('aluguel', 'Aluguel'), ('venda', 'Venda')], max_length=50),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='cep',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Formato do CEP deve ser XXXXX-XXX', regex='\\d{5}-\\d{3}')]),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='estado',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Formato do estado deve ser UF, ex: SP', regex='[A-Z]{2}')]),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='core.contrato'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='metodo_pagamento',
            field=models.CharField(choices=[('cartao', 'Cartão'), ('transferencia', 'Transferência'), ('boleto', 'Boleto')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}')]),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='telefone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Formato do telefone deve ser (XX) XXXXX-XXXX', regex='\\(\\d{2}\\) \\d{4,5}-\\d{4}')]),
        ),
    ]

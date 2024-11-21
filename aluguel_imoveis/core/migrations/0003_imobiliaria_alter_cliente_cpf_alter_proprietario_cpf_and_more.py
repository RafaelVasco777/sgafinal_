# Generated by Django 5.1.1 on 2024-11-21 13:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cliente_cpf_alter_cliente_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CNPJ deve ser XX.XXX.XXX/XXXX-XX', regex='\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}')])),
                ('telefone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Formato do telefone deve ser (XX) XXXXX-XXXX', regex='\\(\\d{2}\\) \\d{4,5}-\\d{4}')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='\\d{9}-\\d{2}')]),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='\\d{9}-\\d{2}')]),
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='Formato do CPF deve ser XXX.XXX.XXX-XX', regex='\\d{9}-\\d{2}')])),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Formato do telefone deve ser (XX) XXXXX-XXXX', regex='\\(\\d{2}\\) \\d{4,5}-\\d{4}')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('creci', models.CharField(max_length=20, unique=True)),
                ('comissao', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('imoveis_gerenciados', models.ManyToManyField(related_name='corretores', to='core.imovel')),
                ('imobiliaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corretores', to='core.imobiliaria')),
            ],
        ),
        migrations.AddField(
            model_name='proprietario',
            name='imobiliaria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proprietarios', to='core.imobiliaria'),
        ),
    ]
# Generated by Django 5.1.1 on 2024-11-28 13:48

import core.models
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_imobiliaria_alter_cliente_cpf_alter_proprietario_cpf_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='descricao_detalhada',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='imovel',
            old_name='cidade',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='proprietario',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='status',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='comissao',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='creci',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='imobiliaria',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='imoveis_gerenciados',
        ),
        migrations.RemoveField(
            model_name='imobiliaria',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='imobiliaria',
            name='email',
        ),
        migrations.RemoveField(
            model_name='imobiliaria',
            name='site',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='imagens',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='proprietario',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='pagamento',
            name='data_vencimento',
        ),
        migrations.RemoveField(
            model_name='pagamento',
            name='metodo_pagamento',
        ),
        migrations.RemoveField(
            model_name='proprietario',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='proprietario',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='proprietario',
            name='imobiliaria',
        ),
        migrations.AddField(
            model_name='imobiliaria',
            name='endereco',
            field=models.CharField(default='Endereço não informado', max_length=255),
        ),
        migrations.AddField(
            model_name='imovel',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.imovel'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='imobiliaria',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='endereco',
            field=models.CharField(default='Endereço não informado', max_length=255),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contrato'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
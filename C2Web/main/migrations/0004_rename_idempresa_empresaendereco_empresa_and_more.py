# Generated by Django 4.2.2 on 2023-06-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_condicaopagamento_dtexclusao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresaendereco',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='estoque',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='estoquemovimento',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='estoquemovimento',
            old_name='idproduto',
            new_name='produto',
        ),
        migrations.RenameField(
            model_name='ordemservico',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='ordemservico',
            old_name='idpessoa',
            new_name='pessoa',
        ),
        migrations.RenameField(
            model_name='ordemservicoequipamento',
            old_name='idordemservico',
            new_name='ordemservico',
        ),
        migrations.RenameField(
            model_name='ordemservicohistorico',
            old_name='idordemservico',
            new_name='ordemservico',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='pessoadocumento',
            old_name='idpessoa',
            new_name='pessoa',
        ),
        migrations.RenameField(
            model_name='pessoaendereco',
            old_name='idpessoa',
            new_name='pessoa',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='idsecao',
            new_name='secao',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='idunidade',
            new_name='unidade',
        ),
        migrations.RenameField(
            model_name='secao',
            old_name='idempresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='unidade',
            old_name='idempresa',
            new_name='empresa',
        ),
    ]

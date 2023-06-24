# Generated by Django 4.2.2 on 2023-06-23 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsrazaosocial', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('nmfantasia', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('dsinscricaoestadual', models.CharField(max_length=30, verbose_name='Inscrição estadual')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isorcamento', models.BooleanField(default=False, verbose_name='Orçamento')),
                ('isaprovado', models.BooleanField(default=False, verbose_name='Aprovado')),
                ('dtentrada', models.DateField(verbose_name='Data entrada')),
                ('dtpromessa', models.DateField(verbose_name='Prometido para')),
                ('valorlimite', models.FloatField(verbose_name='Fazer até no valor de')),
                ('flsitaucao', models.IntegerField(choices=[(0, 'Aberta'), (1, 'Encerrada'), (2, 'Cancelada')], verbose_name='Situação')),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsnome', models.CharField(max_length=100, verbose_name='Nome')),
                ('dssobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('flsituacao', models.IntegerField(choices=[(0, 'Ativa'), (1, 'Inativa'), (2, 'Bloqueada'), (3, 'Excluída')], verbose_name='Situação cadastral')),
                ('flnatureza', models.IntegerField(choices=[(0, 'Física'), (1, 'Jurídica')], verbose_name='Natureza')),
                ('dtnascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dslicenca', models.CharField(max_length=32, verbose_name='Código da licença')),
                ('dsvalidade', models.CharField(max_length=32, verbose_name='Código da licença')),
                ('dtvalidade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdcodigo', models.CharField(max_length=3, verbose_name='Código')),
                ('dsdescricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fltipodocumento', models.IntegerField(choices=[(0, 'RG'), (1, 'CPF'), (2, 'CNPJ'), (3, 'DNI'), (4, 'Passaporte')], verbose_name='Tipo de documento')),
                ('dsdescricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('cdabreviacao', models.CharField(max_length=10, verbose_name='Descrição')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsdescricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrcodigobarras', models.CharField(max_length=18, verbose_name='Código de barras')),
                ('cdreferencia', models.CharField(max_length=15, verbose_name='Código de referência')),
                ('dsdescricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('vlprecovenda', models.FloatField(verbose_name='Preço de venda')),
                ('vlprecocusto', models.FloatField(verbose_name='Preço de custo')),
                ('vlmargem', models.FloatField(verbose_name='Margem de lucro')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('idsecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.secao')),
                ('idunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.unidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsendereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('dscidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('dsuf', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=2, verbose_name='Estado')),
                ('dstelefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('dscelular', models.CharField(max_length=12, verbose_name='Telefone')),
                ('dscep', models.CharField(max_length=8, verbose_name='Telefone')),
                ('dsbairro', models.CharField(max_length=50, verbose_name='Telefone')),
                ('isprincipal', models.BooleanField(default=False, verbose_name='Endereço principal')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idpessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pessoa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsdocumento', models.CharField(max_length=20, verbose_name='Documento')),
                ('isprincipal', models.BooleanField(default=False, verbose_name='Documento principal')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('fltipodocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipodocumento')),
                ('idpessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pessoa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServicoHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtmovimento', models.DateField()),
                ('flsitaucao', models.IntegerField(choices=[(0, 'Ativa'), (1, 'Inativa'), (2, 'Bloqueada'), (3, 'Excluída')])),
                ('dsobservacao', models.TextField(max_length=1000)),
                ('idordemservico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ordemservico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServicoEquipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsequipamento', models.CharField(max_length=200, verbose_name='Equipamento')),
                ('nrserie', models.CharField(max_length=50, verbose_name='Número de série')),
                ('dsmarca', models.CharField(max_length=50, verbose_name='Marca')),
                ('dsdefeito', models.TextField(max_length=1000, verbose_name='Descrição do defeito')),
                ('idordemservico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ordemservico')),
            ],
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='idpessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pessoa'),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsdescricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EstoqueMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrquantidade', models.FloatField(verbose_name='Quantidade')),
                ('nrsqldo', models.FloatField(verbose_name='Saldo atual')),
                ('flmovimento', models.IntegerField(choices=[(0, 'Saldo inicial'), (1, 'Entrada'), (2, 'Saída')], verbose_name='Condição')),
                ('dtmovimento', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('idproduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrquantidade', models.FloatField(verbose_name='Quantidade')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('idproduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsendereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('dscep', models.CharField(max_length=8, verbose_name='Cep')),
                ('dsbairro', models.CharField(max_length=50, verbose_name='Endereço')),
                ('dscidade', models.CharField(max_length=50, verbose_name='Endereço')),
                ('dsUF', models.CharField(choices=[('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('RR', 'Roraima'), ('PA', 'Pará'), ('AP', 'Amapá'), ('TO', 'Tocantins'), ('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('MG', 'Minas Gerais'), ('ES', 'Espírito Santo'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('GO', 'Goiás'), ('DF', 'Distrito Federal')], max_length=2, verbose_name='Estado')),
                ('dsfone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('idempresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.empresa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fllogprocesso', models.BooleanField(default=False, verbose_name='Habilitar Log')),
                ('flenviamensagemwhatsapp', models.BooleanField(default=False, verbose_name='Habilitar o envio de mensagem pelo WhatsApp')),
                ('dschaveapi', models.CharField(max_length=40, verbose_name='Chave da API')),
                ('flutilizarcnpjchaveapi', models.BooleanField(default=True, verbose_name='Utilizar cnpj como chave da API')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CondicaoPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsdescricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('nrparcelas', models.IntegerField(verbose_name='Número de parcelas')),
                ('nrdiasparcelas', models.IntegerField(verbose_name='Número de dias entre parcelas')),
                ('dtcadastro', models.DateField()),
                ('dtalteracao', models.DateField()),
                ('dtexclusao', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
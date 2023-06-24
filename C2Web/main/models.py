from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SITUACAO_ORDEM_SERVICO_LIST = (
    (0,'Aberta'),
    (1,'Encerrada'),
    (2,'Cancelada'),
)

CONDICAO_LISTA = (
    (0, 'A Vista'),
    (1, 'A Prazo'),
)

TIPO_PRODUTO = (
    (0,'Produto'),
    (1,'Serviço')
)

MOVIMENTO_LISTA = (
    (0,'Saldo inicial'),
    (1,'Entrada'),
    (2,'Saída')
)

TIPO_DOCUMENTO_LIST = (
    (0,'RG'),
    (1,'CPF'),
    (2,'CNPJ'),
    (3,'DNI'),
    (4,'Passaporte'),
)

SITUACAO_LIST = (
    (0,'Ativa'),
    (1,'Inativa'),
    (2,'Bloqueada'),
    (3,'Excluída'),
)

NATUREZA_LIST = (
    (0,'Física'),
    (1,'Jurídica'),
)

UF_LIST = (
    ('RO','Rondônia'),
    ('AC','Acre'),
    ('AM','Amazonas'),
    ('RR','Roraima'),
    ('PA','Pará'),
    ('AP','Amapá'),
    ('TO','Tocantins'),
    ('MA','Maranhão'),
    ('PI','Piauí'),
    ('CE','Ceará'),
    ('RN','Rio Grande do Norte'),
    ('PB','Paraíba'),
    ('PE','Pernambuco'),
    ('AL','Alagoas'),
    ('SE','Sergipe'),
    ('BA','Bahia'),
    ('MG','Minas Gerais'),
    ('ES','Espírito Santo'),
    ('RJ','Rio de Janeiro'),
    ('SP','São Paulo'),
    ('PR','Paraná'),
    ('SC','Santa Catarina'),
    ('RS','Rio Grande do Sul'),
    ('MS','Mato Grosso do Sul'),
    ('MT','Mato Grosso'),
    ('GO','Goiás'),
    ('DF','Distrito Federal'),
)

class CondicaoPagamento(models.Model):    
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=50)
    flcondicao = models.IntegerField(verbose_name='Condição', choices=CONDICAO_LISTA),
    nrparcelas = models.IntegerField(verbose_name='Número de parcelas')
    nrdiasparcelas = models.IntegerField(verbose_name='Número de dias entre parcelas')
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class FormaPagamento(models.Model):
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=100)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Configuracao(models.Model):
    fllogprocesso = models.BooleanField(verbose_name='Habilitar Log', default=False)
    flenviamensagemwhatsapp = models.BooleanField(verbose_name='Habilitar o envio de mensagem pelo WhatsApp', default=False)
    dschaveapi = models.CharField(verbose_name='Chave da API', max_length=40)
    flutilizarcnpjchaveapi = models.BooleanField(verbose_name='Utilizar cnpj como chave da API', default=True)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Empresa(models.Model):
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nmfantasia,
            'cnpj': self.cnpj,
            # Adicione outros campos relevantes da Empresa aqui
    }
    dsrazaosocial = models.CharField(verbose_name='Razão Social', max_length=100)
    nmfantasia = models.CharField(verbose_name='Nome Fantasia', max_length=100)
    cnpj = models.CharField(verbose_name='CNPJ', max_length=14)
    dsinscricaoestadual = models.CharField(verbose_name='Inscrição estadual', max_length=30)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EmpresaEndereco(models.Model):
    dsendereco = models.CharField(verbose_name='Endereço', max_length=100)
    dscep = models.CharField(verbose_name='Cep', max_length=8)
    dsbairro = models.CharField(verbose_name='Endereço', max_length=50)
    dscidade = models.CharField(verbose_name='Endereço', max_length=50)
    dsUF = models.CharField(verbose_name='Estado', max_length=2, choices=UF_LIST)
    dsfone = models.CharField(verbose_name='Telefone', max_length=12)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Unidade(models.Model):
    cdcodigo = models.CharField(verbose_name='Código', max_length=3)
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=50)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Secao(models.Model):
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=100)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Produto(models.Model):
    nrcodigobarras = models.CharField(verbose_name='Código de barras', max_length=18)
    cdreferencia = models.CharField(verbose_name='Código de referência', max_length=15)
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=100)
    vlprecovenda = models.FloatField(verbose_name='Preço de venda')
    vlprecocusto = models.FloatField(verbose_name='Preço de custo')
    vlmargem = models.FloatField(verbose_name='Margem de lucro')
    fltipo  = models.IntegerField(verbose_name='Tipo', choices=TIPO_PRODUTO)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Estoque(models.Model):
    nrquantidade = models.FloatField(verbose_name='Quantidade')    
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    idproduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EstoqueMovimento(models.Model):    
    nrquantidade = models.FloatField(verbose_name='Quantidade')
    nrsqldo = models.FloatField(verbose_name='Saldo atual')
    flmovimento = models.IntegerField(verbose_name='Condição', choices=MOVIMENTO_LISTA)
    dtmovimento = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TipoDocumento(models.Model):    
    fltipodocumento = models.IntegerField(verbose_name='Tipo de documento', choices=TIPO_DOCUMENTO_LIST)
    dsdescricao = models.CharField(verbose_name='Descrição', max_length=50)
    cdabreviacao = models.CharField(verbose_name='Descrição', max_length=10)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Registro(models.Model):
    dslicenca = models.CharField(verbose_name='Código da licença', max_length=32)
    dsvalidade = models.CharField(verbose_name='Código da licença', max_length=32)
    dtvalidade = models.DateField()

class Pessoa(models.Model):
    dsnome = models.CharField(verbose_name='Nome', max_length=100)
    dssobrenome = models.CharField(verbose_name='Sobrenome', max_length=100)
    email = models.EmailField(verbose_name='E-mail', max_length=100)
    flsituacao = models.IntegerField(verbose_name='Situação cadastral', choices=SITUACAO_LIST)
    flnatureza = models.IntegerField(verbose_name='Natureza', choices=NATUREZA_LIST)
    dtnascimento = models.DateField(verbose_name='Data de Nascimento')
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PessoaDocumento(models.Model):
    dsdocumento = models.CharField(verbose_name='Documento', max_length=20)
    isprincipal = models.BooleanField(verbose_name='Documento principal', default=False)
    fltipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PessoaEndereco(models.Model):
    dsendereco = models.CharField(verbose_name='Endereço', max_length=100)
    dscidade = models.CharField(verbose_name='Cidade', max_length=100)
    dsuf = models.CharField(verbose_name='Estado', max_length=2, choices=UF_LIST)
    dstelefone = models.CharField(verbose_name='Telefone', max_length=12)
    dscelular = models.CharField(verbose_name='Telefone', max_length=12)
    dscep = models.CharField(verbose_name='Telefone', max_length=8)
    dsbairro = models.CharField(verbose_name='Telefone', max_length=50)
    isprincipal = models.BooleanField(verbose_name='Endereço principal', default=False)
    dtcadastro = models.DateField()
    dtalteracao = models.DateField()
    dtexclusao = models.DateField(null=True, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrdemServico(models.Model):    
    isorcamento = models.BooleanField(verbose_name='Orçamento', default=False)
    isaprovado = models.BooleanField(verbose_name='Aprovado', default=False)
    dtentrada = models.DateField(verbose_name='Data entrada')
    dtpromessa = models.DateField(verbose_name='Prometido para')
    valorlimite = models.FloatField(verbose_name='Fazer até no valor de')
    flsitaucao = models.IntegerField(verbose_name='Situação', choices=SITUACAO_ORDEM_SERVICO_LIST)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrdemServicoEquipamento(models.Model):
    dsequipamento = models.CharField(verbose_name='Equipamento', max_length=200)
    nrserie = models.CharField(verbose_name='Número de série', max_length=50)
    dsmarca = models.CharField(verbose_name='Marca', max_length=50)
    dsdefeito = models.TextField(verbose_name='Descrição do defeito', max_length=1000)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    

class OrdemServicoHistorico(models.Model):
    dtmovimento = models.DateField()
    flsitaucao = models.IntegerField(choices=SITUACAO_LIST)
    dsobservacao = models.TextField(max_length=1000)
    ordemservico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

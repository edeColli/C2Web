from django import forms
from datetime import date
from main.models import Empresa
from main.models import Produto
from main.models import Pessoa
from main.models import Secao

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['dsrazaosocial', 'nmfantasia', 'cnpj', 'dsinscricaoestadual']
        labels = {
            'dsrazaosocial': 'Razão Social', 
            'nmfantasia': 'Nome Fantasia', 
            'cnpj': 'CNPJ', 
            'dsinscricaoestadual': 'Inscrição Estadual'
        }
        
class SecaoForm(forms.ModelForm):
    # empresa_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Secao
        fields = ['dsdescricao']
        labels = {'dsdescricao': 'Descrição'}

class ProdutoForm(forms.ModelForm):
    nrcodigobarras = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o código de barras'}))
    cdreferencia = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o código de referência'}))
    dsdescrição = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite a descrição'}))
    vlprecovenda = forms.FloatField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o valor de venda'}))
    vlprecocusto = forms.FloatField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o preço de custo'}))
    vlmargem = forms.FloatField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite a margem de lucro'}))

    class Meta:
        model = Produto
        fields = ['nrcodigobarras', 'fltipo', 'cdreferencia', 'dsdescricao', 'secao', 'unidade', 'vlprecocusto', 'vlprecovenda', 'vlmargem']
        labels = {
            'nrcodigobarras': 'Código de barras', 
            'fltipo': 'Tipo', 
            'cdreferencia': 'Código de referência', 
            'dsdescricao': 'Descrição', 
            'secao': 'Seção', 
            'unidade': 'Unidade', 
            'vlprecocusto': 'Valor do Custo', 
            'vlprecovenda': 'Preço de Venda', 
            'vlmargem': 'Margem de lucro'
        }

class PessoaForm(forms.ModelForm):
    dsnome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o nome'}))
    dssobrenome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o sobrenome'}))    
    dtnascimento = forms.FloatField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Informe a data de nascimento'}))

    class Meta:
        model = Pessoa
        fields = ['dsnome', 'dssobrenome', 'flnatureza', 'dtnascimento', 'flsituacao']
        labels = {
            'dsnome': 'Nome',
            'dssobrenome': 'Sobrenome',
            'flnatureza': 'Natureza',
            'flsituacao': 'Situação',
            'dtnascimento': 'Data de nascimento',
        }
        widgets = {
            'dtnascimento': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'placeholder':'dd/mm/yyyy','style': 'width: 15%'}),
        }
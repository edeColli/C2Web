from django import forms
from datetime import date
from main.models import Empresa
from main.models import Produto
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
    empresa_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Secao
        fields = ['dsdescricao']
        labels = {'dsdescricao': 'Descrição'}

class ProdutoForm(forms.ModelForm):
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
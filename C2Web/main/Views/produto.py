from datetime import date
from django.shortcuts import render
from main.forms import ProdutoForm

def produto(request):
    sucesso = False

    if request.method == 'GET':
      form = ProdutoForm()
    else:
      print(request)
      form = ProdutoForm(request.POST)
      if form.is_valid():
        produto = form.save(commit=False)
        produto.dtcadastro = date.today()
        produto.dtalteracao = date.today()
        produto.user = request.user                
        empresa_sessao = request.session.get('empresa_sessao')
        produto.empresa_id = empresa_sessao['id']
        produto.save()
        sucesso = True

    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'produto.html', context)
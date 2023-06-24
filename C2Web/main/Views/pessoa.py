from datetime import date
from django.shortcuts import render
from main.forms import PessoaForm
from django.contrib.auth.decorators import login_required

@login_required
def pessoa(request):
    sucesso = False

    if request.method == 'GET':
      form = PessoaForm()
    else:      
      form = PessoaForm(request.POST)
      if form.is_valid():
        pessoa = form.save(commit=False)
        pessoa.dtcadastro = date.today()
        pessoa.dtalteracao = date.today()
        pessoa.user = request.user                
        empresa_sessao = request.session.get('empresa_sessao')
        pessoa.empresa_id = empresa_sessao['id']
        pessoa.save()
        sucesso = True

    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'pessoa.html', context)
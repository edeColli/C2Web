from datetime import date
from django.shortcuts import render
from main.forms import SecaoForm

def secao(request):
    sucesso = False

    if request.method == 'GET':
      form = SecaoForm()
    else:
      form = SecaoForm(request.POST)
      print(form)
      if form.is_valid():
        secao = form.save(commit=False)
        secao.dtcadastro = date.today()
        secao.dtalteracao = date.today()
        secao.user = request.user                
        empresa_sessao = request.session.get('empresa_sessao')
        secao.empresa_id = empresa_sessao['id']
        secao.save()
        sucesso = True
        
    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'secao.html', context)
from datetime import date
from django.shortcuts import render
from main.forms import EmpresaForm
from django.contrib.auth.decorators import login_required

@login_required
def empresa(request):
    sucesso = False

    if request.method == 'GET':
      form = EmpresaForm()
    else:
      print(request)
      form = EmpresaForm(request.POST)
      if form.is_valid():
        empresa = form.save(commit=False)
        empresa.dtcadastro = date.today()
        empresa.dtalteracao = date.today()
        empresa.user = request.user
        empresa.save()
        sucesso = True

    context = {
        'formulario': form,
        'sucesso': sucesso
    }

    return render(request, 'empresa.html', context)
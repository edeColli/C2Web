from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.sessions.backends.db import SessionStore
from main.models import Empresa
from django.core.serializers import serialize
import json

def getSessionEmpresa(request):  
  empresa = Empresa.objects.get(id=1)
  return empresa.to_dict()

def logar(request):
  LOGIN ='login.html'

  if (request.method == 'GET'):
    return render(request, LOGIN, {
      'form': AuthenticationForm
    })
  else:
    user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
    if user is None:
      return render(request, 'login.html', {
          'form': AuthenticationForm,
          'error': 'Usuário ou senha inválido'
      })
    else:
      login(request, user)
      empresa_sessao = getSessionEmpresa(request)      
      session = SessionStore()
      session['empresa_sessao'] = empresa_sessao
      session.save()
      print('=====SESSAO=====')
      for key, value in request.session.items():
        print('{} => {}'.format(key, value))
      print('=====SESSAO=====')
      
      return redirect('/')
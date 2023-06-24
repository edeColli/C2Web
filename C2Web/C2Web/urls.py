"""
URL configuration for C2Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from main.Views.empresa import empresa
from main.Views.secao import secao
from main.Views.produto import produto
from main.Views.login import logar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.inicio, name='inicio'),
    path("about/", views.sobre, name='sobre'),
    path("logar/", logar, name='login'),
    path("sair/", views.sair),
    path("empresa/", empresa, name='empresa'),
    path("secao/", secao, name='secao'),
    path("produto/", produto, name='produto'),
]

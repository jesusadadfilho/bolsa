"""bolsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from valores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('empresas/', views.mostrar_empresas, name='mostrar_empresas'),
    path('empresas/novo', views.nova_empresa, name='nova_empresa'),
    path('acoes/', views.mostrar_acoes, name='mostrar_acoes'),
    path('acoes/novo', views.nova_acao, name='nova_acao'),
    path('cotacao/', views.mostrar_cotacoes, name='mostrar_cotacoes'),
    path('cotacao/novo', views.nova_cotacao, name='nova_cotacao'),
]

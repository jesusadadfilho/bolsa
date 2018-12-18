from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mostrar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'Empresas.html',
                  {'empresas': empresas})

def nova_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_empresas')
    else:
        form = EmpresaForm()
        return render(request, 'nova_empresa.html',
                      {'form': form})

def mostrar_acoes(request):
    acoes = Acao.objects.all()
    return render(request, 'Acoes.html',
                  {'acoes': acoes})

def nova_acao(request):
    if request.method == "POST":
        form = AcaoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_acoes')
    else:
        form = AcaoForm()
        return render(request, 'nova_acao.html',
                      {'form': form})

def mostrar_cotacoes(request):
    cotacoes = Cotacao.objects.all()

    return render(request, 'Cotacao.html',
                  {'cotacoes': cotacoes})

def nova_cotacao(request):
    if request.method == "POST":
        form = CotacaoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mostrar_cotacoes')
    else:
        form = CotacaoForm()
        return render(request, 'nova_cotacao.html',
                      {'form': form})
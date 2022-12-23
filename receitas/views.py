from django.shortcuts import render
from django.http import HttpResponse
from .models import Receita

def index(request):
    receitas = Receita.objects.all() 
    return render(request, 'index.html', {'receitas':receitas})

def receita(request,receita_id):
    receita = Receita.objects.get(pk=receita_id)
    return render(request, 'receita.html', {'receita':receita})
from django.shortcuts import render, redirect,get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    paginator = Paginator(receitas,6)
    page = request.GET.get('page')
    receiatas_por_paginas = paginator.get_page(page)
    return render(request, 'receitas/index.html', {'receitas':receiatas_por_paginas})

def receita(request,receita_id):
    receita = Receita.objects.get(pk=receita_id)
    return render(request, 'receitas/receita.html', {'receita':receita})

def criaReceita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/criarReceita.html')

def deletaReceita(request,receita_id):
    receita = Receita.objects.get(pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editarReceita(request,receita_id):
    receita = Receita.objects.get(pk=receita_id)
    return render(request, 'receitas/editarReceita.html', {'receita':receita})

def atualizaReceita(request, receita_id):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
    return redirect('dashboard')
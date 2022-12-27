from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('<int:receita_id>', receita, name="receita"),
    path('busca/', busca, name="buscarReceita"),
    path('criar/receita', criaReceita, name="criaReceita"),
    path('deleta/<int:receita_id>', deletaReceita , name="deletaReceita"),
    path('editar/<int:receita_id>', editarReceita , name="editarReceita"),
    path('atualiza/<int:receita_id>', atualizaReceita , name="atualizaReceita"),
]

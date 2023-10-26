from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="alunos"),
   path('cadastrar_aluno/', views.create, name="cadastrar_aluno"),
    path('<int:aluno_id>/', views.visualizar_aluno, name='visualizar_aluno'),
    path('remover/<int:aluno_id>/', views.remover_aluno, name='remover_aluno'),
   
]


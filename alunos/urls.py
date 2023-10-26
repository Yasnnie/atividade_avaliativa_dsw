from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="alunos"),
   path('cadastrar_aluno/', views.create, name="cadastrar_aluno")
]


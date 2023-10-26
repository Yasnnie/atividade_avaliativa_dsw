
from django.shortcuts import render,redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})


def create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm()
    
    return render(request, 'cadastro.html', {'form': form})


def visualizar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    return render(request, 'detalhes.html', {'aluno': aluno})

def remover_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    aluno.delete()
    return redirect('alunos')

def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno) 
        if form.is_valid():
            form.save()
            return redirect('alunos') 
    else:
        form = AlunoForm(instance=aluno)  
    return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})
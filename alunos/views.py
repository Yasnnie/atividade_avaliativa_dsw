
from django.shortcuts import render,redirect
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
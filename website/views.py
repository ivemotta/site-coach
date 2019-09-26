from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = Coach()
        data.nome = request.POST['nome']
        data.frase = request.POST['frase']
        data.inspirador = request.POST['inspirador']
        data.save()
        args = {
            "sucesso": "parabéns seu otario"
        }
        return render(request, 'index.html', args)
    return render(request, 'index.html', ) 

def listar_coaches(request):
    listar_coaches = Coach.objects.filter(ativo=True).all()
    args = {
        'listar_coaches': listar_coaches
    }
    return render(request, 'listar_coaches.html', args)

def delete_coach(request, id):
    item = Coach.objects.get(id=id)
    if item is not None:
        item.ativo = False
        item.save() 
        return redirect('/coaches/listar')
    return render (request, 'listar_coaches.html', {'msg': 'eh xau pra quem eh coach'})
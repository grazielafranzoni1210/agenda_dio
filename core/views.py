from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

def index(request):
    return redirect('/agenda/') # quando acessar a raiz vai redirecionar para a url agenda


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

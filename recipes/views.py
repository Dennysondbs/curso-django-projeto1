from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'recipes/home.html')

def Sobre(request):
    return HttpResponse('Sobre')

def Contatos(request):
    return HttpResponse('Contatos')
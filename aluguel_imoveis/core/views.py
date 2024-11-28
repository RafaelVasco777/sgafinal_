from django.shortcuts import render

def index(request):
    return render(request, 'core/templates/core/index.html')

def sobre_nos(request):
    return render(request, 'core/templates/core/sobre_nos.html')

def locais_disponiveis(request):
    return render(request, 'core/templates/core/locais_disponiveis.html')

def corretores(request):
    return render(request, 'core/templates/core/corretores.html')

def contato(request):
    return render(request, 'core/templates/core/contato.html')
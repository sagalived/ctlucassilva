# ct_core/views.py

from django.shortcuts import render
from .models import MediaGaleria

def home_view(request):
    # Pega os 3 itens mais recentes da galeria
    ultimas_imagens = MediaGaleria.objects.all().order_by('-data_upload')[:3] 
    return render(request, 'ct_core/home.html', {'ultimas_imagens': ultimas_imagens})

# NOVA VIEW: Sobre Nós
def about_view(request):
    return render(request, 'ct_core/about.html') # Vai usar o template about.html

# View de Aulas/Planos (nome da view mantido, URL e template atualizados)
def aulas_view(request):
    return render(request, 'ct_core/planos.html') # Vai usar o template planos.html

def galeria_view(request):
    # Pega todos os itens da galeria
    imagens = MediaGaleria.objects.all() 
    return render(request, 'ct_core/galeria.html', {'imagens': imagens})

# NOVA VIEW: Localização
def location_view(request):
    return render(request, 'ct_core/localizacao.html') # Vai usar o template localizacao.html

def contato_view(request):
    return render(request, 'ct_core/contato.html')
# ct_core/urls.py

from django.urls import path
from . import views

# Define o namespace do aplicativo para uso na tag {% url 'ct_core:home' %}
app_name = 'ct_core'

urlpatterns = [
    path('', views.home_view, name='home'),
    # Nome rota: Sobre Nós
    path('sobre/', views.about_view, name='sobre'), 
    # Nome da rota: 'aulas' para 'planos'
    path('planos/', views.aulas_view, name='planos'), 
    path('galeria/', views.galeria_view, name='galeria'), 
    # Nome rota: Localização
    path('localizacao/', views.location_view, name='localizacao'), 
    path('contato/', views.contato_view, name='contato'), 
]
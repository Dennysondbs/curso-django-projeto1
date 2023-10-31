from django.urls import path
from recipes.views import Home, Sobre, Contatos

urlpatterns = [
    path('', Home), # Home
    path('sobre/', Sobre), # /Sobre/
    path('contatos/', Contatos), # /Contatos/
]
from django.urls import path
from .views import * 

urlpatterns = [
    path ('agrega_curso/<nombre>/<camada>', curso),
    path ('lista_cursos/', lista_curso),
    path ('inicio/', inicio),
    path ('cursos/', cursos),
    path ('estudiantes/', estudiantes),
    path ('profesores/', profesores),
    path ('entregables/', entregables),

]

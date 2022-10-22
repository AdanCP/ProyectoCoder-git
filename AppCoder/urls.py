from django.urls import path
from .views import * 

urlpatterns = [
    path ('agrega_curso/<nombre>/<camada>', curso),
    path ('lista_cursos/', lista_curso),
    path ('', inicio),
    path ('cursos/', cursos, name ='cursos'),
    path ('estudiantes/', estudiantes, name = 'estudiantes'),
    path ('profesores/', profesores, name = 'profesores'),
    path ('entregables/', entregables, name= 'entregables'),

]

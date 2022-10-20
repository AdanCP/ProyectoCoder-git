from django.urls import path
from .views import curso, lista_curso

urlpatterns = [
    path ('agrega_curso/<nombre>/<camada>', curso),
    path ('lista_cursos/', lista_curso)  
]

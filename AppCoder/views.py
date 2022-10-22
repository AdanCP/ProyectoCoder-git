from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

def curso (request, nombre, camada):

    curso = Curso (nombre=nombre, camada = camada)
    curso.save()
    return HttpResponse (f"""
        <p> Curso {curso.nombre} - Camada: {curso.camada} agregado!<p>
    """)

def lista_curso (request):
    lista = Curso.objects.all ()
    return render (request, "lista_cursos.html",{"lista_cursos": lista}) 

def inicio (request):
    return render (request, "inicio.html")
    
def cursos (request):
    return render (request, "cursos.html")
    
def estudiantes (request):
    return render (request, "estudiantes.html")
    
def profesores (request):
    return render (request, "profesores.html")
    
def entregables (request):
    return render (request, "entregables.html")
    
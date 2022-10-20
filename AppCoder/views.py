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
    return HttpResponse ("Vista inicio")

def cursos (request):
    return HttpResponse ("Vista cursos")

def estudiantes (request):
    return HttpResponse ("Vista estudiantes")

def profesores (request):
    return HttpResponse ("Vista profesores")

def entregables (request):
    return HttpResponse ("Vista entregables")

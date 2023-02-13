from django.shortcuts import render
from django import http

from .models import Tarea
# Create your views here.
def home(request):
    #recuperamos la informacion de la base de datos
    tareas = Tarea.objects.all()
    #renderizamos la informacion en el template y la variable tareas
    return render(request, 'home.html', {'tareas': tareas})
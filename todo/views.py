from django.shortcuts import render, redirect
from django import http
from .forms import TareaForm
from . models import Tarea
# Create your views here.
def home(request):
    #recuperamos la informacion de la base de datos
    tareas = Tarea.objects.all()
    #renderizamos la informacion en el template y la variable tareas
    return render(request, 'home.html', {'tareas': tareas})


def agregar(request):
    if request.method == 'POST':
        
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
        
        context = { 'form': form }
        
        return render(request, 'agregar.html', context)
    
    
def eliminar(request,id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('home')


def editar (request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    context = {'form':form}
    return render(request, 'editar.html', context)
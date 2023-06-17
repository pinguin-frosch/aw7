from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from tareas.forms import TareaFormulario
from tareas.models import Tarea


def tareas(request: HttpRequest):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tareas.html', {
        'tareas': tareas
    })

def agregar(request: HttpRequest):
    if request.method == 'POST':
        formulario = TareaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tareas:tareas'))
        else:
            return render(request, 'tareas/agregar.html', {
                'formulario': formulario,
                'accion': 'Agregar'
            })
    return render(request, 'tareas/agregar.html', {
        'formulario': TareaFormulario(),
        'accion': 'Agregar'
    })

def actualizar(request: HttpRequest, id):
    try:
        tarea = Tarea.objects.get(pk=id)
        formulario = TareaFormulario(instance=tarea)
    except ObjectDoesNotExist:
        return redirect(reverse('tareas:tareas'))
    if request.method == 'POST':
        formulario = TareaFormulario(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tareas:tareas'))
        else:
            return render(request, 'tareas/agregar.html', {
                'formulario': formulario,
                'accion': 'Actualizar'
            })
    return render(request, 'tareas/agregar.html', {
        'formulario': formulario,
        'accion': 'Actualizar'
    })

def eliminar(_, id):
    try:
        tarea = Tarea.objects.get(pk=id)
    except ObjectDoesNotExist:
        return redirect(reverse('tareas:tareas'))
    tarea.delete()
    return redirect(reverse('tareas:tareas'))

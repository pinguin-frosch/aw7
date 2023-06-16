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
                'formulario': formulario
            })

    return render(request, 'tareas/agregar.html', {
        'formulario': TareaFormulario()
    })

from django import forms
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

TAREAS = []

def tareas(request: HttpRequest):
    return render(request, 'tareas/tareas.html', {
        'tareas': TAREAS
    })

class TareaFormulario(forms.Form):
    tarea = forms.CharField(label='Tarea', max_length=50)

def agregar(request: HttpRequest):
    if request.method == 'POST':
        formulario = TareaFormulario(request.POST)
        if formulario.is_valid():
            TAREAS.append(formulario.cleaned_data['tarea'])
            return redirect(reverse('tareas:tareas'))
        else:
            return render(request, 'tareas/agregar.html', {
                'formulario': formulario
            })

    return render(request, 'tareas/agregar.html', {
        'formulario': TareaFormulario()
    })

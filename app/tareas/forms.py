from django import forms
from tareas.models import Tarea


class TareaFormulario(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

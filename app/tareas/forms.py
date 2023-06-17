from django import forms
from tareas.models import Tarea


class TareaFormulario(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'
        widgets = {
            'prioridad': forms.NumberInput(attrs={'class': 'form-control'}),
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
        }

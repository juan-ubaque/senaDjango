from django import forms
from .models import Tarea

class tareaForm (forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo', 'descripcion', 'prioridad', 'fecha', 'estado', 'usuario')
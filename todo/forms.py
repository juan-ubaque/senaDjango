from django import forms
from . models import Tarea

class TareaForm (forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    class Meta: 
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado']
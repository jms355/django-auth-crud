from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ['titulo', 'descripcion', 'importante']
        #esto es a lo ultimo para dar css al formulario de crear tareas
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el titulo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingrese la descripcion'}),
            'datecompleted': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

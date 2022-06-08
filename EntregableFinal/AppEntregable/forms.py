from django import forms
from AppEntregable.models import *
#Formulario de usuario
class Libro_form(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }
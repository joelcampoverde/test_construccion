from django import forms 
from .models import *

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields=['nombre','apellido','cedula','celular']
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PropiedadForm(forms.ModelForm):
    
    class Meta:
        model=Propiedad
        fields=['cedula','descripcion','direccion']
        widgets={
            'cedula': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }

        
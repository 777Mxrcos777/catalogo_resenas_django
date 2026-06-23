from django import forms
from .models import Resena
from apps.usuarios.models import Usuario

class ResenaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    email = forms.EmailField(required=True, label="Correo electrónico")
    
    class Meta:
        model = Resena
        fields = ['calificacion', 'texto']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña...'}),
        }
        labels = {
            'calificacion': 'Calificación (1-5)',
            'texto': 'Comentario',
        }
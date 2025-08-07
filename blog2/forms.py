from django import forms
from .models import Club
class FormPublicacion(forms.ModelForm):
        class Meta:
                model = Club
                fields = (
                        'nombre',
                        'fecha_fundacion',
                        'descripcion',
                        'escudo_url',
                        'estadio_url',
                        'logro_destacado',
                        'descripcion_estadio'   
                )

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }
        labels = {
            'texto': '',
        }

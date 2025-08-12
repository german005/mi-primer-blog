from django import forms
from .models import Club, Comentario

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
            'descripcion_estadio',
        )
        # widgets útiles (tipos y tamaños)
        widgets = {
            'fecha_fundacion': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Uno o dos párrafos'}),
            'logro_destacado': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Título + breve detalle'}),
            'descripcion_estadio': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Capacidad, ubicación, curiosidades...'}),
            'escudo_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'estadio_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
        labels = {
            'nombre': 'Nombre del club',
            'fecha_fundacion': 'Fecha de fundación',
            'descripcion': 'Descripción breve',
            'escudo_url': 'URL del escudo',
            'estadio_url': 'URL de la imagen del estadio',
            'logro_destacado': 'Logro más importante del club',
            'descripcion_estadio': 'Descripción del estadio',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clase Bootstrap a todos los campos “normales”
        for field in self.visible_fields():
            w = field.field.widget
            if not isinstance(w, (forms.CheckboxInput, forms.RadioSelect,
                                  forms.CheckboxSelectMultiple, forms.FileInput)):
                css = w.attrs.get('class', '')
                w.attrs['class'] = (css + ' form-control').strip()

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...',
                'class': 'form-control'  # ya sale con Bootstrap
            }),
        }
        labels = {'texto': ''}

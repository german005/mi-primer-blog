from django.conf import settings
from django.db import models
from django.utils import timezone


class Club(models.Model):
    
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='clubes',
    )

    
    nombre = models.CharField('Nombre del club', max_length=200)
    fecha_fundacion = models.DateField('Fecha de fundación')
    descripcion = models.TextField('Descripción breve', help_text='Uno o dos párrafos')

    
    escudo_url = models.URLField('URL del escudo')
    estadio_url = models.URLField('URL de la imagen del estadio')

    
    logro_destacado = models.TextField('Logro más importante del club')
    descripcion_estadio = models.TextField('Descripción del estadio')

    
    fecha_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Club'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.nombre


from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    publicacion = models.ForeignKey('Club', on_delete=models.CASCADE, related_name='comentarios')  # o Publicacion si lo llamás así
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.publicacion.nombre}'

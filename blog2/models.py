from django.conf import settings
from django.db import models
from django.utils import timezone


class Club(models.Model):
    # Quién cargó el club (opcional, pero mantiene el control de autoría)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='clubes',
    )

    # Datos básicos
    nombre = models.CharField('Nombre del club', max_length=200)
    fecha_fundacion = models.DateField('Fecha de fundación')
    descripcion = models.TextField('Descripción breve', help_text='Uno o dos párrafos')

    # Imágenes (se guardan como URL externas, así evitas configurar media)
    escudo_url = models.URLField('URL del escudo')
    estadio_url = models.URLField('URL de la imagen del estadio')

    # Texto destacado
    logro_destacado = models.TextField('Logro más importante del club')
    descripcion_estadio = models.TextField('Descripción del estadio')

    # Metadatos
    fecha_creacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Club'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.nombre

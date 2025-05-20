from django.shortcuts import render
from .models import Publicacion

def lista_public(request): 
    pubkucaciones=publicacion.objects.filter
    (fecha_publicacion_lte=timezone.now()).
    order_by('fecha_publicacion')
    return render(request, 'blog/lista_public.html', {'publicaciones':publicaciones})
# Create your views here.

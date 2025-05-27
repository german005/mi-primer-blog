from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def lista_public(request): 

    publicaciones=Publicacion.objects.filter(fecha_publicacion_lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'blog/lista_public.html', {'publicaciones':publicaciones})
# Create your views here.

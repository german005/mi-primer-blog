from django.shortcuts import render
from .models import Publicacion
from django.contrib.auth.models import User
from django.utils import timezone

def lista_public(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now())
    usuarios = User.objects.all()
    usuario_id = request.GET.get('usuario')
    if usuario_id:
        publicaciones = publicaciones.filter(autor__id=usuario_id)
    return render(request, 'blog/lista_public.html', {
        'publicaciones': publicaciones,
        'usuarios': usuarios,
        'usuario_activo': int(usuario_id) if usuario_id else None
    })
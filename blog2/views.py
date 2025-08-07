from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
from .forms import FormPublicacion
from django.utils import timezone

def club_list(request):
    usuarioActivo = request.user
    clubes = Club.objects.filter(autor=usuarioActivo, fecha_creacion__lte=timezone.now()).order_by('-fecha_creacion')
    return render(request, 'blog2/club_list.html', {
        'clubes': clubes,
        'usuarioActivo': usuarioActivo
    })

def nueva_publicacion(request):
    if request.method == "POST":
        form = FormPublicacion(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user  # opcional: si tu modelo tiene campo autor
            publicacion.save()
            return redirect('club_list')  # redirige al listado u otra página
    else:
        form = FormPublicacion()
    return render(request, 'blog2/nueva_publicacion.html', {'form': form})

from django.shortcuts import get_object_or_404

def editar_club(request, pk):
    club = get_object_or_404(Club, pk=pk)

    if request.method == "POST":
        form = FormPublicacion(request.POST, instance=club)
        if form.is_valid():
            club = form.save(commit=False)
            club.autor = request.user
            club.save()
            return redirect('club_list')
    else:
        form = FormPublicacion(instance=club)
    
    return render(request, 'blog2/editar_club.html', {'form': form})

from .models import Comentario
from .forms import ComentarioForm

def detalle_public(request, pk):
    publicacion = get_object_or_404(Club, pk=pk)
    comentarios = publicacion.comentarios.all().order_by('-fecha_creacion')

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_public', pk=publicacion.pk)
    else:
        form = ComentarioForm()

    return render(request, 'blog2/detalle_public.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form': form
    })



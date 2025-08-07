from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, Comentario
from .forms import FormPublicacion, ComentarioForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def club_list(request):
    if request.user.is_authenticated:
        clubes = Club.objects.filter(autor=request.user, fecha_creacion__lte=timezone.now()).order_by('-fecha_creacion')
    else:
        clubes = Club.objects.filter(fecha_creacion__lte=timezone.now()).order_by('-fecha_creacion')
    return render(request, 'blog2/club_list.html', {'clubes': clubes})

@login_required
def nueva_publicacion(request):
    if request.method == "POST":
        form = FormPublicacion(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('club_list')
    else:
        form = FormPublicacion()
    return render(request, 'blog2/nueva_publicacion.html', {'form': form})

@login_required
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

@login_required
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



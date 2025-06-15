from django.shortcuts import render
from .models import Club

def club_list(request):
    clubes = Club.objects.all()
    return render(request, 'blog2/club_list.html', {'clubes': clubes})

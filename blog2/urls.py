from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion2', views.club_list, name='club_list'),
    path('publicacion/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('club/<int:pk>/editar/', views.editar_club, name='editar_club'),
    path('club/<int:pk>/', views.detalle_public, name='detalle_public'),  # <- esta es nueva
]

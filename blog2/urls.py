from django.urls import path
from . import views


urlpatterns = [ 
path('evaluacion2', views.club_list, name='club_list'), 
]
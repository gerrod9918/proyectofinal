from django.urls import path
from . import views

urlpatterns = [
    path('', views.nueva_materia, name='nueva_materia'),
]

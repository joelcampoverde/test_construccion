from django.urls import path
from .views import *
from . import views
urlpatterns = [
   path('',views.home,name='inicio'),
   path('cliente', Cliente.as_view(), name='cliente'),
   path('crear',Crear.as_view(), name='crear'),
   path('editar/<int:pk>',Editar.as_view(), name='editar'),
   path('eliminar/<int:pk>',Eliminar.as_view(), name='eliminar'),
   #propiedad
   path('propiedad', Propiedad.as_view(), name='propiedad'),
   path('crear_p',CrearPropiedad.as_view(), name='crear_p'),
   path('editar_p/<int:pk>',EditarPropiedad.as_view(), name='editar_p'),
   path('eliminar_p/<int:pk>',EliminarPropiedad.as_view(), name='eliminar_p'),
]
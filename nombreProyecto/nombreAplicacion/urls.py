from django.urls import path
from . import views
# primaria ruta para la aplicacion
urlpatterns = [ 
    path('plantilla/', views.plantilla, name='plantilla'),
    path('cotizaciones/', views.cotizaciones, name='cotizaciones'),
    path('producto/', views.producto, name='producto'),
    path('login/', views.login, name='login'),
]        
# 127.0.0.1:8000/plantilla
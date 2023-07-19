
from django.urls import path, include #debemos agregar include para obtener la funcion de incluir la app a la hora de solicitar la clave /publicaciones
from core import views

#app_name = 'core'

urlpatterns = [
    path('index/', views.indexView, name = 'index'),
    #incluye (menciona el nombre_de_la_app.archivo_de_la_app)
    path('publicaciones/', include('publicaciones.urls')),
    path('login/', include('users.urls')),
    
]
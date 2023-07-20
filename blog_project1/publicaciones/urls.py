
from django.urls import path
#importamos la view de la aplicacion
from publicaciones import views


app_name = 'publicaciones'

urlpatterns = [
    path('publicaciones/', views.VerPublicaciones.as_view(), name = 'publicaciones' ),
    path('postear/', views.Postear.as_view(), name = 'postear' ),
    path('editar/<int:pk>', views.EditarPost.as_view(), name = 'editar' ),
    path('eliminar/<int:pk>', views.EliminarPost.as_view(), name = 'eliminar'),
]
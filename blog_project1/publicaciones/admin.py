from django.contrib import admin
##from publicaciones.models import publicaciones
from .models import publicaciones, categoria
# Register your models here.
##admin.site.register(publicaciones)
admin.site.register(publicaciones)
admin.site.register(categoria)
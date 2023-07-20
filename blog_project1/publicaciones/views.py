from typing import Any
#from django.db.models.query import QuerySet
#from django.shortcuts import render
#importamos de la app.archivo el modelo de la tabla para que se renderice 
from .models import publicaciones

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CrearpublicacionForm
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
#view que renderiza publicaciones basada en def
#def publicacionesView(request):
#    ctx = { 'posteos':publicaciones.objects.all().order_by('fecha') }
#      return render(request, 'publicaciones.html', ctx)

#view que renderiza publicaciones basada en clase
class VerPublicaciones (ListView):
    model = publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    
    def get_queryset(self):
        consulta_anterior = super().get_queryset()

        return consulta_anterior.order_by('-fecha') 
    
#class Postear(CreateView): 
 #   model = postear_publicacion no es necesario
  #  template_name = postear.html
from django.urls import reverse
class Postear(LoginRequiredMixin, CreateView):
    model = publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearpublicacionForm
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    def form_valid(self, form):
        f = form.save(commit=False)
        f.creador_id = self.request.user.id #redefinimos form_valid que viene por defecto en el createview
        return super().form_valid(f)         #solicitamos a que form_valid registre la publicacion en conjunto al id del creador

    
#view para editar publicacion 
class EditarPost(LoginRequiredMixin, UpdateView):
    model = publicaciones
    template_name = 'publicaciones/editar.html'
    form_class = CrearpublicacionForm
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
#view para eliminar publicacion 
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = publicaciones
    template_name = 'publicaciones/Eliminar.html'
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')



    



            
        
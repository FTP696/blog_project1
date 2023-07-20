# from django.forms import ModelForm
#from .models import publicaciones


#class CrearpublicacionForm(ModelForm):
#    class Meta:
#        model = publicaciones
#        fields = ['Titulo', 'Post',] 

from django import forms
from .models import publicaciones

class CrearpublicacionForm(forms.ModelForm):
    class Meta:
       model = publicaciones
       fields = ['titulo', 'post', 'categoria',]
       labels = {
            'titulo' : '',
            'post' : '',
            'categoria' : ''
        }
       
       widgets = {
           'titulo' : forms.TextInput(attrs = {'placeholder' : 'Aca va el titulo', 'class' : 'form-control-lg'},),
           'post' : forms.TextInput(attrs = {'placeholder' : 'Aqui lo que quieras publicar', 'class' : 'form-control'},),
           'categoria' : forms.Select(attrs = {'class' : 'form-select', 'placeholder' : 'selecciona una categoria'})
           }

       
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import usuario
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.urls import reverse
# Create your views here.

#creamos una vista basada en clases
class RegistroView(CreateView):
    model = usuario
    template_name = 'usuarios/registro.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('index')
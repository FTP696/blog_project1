from django.contrib.auth.forms import UserCreationForm
from .models import usuario
#clase que crea un formulario de registro

class RegisterForm(UserCreationForm):
    class Meta:
        model = usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio',] 
        labels = {
            'first_name' : 'Escribi tu nombre'
        }

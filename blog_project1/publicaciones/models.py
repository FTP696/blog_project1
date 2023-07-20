from django.db import models
from users.models import usuario

# Create your models here.
#lo habiamos hecho en core al principio pero lo movimos aca para que la app publicaciones contenga la tabla
class categoria(models.Model):
    nombre = models.CharField((""), max_length=255)
    
    def __str__(self):
        return self.nombre

#tabla de categorias    
class publicaciones (models.Model):
    fecha = models.DateField(auto_now_add=True)
    update = models.DateField (auto_now = True) #agregado despues para constar edicion de publicacion
    titulo = models.CharField((""), max_length=255)
    post = models.TextField()
    #categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, related_name = 'posteos') #para que borre categorias nulas
    categoria = models.ForeignKey(categoria, on_delete=models.SET_NULL, related_name = 'posteos', null = True)
    creador = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name = 'posteos_usuario', null = True,)
    def __str__(self):
        return self.titulo
    
#class postear_publicacion(---): # TODO ESTO SE CREA EN REALIDAD EN FORMS.PY
 #   fecha = models.DateField()
  #  titulo = models.CharField((""), max_length=255)
   # es_admin = models.BooleanField(default = False)
   
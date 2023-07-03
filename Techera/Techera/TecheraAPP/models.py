from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=40)
    website = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)


class BlogPost(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    subTitulo = models.CharField(max_length=200,null=True)
    contenido = RichTextField(null=True)
    fecha_creado = models.DateField(max_length=40)
    imagen = models.ImageField(upload_to='postImagenes', null=True, blank=True)
    
    
class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')
    titulo = models.CharField(max_length=200,null=True)
    mensaje = RichTextField(null=True)
    
class About(models.Model):
    imagen = models.ImageField(upload_to='aboutImagenes', null=True, blank=True)
    descripcion = RichTextField(null=True)





# usuario y permite poder modificar y/o borrar: imagen - nombre -
# descripción - un link a una página web - email y contraseña
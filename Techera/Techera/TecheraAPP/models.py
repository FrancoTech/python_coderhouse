from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return  f'{self.nombre}'

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    edad = models.IntegerField()
    def __str__(self):
        return  f'{self.nombre}'

class BlogPost(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=20)
    fecha_creado = models.DateField(max_length=40)

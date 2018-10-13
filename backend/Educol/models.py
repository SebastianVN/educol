from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)

class UsuarioEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    asistencia = models.IntegerField()
from django.db import models
# Create your models here.
class Persona (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    is_inventariable  = models.BooleanField(default=True)
    is_planta = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class nacionalidades(models.Model):
    nombre = models.CharField(max_length=30)
    lugarturistico = models.CharField(max_length=30)

class ciudades(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.CharField(max_length=30)

    

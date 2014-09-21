from django.contrib.auth.models import AbstractUser
from django.db import models

class Client(AbstractUser):
    telefono = models.CharField(max_length=12, help_text="Telefono de contacto", blank=True, null=True)

class Schedule(models.Model):
    cliente = models.ForeignKey(Client, related_name="clients")
    tiempo = models.DateField(blank=True, null=True)






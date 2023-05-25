from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reseña (models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"
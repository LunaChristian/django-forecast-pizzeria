from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class SemanaForecast(models.Model):
    fecha_lunes = models.DateField()
    lunes = models.PositiveIntegerField()
    martes = models.PositiveIntegerField()
    miercoles = models.PositiveIntegerField()
    jueves = models.PositiveIntegerField()
    viernes = models.PositiveIntegerField()
    sabado = models.PositiveIntegerField()
    domingo = models.PositiveIntegerField()
    
    def clean(self):
        if self.fecha_lunes.weekday() != 0:
            raise ValidationError("La fecha debe ser un lunes.")
    
    @property
    def total(self):
        return (
            self.lunes + self.martes + self.miercoles +
            self.jueves + self.viernes + self.sabado + self.domingo
        )
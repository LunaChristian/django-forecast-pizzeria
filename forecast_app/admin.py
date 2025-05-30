from django.contrib import admin
from .models import SemanaForecast

@admin.register(SemanaForecast)
class SemanaForecastAdmin(admin.ModelAdmin):
    list_display = ('fecha_lunes', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo', 'total')

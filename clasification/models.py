from django.db import models

class School(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    codigo_dane = models.CharField(max_length=30, blank=True, null=True)
    sector = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    clasificacion = models.CharField(max_length=10, blank=True, null=True)
    evaluados = models.IntegerField(blank=True, null=True)
    matriculados = models.IntegerField(blank=True, null=True)
    ingles = models.FloatField(blank=True, null=True)
    sociales = models.FloatField(blank=True, null=True)
    matematicas = models.FloatField(blank=True, null=True)
    ciencias = models.FloatField(blank=True, null=True)
    lectura = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nombre

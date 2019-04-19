from django.db import models
from django.utils.text import slugify

class Colegio(models.Model):
    nombreinstitucion = models.CharField(max_length=100, blank=True, null=True)
    codinst = models.CharField(max_length=20, blank=True, null=True)
    nombremunicipio = models.CharField(max_length=100, blank=True, null=True)
    codigomunicipio = models.IntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    calendario = models.CharField(max_length=2, blank=True, null=True)
    naturaleza = models.CharField(max_length=30, blank=True, null=True)
    evaluados = models.IntegerField(blank=True, null=True)
    prommatematica = models.FloatField(blank=True, null=True)
    promsocialesyciudadanas = models.FloatField(blank=True, null=True)
    promingles = models.FloatField(blank=True, null=True)
    promcienciasnaturales = models.FloatField(blank=True, null=True)
    promlecturacritica = models.FloatField(blank=True, null=True)
    jornada = models.CharField(max_length=50, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    puntajeglobal = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombreinstitucion

    def save(self, *args, **kwargs):
        self.puntajeglobal = ((self.prommatematica + self.promsocialesyciudadanas + self.promcienciasnaturales + self.promlecturacritica) * 3 + self.promingles) / 13.0 * 5
        self.puntajeglobal = round(self.puntajeglobal, 2)
        self.slug = slugify(self.nombreinstitucion)
        super(Colegio, self).save(*args, **kwargs)

    class Meta:
        db_table = 'colegio'


class Departamento(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

ASIGNATURAS = (
    ('matematicas', 'Matematicas'),
    ('ciencias', 'Ciencias'),
    ('sociales', 'Sociales y Ciudadanas'),
	('competencias', 'Competencias Ciudadanas'),
	('ingles', 'Ingles'),
	('razonamiento', 'Razonamiento Cuantitativo'),
	('lectura', 'Lectura Critica'),
)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100, choices=ASIGNATURAS)

    def __str__(self):
        return self.get_nombre_display()

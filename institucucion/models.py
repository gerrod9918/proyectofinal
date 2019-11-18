from django.db import models
from django.contrib import admin
from django.utils import timezone


class Profesor(models.Model):
    nombre  =   models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=15)

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"

    def __str__(self):

        return self.nombre

class Materia(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre  =   models.CharField(max_length=30)
    credito = models.IntegerField()

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):

        return self.nombre


class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    seccion      = models.CharField(max_length=3)
    materias   = models.ManyToManyField(Materia, related_name="get_materias", through='Pensum')

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    nombre  =   models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    edad = models.IntegerField()

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):

        return self.nombre


#Relacion de muchos a muchos para crear el pensum de un grado en especifico
class Pensum (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)



class PensumInLine(admin.TabularInline):
    model = Pensum
    extra = 1


class MateriaAdmin(admin.ModelAdmin):
    inlines = (PensumInLine,)


class GradoAdmin (admin.ModelAdmin):
    inlines = (PensumInLine,)

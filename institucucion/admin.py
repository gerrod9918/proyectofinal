from django.contrib import admin
from institucucion.models import Profesor, Materia, MateriaAdmin, Grado, GradoAdmin, Estudiante

admin.site.register(Profesor)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Estudiante)

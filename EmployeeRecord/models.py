from django.db import models

# Create your models here.

#=========Creando un modelo en SQL lite de la tabla empleado==========

class Empleado (models.Model):
    Primer_Nombre = models.CharField(max_length = 30, unique = False)
    Segundo_Nombre = models.CharField(max_length = 30, unique = False)
    Primer_Apellido = models.CharField(max_length = 30, unique = False)
    Segundo_Apellido = models.CharField(max_length = 30, unique = False)


    
    TIPO_DOCUMENTO_ELECCIONES = [
        ('DUI', 'Dui'),
        ('NIT', 'Nit'),
    ]
    
    Tipo_Documento = models.CharField(max_length = 10, choices = TIPO_DOCUMENTO_ELECCIONES, unique = False)
    Documento = models.CharField(max_length = 14, unique = True)
    
    
    AREA_ELECCIONES = [
        ('Finanzas', (
            ('Contador', 'Contador'),
            ('Tesorero', 'Tesorero'),
            ('Activo Fijo', 'Activo Fijo'),
        )
         ),

        ('Legal', (
            ('Gerente Legal', 'Gerente Legal'),
            ('Oficialia Cumplimiento', 'Oficialia Cumplimiento'),
        )
        ),

        ('Administrativa', (
            ('Gerente administrativo', 'Gerente administrativo'),
            ('Unidad de adquisiciones', 'Unidad de aquisiciones'),
        )    
        ),
    ]

    Area = models.CharField(max_length = 30, choices = AREA_ELECCIONES, unique = False)

    ##======Method to debugg class======
    def __str__(self):
        return self.Primer_Nombre

    

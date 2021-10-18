from django.test import TestCase

from EmployeeRecord.models import Empleado
# Create your tests here.

empleado = Empleado.objects.get(id=10)

if empleado.Tipo_Documento == 'DUI':
    print("dui lokita")
#++++Si lo que seleccione en el form fue dui, cambiar longitud maxima (forms)

print(empleado.Primer_Nombre)
print("Puesto " + empleado.Area)
print("Unidad " + str(empleado.AREA_ELECCIONES[0]))

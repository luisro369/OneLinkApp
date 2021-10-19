from django.test import TestCase

from EmployeeRecord.models import Empleado
# Create your tests here.

empleado = Empleado.objects.get(id=10)

if empleado.Tipo_Documento == 'DUI':
    print("dui lokita")

print("Nombre: " + empleado.Primer_Nombre)
    

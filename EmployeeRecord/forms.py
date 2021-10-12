from django import forms

from EmployeeRecord.models import Empleado

#==========Creando formulario para ingreso de empleado======

class EmpleadoForm(forms.ModelForm):
    
    class Meta():
        model = Empleado
        fields = '__all__'



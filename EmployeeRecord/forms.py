from django import forms
from django.core.validators import RegexValidator

from EmployeeRecord.models import Empleado

#==========Creando formulario para ingreso de empleado======

validar_letras = RegexValidator(r'^[a-zA-Z]*$', 'Verificar campos de letras')
validar_numeros = RegexValidator(r'^[0-9]*$', 'Documento solo debe ingresar numeros')

class EmpleadoForm(forms.ModelForm):
    Primer_Nombre = forms.CharField(max_length = 30, required=True,
                                    widget=forms.TextInput(attrs={"placeholder":"Primer nombre"}),
                                    validators=[validar_letras])
    Segundo_Nombre = forms.CharField(max_length = 30, required=False,
                                    widget=forms.TextInput(attrs={"placeholder":"Segundo nombre"}),
                                    validators=[validar_letras])
    Primer_Apellido = forms.CharField(max_length = 30, required=True,
                                    widget=forms.TextInput(attrs={"placeholder":"Primer apellido"}),
                                    validators=[validar_letras])
    Segundo_Apellido = forms.CharField(max_length = 30, required=False,
                                    widget=forms.TextInput(attrs={"placeholder":"Segundo apellido"}),
                                    validators=[validar_letras])
    Documento = forms.CharField(min_length=9,max_length = 14, required=True,
                                validators=[validar_numeros])


        
    class Meta():
        model = Empleado
        fields = ['Primer_Nombre',
                  'Segundo_Nombre',
                  'Primer_Apellido',
                  'Segundo_Apellido',
                  'Tipo_Documento',
                  'Documento',
                  'Area'
                  ]

    '''def clean_Primer_Nombre(self):
        tDoc = self.cleaned_data.get('Tipo_Documento')
        doc = self.cleaned_data.get('Documento')
        if tDoc == 'Dui' and len(doc) != 9:
            raise forms.ValidationError("duiiiii")
        return tDoc'''
        
    
  
       
            



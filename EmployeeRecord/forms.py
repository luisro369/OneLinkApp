from django import forms
from django.core.validators import RegexValidator
from django.contrib import messages

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
  
    Documento = forms.CharField(min_length=9,max_length = 14, required=True, validators=[validar_numeros])


        
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

    
    # Funcion que valida que la cantidad de numeros sea acorde al tipo de documento
    def clean(self):
         
        # extrayendo los datos ingresados del tipo del documento y el numero
        tipoDoc = self.cleaned_data.get('Tipo_Documento')
        Doc = self.cleaned_data.get('Documento')

        try:
            #----Si se selecciona DUI y no es igual a 9 validar
            if tipoDoc == 'DUI' and len(Doc) != 9:
                raise forms.ValidationError("DUI debe incluir solo 9 numeros (" + str(len(Doc)) +" ingresados)")
        
            #----Si se selecciona DUI y no es igual a 14 validar
            if tipoDoc == 'NIT' and len(Doc) != 14:
                raise forms.ValidationError("NIT debe incluir solo 14 numeros (" + str(len(Doc)) + " ingresados)")

        except Exception as e:
            raise forms.ValidationError(e)

            
        # Si no hay errores retornar la misma data
        return self.cleaned_data

        
    
  
       
            



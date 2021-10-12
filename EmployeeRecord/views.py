from django.shortcuts import render

from EmployeeRecord.forms import EmpleadoForm, EditarEmpleado
from EmployeeRecord.models import Empleado
# Create your views here.
def index (request):
    return render(request, 'EmployeeRecord/index.html')


#=====Vista para listar empleados======
def records (request):
    lista_empleados = Empleado.objects.order_by('id')
    dic_empleados = {'empleados':lista_empleados}
    return render(request, 'EmployeeRecord/records.html', context = dic_empleados)


#====Vista que conecta el formulario de empleado====
def EnterNewEmployee (request):
    form = EmpleadoForm()

    if request.method == "POST":
        form = nuevoEmpleadoForm(request.POST)
        #---validando que el formulario sea valido, si lo es
        #---guardar y regresar a index
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise forms.validationError("Ups! algo ha salido mal, verifica los campos")
        
    return render(request, 'EmployeeRecord/insert.html', {'formulario':form})


def EditEmployee (request, Id):
    #---obteniendo id de usuario enviado desde el boton "Editar"----
    empleado = Empleado.objects.get(id=Id)
    #---Con instance llenamos el formulario con los datos (ID)---
    form = EmpleadoForm(instance = empleado)

    #---guardar cambios y regresar a index
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Ups! algo ha salido mal, verifica los campos")
    

    return render(request,'EmployeeRecord/edit.html', {'formulario':form})


def SearchEmployee (request):
    return render(request, 'EmployeeRecord/search.html')

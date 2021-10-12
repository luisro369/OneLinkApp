from django.shortcuts import render

from EmployeeRecord.forms import EmpleadoForm
from EmployeeRecord.models import Empleado
# Create your views here.
def index (request):
    return render(request, 'EmployeeRecord/index.html')


#=====Vista para listar empleados======
def records (request):
    lista_empleados = Empleado.objects.order_by('id')
    dic_empleados = {'empleados':lista_empleados}
    return render(request, 'EmployeeRecord/records.html', context = dic_empleados)



#====Vista que crea nuevo empleado====
def EnterNewEmployee (request):
    form = EmpleadoForm()

    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        #---validando que el formulario sea valido, si lo es
        #---guardar y regresar a index
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise forms.validationError("Ups! algo ha salido mal, verifica los campos")
    return render(request, 'EmployeeRecord/insert.html', {'formulario':form})


#====Vista para editar empleado=======
def EditEmployee (request, Id):
    #---obteniendo id de empleado enviado desde el boton "Editar"----
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


#=====Eliminar empleado===========
def DeleteEmployee (request, Id):
    #---obteniendo id de empleado enviado desde el boton "Eliminar"---
    empleado = Empleado.objects.get(id=Id)

    #---eliminar usuario y regresar a index
    if request.method == 'POST':
        empleado.delete()
        return index(request)
    
    return render(request, 'EmployeeRecord/delete.html', {'empleado':empleado})



#========vista para buscar empleado=========
def SearchEmployee (request):
    return render(request, 'EmployeeRecord/search.html')

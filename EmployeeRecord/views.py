from django.shortcuts import render

from EmployeeRecord.forms import nuevoEmpleadoForm
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
    form = nuevoEmpleadoForm()

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


def EditEmployee (request):
    return render(request, 'EmployeeRecord/edit.html')


def SearchEmployee (request):
    return render(request, 'EmployeeRecord/search.html')

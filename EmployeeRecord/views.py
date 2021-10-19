from django.shortcuts import render
from django.db.models import Q
from django import forms
from django.contrib import messages

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
            try:
                form.save(commit=True)
                messages.success(request, 'Usuario ingresado Correctamente!')
                return index(request)
            except Exception as e:
                messages.error(request,e)
                return index(request)
        
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
            try:
                form.save(commit=True)
                messages.success(request, 'Usuario modificado Correctamente!')
                return index(request)
            except Exception as e:
                messages.error(request,e)
                return index(request)
            
    return render(request,'EmployeeRecord/edit.html', {'formulario':form})


#=====Eliminar empleado===========
def DeleteEmployee (request, Id):
    #---obteniendo id de empleado enviado desde el boton "Eliminar"---
    empleado = Empleado.objects.get(id=Id)

    #---eliminar usuario y regresar a index
    if request.method == 'POST':
        try:
            empleado.delete()
            messages.success(request, 'Usuario eliminado correctamente')
            return index(request)
        except Exception as e:
            messages.error(request,'Algo salio mal, por favor intentalo de nuevo')
            return index(request)
    
    return render(request, 'EmployeeRecord/delete.html', {'empleado':empleado})



#========vista para buscar empleado=========
def SearchEmployee (request):
    busqueda = ""
    consulta = []
    diccionario_contexto = {}
    
    if request.method == "POST":
        #---obteniendo lo ingresado en barra de busqueda---
        busqueda = request.POST['search_bar']
        #---Extrayendo nombre ingresados y comparando con query a base de datos
        consulta = Empleado.objects.filter(Q(Primer_Nombre__iexact = busqueda) |
                                           Q(Segundo_Nombre__iexact = busqueda) |
                                           Q(Primer_Apellido__iexact = busqueda) |
                                           Q(Segundo_Apellido__iexact = busqueda) |
                                           Q(Documento__iexact = busqueda))
        #print(dir(consulta))
        if len(consulta) > 0:
            messages.success(request, 'Usuarios encontrados')
        else:
            messages.error(request, 'Usuarios no encontrados')
        diccionario_contexto = {'busqueda':busqueda, 'Consulta':consulta}
    return render(request, 'EmployeeRecord/search.html', context = diccionario_contexto)

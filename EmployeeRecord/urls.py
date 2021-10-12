from django.urls import path
from EmployeeRecord import views

# TEMPLATE TAGGING

app_name = "references"

urlpatterns = [
    path('records', views.records, name="listar-empleados"),
    path('insert', views.EnterNewEmployee, name="ingresar-empleado"),
    path('search', views.SearchEmployee, name="buscar-empleado"),
    path('edit/<str:Id>', views.EditEmployee, name="editar-empleado"),
    path('delete/<str:Id>', views.DeleteEmployee, name="eliminar-empleado"),
    ]


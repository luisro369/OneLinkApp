from django.shortcuts import render


# Create your views here.
def index (request):
    return render(request, 'EmployeeRecord/index.html')

def records (request):
    return render(request, 'EmployeeRecord/records.html')

def EnterNewEmployee (request):
    return render(request, 'EmployeeRecord/insert.html')

def SearchEmployee (request):
    return render(request, 'EmployeeRecord/search.html')

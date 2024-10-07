from django.shortcuts import render # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from rest_framework.parsers import JSONParser # type: ignore
from django.http.response import JsonResponse # type: ignore

from . models import Departments, Employees
from . serializers import DepartmentSerializer, EmployeeSerializer



# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET': #For getting data from api.
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=True)
    
    elif request.method == 'POST': #Add data into the database.
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added Record Successfully.', safe=False)
        return JsonResponse('Failed to Add Record.', safe=False)
    
    elif request.method == 'PUT': # Modify DATA in databases with help of unique id.
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        department_serializer = DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Record Updated Successfully.', safe=False)
        return JsonResponse('Failed to Update Record.', safe=False)
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse('Record Deleted Successfully.', safe=False)
    
    else:
        return JsonResponse('Invalid Request Initiated.', safe=False)




#Employee  Rest API with one Snap
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET': #For getting data from api.
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    elif request.method == 'POST': #Add data into the database.
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Added Record Successfully.', safe=False)
        return JsonResponse('Failed to Add Record.', safe=False)
    
    elif request.method == 'PUT': # Modify DATA in databases with help of unique id.
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeID=employee_data['EmployeeID'])
        employee_serializer = EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Record Updated Successfully.', safe=False)
        return JsonResponse('Failed to Update Record.', safe=False)
    
    elif request.method == 'DELETE':
        employee = Departments.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse('Record Deleted Successfully.', safe=False)
    
    else:
        return JsonResponse('Invalid Request Initiated.', safe=False)

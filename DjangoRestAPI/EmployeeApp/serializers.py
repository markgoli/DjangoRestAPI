# Serializers help covert complex data types like django models to and back simple python data structures.
# they help perform basic operations like CRUD Operations.
# They help in Serializations and Deserialization.
# play a key role in REST FRAMEWORK APIs

from rest_framework import serializers # type: ignore
from . models import Departments, Employees

class DepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentID', 'DepartmentName')


class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeID', 'EmployeeName', 'EmployeeDepartment', 'DateOfJoining', 'PhotoFileName')



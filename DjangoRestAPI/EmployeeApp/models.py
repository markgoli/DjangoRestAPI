from django.db import models # type: ignore

# Create your models here.


class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=300, unique=True)




class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=300)
    EmployeeDepartment = models.CharField(max_length=250, unique=True)
    DateOfJoining = models.DateTimeField()
    PhotoFileName = models.CharField(max_length=250)
    

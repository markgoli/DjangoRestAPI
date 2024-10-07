# Generated by Django 5.1.1 on 2024-10-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=300)),
                ('EmployeeDepartment', models.CharField(max_length=250)),
                ('DateOfJoining', models.DateTimeField()),
                ('PhotoFileName', models.CharField(max_length=250)),
            ],
        ),
    ]

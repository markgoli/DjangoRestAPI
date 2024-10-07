from django.urls import path, include
from . import views

urlpatterns = [
    path('department', views.departmentApi),
    path('department/<int:id>', views.departmentApi), # to accepting id as integer and as a request.


    path('employee', views.employeeApi),
    path('employee/<int:id>', views.employeeApi) # to accepting id as integer and as a request.
]

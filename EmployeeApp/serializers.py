from rest_framework import serializers
from .models import Employees, Departements


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departements
        fields=('DepartementId', 'DepartementName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Departement', 'DateOfJoining', 'PhotoName')


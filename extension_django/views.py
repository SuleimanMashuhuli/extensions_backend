from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
"""
ViewSet for viewing employees with search and filter capabilities.
"""
class EmployeeViewSet(viewsets.ModelViewSet):
    """
        API endpoint for Employee CRUD operations.
        Employees are registered ONLY via this API (from frontend).
        
        Supports:
        - GET /api/employees/ - List all employees
        - GET /api/employees/?search=<query> - Search by name or department
        - POST /api/employees/ - Create new employee (from frontend)
        - GET /api/employees/<id>/ - Retrieve single employee
        - PUT /api/employees/<id>/ - Update employee
        - DELETE /api/employees/<id>/ - Delete employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'department']
    filterset_fields = ['department']
    ordering_fields = ['name', 'department', 'created_at']
    ordering = ['name']

    def create_employee(self, request, *args, **kwargs):
        """
            Creating New Employee From Frontend
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "message": "Employee registered successfully",
                "data": serializer.data
            }, 
            status=status.HTTP_201_CREATED
        )

    def update_employee(self, request, *args, **kwargs):
        """
            Updating existing Employee From Frontend
        """
        partial = kwargs.pop('partial', False)
        employee = self.get_object()
        serializer = self.get_serializer(instance=employee, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                "message": "Employee updated successfully",
                "data": serializer.data
            },
             status=status.HTTP_200_OK
        )

    def delete_employee(self, request, *args, **kwargs):
        """
            Deleting Employee From Frontend
        """
        employee = self.get_object()
        employee_name = employee.name
        self.perform_destroy(employee)

        return Response(
            {
                "message": "Employee '{employee_name}' deleted successfully"
            }, 
            status=status.HTTP_204_NO_CONTENT
        )




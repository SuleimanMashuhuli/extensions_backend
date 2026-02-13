import re
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
        Turns Python objects into data that the frontend apps can understand and vice versa.
    """

    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'extension', 'mobile_number', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long")
        return value.strip()

    def validate_extension(self, value):
        if value is None:
            raise serializers.ValidationError("Extension is required")
        str_value = str(value).strip()
    
        if not str_value.isdigit():
            raise serializers.ValidationError("Extension must be a digit number")
        
        if len(str_value) != 4:
            raise serializers.ValidationError("Extension must be exactly 4 digits")

        return int(str_value)


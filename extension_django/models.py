from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    """
        Employee Model
    """

    name = models.CharField(max_length=200, default='')
    department = models.CharField(max_length=100, default='')
    extension = models.CharField(max_length=20, default='')
    mobile_number = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    """
        Metadata tells Django how to behave with this model
    """
    class Meta:
        db_table = 'employees'


    """
        Tell Django how to represent each instance as a human-readable string
    """
    def __str__(self):
        return f"{self.name} - {self.department}"

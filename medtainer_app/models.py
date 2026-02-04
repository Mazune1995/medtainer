from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Admin'),
        ('reception', 'Reception'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

# Department
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

# Equipment
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Available")
    purchase_date = models.DateField()

# Maintenance Record
class MaintenanceRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    performed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

# Activity Log
class ActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

# Inventory
class Inventory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

# Optional: AdminRegistration (only if you actually need it)
class AdminRegistration(models.Model):
    admin_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)

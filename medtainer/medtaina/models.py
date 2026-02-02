from django.contrib . auth.models import AbstractUser
from django.db import models        
# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
    class InventoryItem(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField(blank=True)
        quantity = models.PositiveIntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        last_updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'{self.name} ({self.quantity})'
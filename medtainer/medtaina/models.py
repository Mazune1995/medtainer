from django.contrib . auth.models import AbstractUser
from django.db import models        
# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
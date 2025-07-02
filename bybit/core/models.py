from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance2 = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
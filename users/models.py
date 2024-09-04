from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('employ', 'Employ'),
        ('customer', 'Customer'),
    )
    
    user_role = models.CharField(choices=USER_ROLE_CHOICES, default='customer', max_length=20)

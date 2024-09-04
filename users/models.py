from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # override user model for add extra user roal field 
    USER_ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('employ', 'Employ'),
    )
    user_role = models.CharField(choices=USER_ROLE_CHOICES, default='employ', max_length=20)

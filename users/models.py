from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

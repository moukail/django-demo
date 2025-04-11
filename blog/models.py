from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=128)
    #first_name = models.CharField(max_length=30, blank=True)
    #last_name = models.CharField(max_length=30, blank=True)
    #is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)

    pass
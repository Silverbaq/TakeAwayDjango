# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    phone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    class Meta:
        ordering = ['pk']

    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length = 120, null = False, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    def __str__(self):
        return f'{self.username} - {self.email}'



from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True)
    profile_photo = models.ImageField(blank=True)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('the email must be set')
        return user
        
    def create_superuser(self, email, password):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

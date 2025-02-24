from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import permission

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


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    class Meta:
        permission = [
            ("can_view", "can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete"),



        ]

    def __str__(self):
        return self.title
    
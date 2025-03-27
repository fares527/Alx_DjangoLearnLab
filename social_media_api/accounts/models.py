from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True)
    followers = models.ManyToManyField('self', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custmmuser_set',
        related_query_name='user',

    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permission',
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
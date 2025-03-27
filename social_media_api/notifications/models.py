from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.TextField()
    target = GenericForeignKey()
    timestamp = models.DateTimeField()

from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
    def __str__(self):
        return super().__str__()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.TextField()
    updated_at = models.DateField()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


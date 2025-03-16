from django.db import models


class Author(models.Model):
    """
    asjldhhcb
    """
    name = models.CharField(max_length=200)

class Book(models.Model):
    """
    safcnja
    """
    title = models.CharField(max_length=200)
    publication_date = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

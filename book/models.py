from django.db import models
from genre.models import Genre
from user.models import User
from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.ManyToManyField(Author)
    description = models.TextField(max_length=2000)
    genre = models.ManyToManyField(Genre)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

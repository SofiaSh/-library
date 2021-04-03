from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Genres'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

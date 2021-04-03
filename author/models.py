from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'Authors'

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

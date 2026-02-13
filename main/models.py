from django.db import models
from ckeditor.fields import RichTextField


class Navigation(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
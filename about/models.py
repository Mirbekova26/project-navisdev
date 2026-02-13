from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=200, default='О нас')
    content = RichTextField()
    mission = RichTextField()
    values = RichTextField()

    class Meta:
        verbose_name_plural = 'About'
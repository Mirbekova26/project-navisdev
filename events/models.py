from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    full_description = RichTextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to='events/')

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.slug])

    def __str__(self):
        return self.title
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


class ProjectDirection(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/directions/')

    def get_absolute_url(self):
        return reverse('projects:direction_detail', args=[self.slug])

    def __str__(self):
        return self.name




class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    direction = models.ForeignKey(ProjectDirection, on_delete=models.CASCADE)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/')
    date = models.DateField()
    is_completed = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

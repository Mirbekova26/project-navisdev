from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    requirements = RichTextField()
    conditions = RichTextField()
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vacancies:vacancy_detail', args=[self.slug])

    def __str__(self):
        return self.title
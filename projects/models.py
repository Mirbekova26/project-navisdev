from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse


class ProjectDirection(models.Model):
    name = models.CharField("Название направления", max_length=200)
    slug = models.SlugField("URL", unique=True)
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='projects/directions/')

    class Meta:
        verbose_name = "Направление проекта"
        verbose_name_plural = "Направления проектов"

    def get_absolute_url(self):
        return reverse('projects:direction_detail', args=[self.slug])

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField("Название проекта", max_length=200)
    slug = models.SlugField("URL", unique=True, blank=True)
    direction = models.ForeignKey(
        ProjectDirection,
        verbose_name="Направление",
        on_delete=models.CASCADE
    )
    description = RichTextField("Описание")
    image = models.ImageField("Изображение", upload_to='projects/')
    date = models.DateField("Дата")
    is_completed = models.BooleanField("Завершён", default=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
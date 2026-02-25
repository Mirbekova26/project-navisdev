from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Vacancy(models.Model):
    title = models.CharField("Название вакансии", max_length=200)
    slug = models.SlugField("URL", unique=True)
    description = RichTextField("Описание")
    requirements = RichTextField("Требования")
    conditions = RichTextField("Условия")
    salary_from = models.IntegerField("Зарплата от", null=True, blank=True)
    salary_to = models.IntegerField("Зарплата до", null=True, blank=True)
    is_active = models.BooleanField("Активна", default=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('vacancies:vacancy_detail', args=[self.slug])

    def __str__(self):
        return self.title
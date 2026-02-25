from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Event(models.Model):
    title = models.CharField("Название мероприятия", max_length=200)
    slug = models.SlugField("URL", unique=True)
    description = RichTextField("Краткое описание")
    full_description = RichTextField("Полное описание")
    date = models.DateTimeField("Дата и время проведения")
    location = models.CharField("Место проведения", max_length=300)
    image = models.ImageField("Изображение", upload_to='events/')

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date']  # сортировка по дате (новые сверху)

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.slug])

    def __str__(self):
        return self.title
from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField("Заголовок", max_length=200, default='О нас')
    content = RichTextField("Основной текст")
    mission = RichTextField("Миссия")
    values = RichTextField("Ценности")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "Раздел «О нас»"

    def __str__(self):
        return self.title
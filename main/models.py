from django.db import models
from ckeditor.fields import RichTextField


class Navigation(models.Model):
    name = models.CharField("Название пункта", max_length=100)
    url = models.CharField("Ссылка", max_length=200)
    order = models.IntegerField("Порядок отображения", default=0)

    class Meta:
        verbose_name = "Пункт навигации"
        verbose_name_plural = "Навигация"
        ordering = ['order']

    def __str__(self):
        return self.name
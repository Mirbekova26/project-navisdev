from django.db import models


class Contact(models.Model):
    address = models.TextField("Адрес")
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    telegram = models.URLField("Telegram", blank=True)
    instagram = models.URLField("Instagram", blank=True)

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return "Контактная информация"


class Feedback(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Сообщения обратной связи"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email})"
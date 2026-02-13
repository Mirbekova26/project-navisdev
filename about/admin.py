from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']

    def has_add_permission(self, request):
        # Разрешаем только одну запись
        if About.objects.exists():
            return False
        return True
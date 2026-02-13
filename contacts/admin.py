from django.contrib import admin
from .models import Contact, Feedback


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']

    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        return True


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
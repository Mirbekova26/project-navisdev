from django.contrib import admin
from .models import Project, ProjectDirection

@admin.register(ProjectDirection)
class ProjectDirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'direction', 'date', 'is_completed']
    list_filter = ['direction', 'is_completed', 'date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'

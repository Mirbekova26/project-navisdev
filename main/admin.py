from django.contrib import admin
from projects.models import Project, ProjectDirection
from vacancies.models import Vacancy




@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


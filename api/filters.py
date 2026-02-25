import django_filters
from projects.models import Project
from vacancies.models import Vacancy
from events.models import Event


class ProjectFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    direction_name = django_filters.CharFilter(field_name='direction__name', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['direction', 'is_completed', 'min_date', 'max_date', 'direction_name']


class VacancyFilter(django_filters.FilterSet):
    min_salary = django_filters.NumberFilter(field_name='salary_from', lookup_expr='gte')
    max_salary = django_filters.NumberFilter(field_name='salary_to', lookup_expr='lte')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='date__gte')

    class Meta:
        model = Vacancy
        fields = ['is_active', 'min_salary', 'max_salary', 'created_after']
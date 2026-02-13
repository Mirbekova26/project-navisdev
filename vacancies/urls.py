from django.urls import path
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.vacancies_list, name='vacancies_list'),
    path('<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),
]
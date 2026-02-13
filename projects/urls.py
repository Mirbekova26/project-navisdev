from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('direction/<slug:slug>/', views.direction_detail, name='direction_detail'),
]
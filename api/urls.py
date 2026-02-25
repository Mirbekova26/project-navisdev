from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'directions', views.ProjectDirectionViewSet, basename='direction')
router.register(r'vacancies', views.VacancyViewSet, basename='vacancy')
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'about', views.AboutViewSet, basename='about')
router.register(r'contacts', views.ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback'),
]
from rest_framework import viewsets, filters, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from projects.models import Project, ProjectDirection
from vacancies.models import Vacancy
from events.models import Event
from about.models import About
from contacts.models import Contact, Feedback
from .serializers import *


# Кастомная пагинация
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProjectDirectionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для направлений проектов"""
    queryset = ProjectDirection.objects.all()
    serializer_class = ProjectDirectionSerializer
    lookup_field = 'slug'
    pagination_class = CustomPagination


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для проектов"""
    queryset = Project.objects.all().order_by('-date')
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['direction', 'is_completed']
    search_fields = ['title', 'description']
    ordering_fields = ['date', 'title']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer

    @action(detail=False, methods=['get'])
    def by_direction(self, request):
        """Получить проекты по направлению"""
        direction_slug = request.query_params.get('direction', None)
        if direction_slug:
            direction = get_object_or_404(ProjectDirection, slug=direction_slug)
            projects = self.queryset.filter(direction=direction)
            page = self.paginate_queryset(projects)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response({"error": "direction parameter required"}, status=400)


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для вакансий"""
    queryset = Vacancy.objects.filter(is_active=True).order_by('-created_at')
    lookup_field = 'slug'
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'requirements']
    ordering_fields = ['created_at', 'salary_from', 'title']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VacancySerializer
        return VacancyListSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для мероприятий"""
    queryset = Event.objects.all().order_by('date')
    lookup_field = 'slug'
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location']
    search_fields = ['title', 'description']
    ordering_fields = ['date', 'title']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EventSerializer
        return EventListSerializer

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Получить предстоящие мероприятия"""
        from django.utils import timezone
        upcoming_events = self.queryset.filter(date__gte=timezone.now())
        page = self.paginate_queryset(upcoming_events)
        serializer = EventListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'])
    def past(self, request):
        """Получить прошедшие мероприятия"""
        from django.utils import timezone
        past_events = self.queryset.filter(date__lt=timezone.now())
        page = self.paginate_queryset(past_events)
        serializer = EventListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для страницы 'О нас'"""
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        """Возвращаем первую запись о компании"""
        about = About.objects.first()
        if about:
            serializer = self.get_serializer(about)
            return Response(serializer.data)
        return Response({"detail": "Информация не найдена"}, status=404)


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для контактов"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        """Возвращаем контакты"""
        contact = Contact.objects.first()
        if contact:
            serializer = self.get_serializer(contact)
            return Response(serializer.data)
        return Response({"detail": "Контакты не найдены"}, status=404)


class FeedbackCreateView(generics.CreateAPIView):
    """View для создания обратной связи"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Спасибо за обратную связь!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
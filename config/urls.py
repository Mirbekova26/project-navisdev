from django.contrib import admin  # Этого импорта не хватает!
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Navisdevs API",
        default_version='v1',
        description="API для сайта Navisdevs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@navisdevs.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('admin/', admin.site.urls),  # Теперь admin найден

                  # ВРЕМЕННО ЗАКОММЕНТИРОВАНО
                  # path('', include('main.urls')),
                  # path('projects/', include('projects.urls')),
                  # path('vacancies/', include('vacancies.urls')),
                  # path('events/', include('events.urls')),
                  # path('contacts/', include('contacts.urls')),
                  # path('about/', include('about.urls')),

                  # API URLs
                  path('api/', include('api.urls')),

                  # Swagger документация
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
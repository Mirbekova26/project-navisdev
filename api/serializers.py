from rest_framework import serializers
from projects.models import Project, ProjectDirection
from vacancies.models import Vacancy
from events.models import Event
from about.models import About
from contacts.models import Contact, Feedback


class ProjectDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDirection
        fields = ['id', 'name', 'slug', 'description', 'image']


class ProjectSerializer(serializers.ModelSerializer):
    direction_name = serializers.CharField(source='direction.name', read_only=True)
    direction_slug = serializers.CharField(source='direction.slug', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'direction', 'direction_name',
            'direction_slug', 'description', 'image', 'date', 'is_completed'
        ]


class ProjectDetailSerializer(ProjectSerializer):
    direction = ProjectDirectionSerializer(read_only=True)

    class Meta(ProjectSerializer.Meta):
        fields = ProjectSerializer.Meta.fields + ['direction']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'id', 'title', 'slug', 'description', 'requirements',
            'conditions', 'salary_from', 'salary_to', 'is_active', 'created_at'
        ]


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'slug', 'salary_from', 'salary_to', 'created_at']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'title', 'slug', 'description', 'full_description',
            'date', 'location', 'image'
        ]


class EventListSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        model = Event
        fields = ['id', 'title', 'slug', 'description', 'date', 'location', 'image']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'content', 'mission', 'values']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'phone', 'email', 'telegram', 'instagram']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)
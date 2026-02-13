from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Event

def events_list(request):
    events = Event.objects.all().order_by('-date')
    context = {
        'events': events,
        'title': 'Мероприятия'
    }
    return render(request, 'events/list.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    context = {
        'event': event,
        'title': event.title
    }
    return render(request, 'events/detail.html', context)
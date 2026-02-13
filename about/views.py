from django.shortcuts import render
from .models import About

def about_view(request):
    about_info = About.objects.first()
    context = {
        'about': about_info,
        'title': 'О нас'
    }
    return render(request, 'about/index.html', context)
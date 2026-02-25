from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
        <h1>NAVISDEV Главная</h1>
        <p>Сайт работает!</p>
        <ul>
            <li><a href="/admin/">Админка</a></li>
            <li><a href="/api/">API</a></li>
        </ul>
    """)

# Добавьте другие представления по мере необходимости
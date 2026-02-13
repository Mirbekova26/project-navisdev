from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Feedback
from .forms import FeedbackForm


def contacts_view(request):
    contact_info = Contact.objects.first()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contacts')
    else:
        form = FeedbackForm()

    context = {
        'contact': contact_info,
        'form': form,
        'title': 'Контакты'
    }
    return render(request, 'contacts/index.html', context)
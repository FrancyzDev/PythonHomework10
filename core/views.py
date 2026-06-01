from os import error
from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})

def custom_404(request, exception=None):
    error_message = str(exception) if exception else ""
    error_message = error_message if len(error_message) < 50 else '' # Убрал длиные текста дебага для красоты
    return render(request, '404.html', {
        'path': request.path,
        'error_message': error_message
    }, status=404)
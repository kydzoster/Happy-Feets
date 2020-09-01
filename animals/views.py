from django.shortcuts import render
from .models import Animal


def home(request):
    context = {
        'animals': Animal.objects.all(),
    }
    return render(request, 'home.html', context)


def search(request):
    context = {}
    return render(request, 'search.html', context)

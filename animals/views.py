from django.shortcuts import render
from .models import Animal
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):

    animals = Animal.objects.all()
    mammals = Animal.objects.filter(Q(animal='Cat') | Q(animal='Dog'))
    paginator1 = Paginator(mammals, 1)
    page = request.GET.get('mammalspage')
    mammals = paginator1.get_page(page)

    others = Animal.objects.filter(Q(animal='Reptile') | Q(animal='Bird'))
    paginator2 = Paginator(others, 1)
    page = request.GET.get('otherspage')
    others = paginator2.get_page(page)

    context = {
        'animals': animals,
        'mammals': mammals,
        'others': others,
    }
    return render(request, 'home.html', context)


def search(request):
    context = {}
    return render(request, 'search.html', context)

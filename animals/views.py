from django.shortcuts import render
from .models import Animal
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


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


def detail(request, animal_id):
    # find an animal with this id if it does not exist pass 404
    animal = get_object_or_404(Animal, pk=animal_id)
    animals = Animal.objects.all()

    context = {
        'animal': animal,
        'animals': animals,
    }
    return render(request, 'detail.html', context)


def search(request):
    animals = Animal.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        animals = animals.filter(
            Q(name__icontains=search_query) |
            Q(animal__icontains=search_query) |
            Q(gender__iexact=search_query)
        )
    context = {
        'animals': animals,
        'search_query': search_query,
    }
    return render(request, 'search.html', context)

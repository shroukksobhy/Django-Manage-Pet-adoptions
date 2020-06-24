from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets
    })


def pet_details(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request, 'pet_details.html', {
        'pet': pet,

    })

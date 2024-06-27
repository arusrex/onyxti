from django.shortcuts import render, redirect
from home.models import Carousel

def index(request):
    carousels = Carousel.objects.all()

    context = {
        'carousels': carousels,
    }
    
    return render(request, 'home/pages/index.html', context)
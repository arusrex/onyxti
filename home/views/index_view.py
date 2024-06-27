from django.shortcuts import render, redirect
from home.models import *

def index(request):
    carousels = Carousel.objects.order_by('-id')[:5]
    team = Team.objects.first()
    services = Services.objects.first()
    services_items = ServicesItems.objects.order_by('-id')[:3]
    new_ideas = NewIdeas.objects.first()
    new_idea_items = NewIdeasItems.objects.order_by('-id')[:3]
    testemonials = Testemonial.objects.first()
    testemonial_items = TestemonialsItems.objects.order_by('-id')[:2]

    context = {
        'carousels': carousels,
        'team': team,
        'services': services,
        'services_items': services_items,
        'new_ideas': new_ideas,
        'new_idea_items': new_idea_items,
        'testemonials': testemonials,
        'testemonial_items': testemonial_items,
    }

    return render(request, 'home/pages/index.html', context)
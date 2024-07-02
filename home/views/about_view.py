from django.shortcuts import render
from home.models import Team

def about(request):
    team = Team.objects.first()

    context = {
        'team': team,
    }

    return render(request, 'home/pages/about.html', context)

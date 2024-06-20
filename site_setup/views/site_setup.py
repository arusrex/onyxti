from django.shortcuts import render
from site_setup.models import SiteSetup

def site_setup(request):
    settings = SiteSetup.objects.first()
    
    context = {
        'settings': settings,
    }

    return context

from django.shortcuts import render
from site_setup.models import SiteSetup

def site_setup(request):
    try:
        settings = SiteSetup.objects.first()
    except Exception as e:
        print(f'Usúario master não criou as primeiras configurações, erro: {e}')
        settings = ''
    
    context = {
        'settings': settings,
    }

    return context

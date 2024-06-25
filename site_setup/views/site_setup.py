from django.shortcuts import redirect
from site_setup.models import SiteSetup
from home.forms import NewsLetterForm, ContactForm
from django.contrib import messages

def site_setup(request):
    try:
        settings = SiteSetup.objects.first()
        newsletter_form = NewsLetterForm()
        contact_form = ContactForm()
    except Exception as e:
        print(f'Usúario master não criou as primeiras configurações, erro: {e}')
        settings = ''
    
    context = {
        'settings': settings,
        'newsletter_form': newsletter_form,
        'contact_form': contact_form,
    }

    return context


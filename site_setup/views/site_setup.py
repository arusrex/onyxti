from django.shortcuts import redirect, render
from site_setup.models import SiteSetup
from home.forms import NewsLetterForm, ContactForm
from site_setup.forms import SiteSetupForm
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

def dashboard_settings(request):
    obj = SiteSetup.objects.first()
    form = SiteSetupForm(instance=obj)

    if request.method == 'POST':
        form = SiteSetupForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:settings')
        else:
            messages.error(request, 'Error!')
            return redirect('home:settings')
    
    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/settings.html', context)


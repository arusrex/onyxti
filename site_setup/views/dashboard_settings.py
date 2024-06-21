from django.shortcuts import render
from home.models import NewsLetter, Contact

def dashboard(request):
    newsletter = NewsLetter.objects.order_by('-created_at')[:20]
    contacts = Contact.objects.order_by('-created_at')[:20]

    context = {
        'newsletter': newsletter,
        'contacts': contacts,
    }

    return render(request, 'dashboard/pages/control.html', context)
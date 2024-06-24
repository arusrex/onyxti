from django.shortcuts import render
from home.models import NewsLetter, Contact

def dashboard(request):
    try:
        newsletter = NewsLetter.objects.order_by('-created_at')[:20]
        contacts = Contact.objects.order_by('-created_at')[:20]
    except Exception as e:
        print(f'Provavelmente a causa do erro é a ausência de dados ou da própria tabela no banco de dados, o erro é: {e}')
        newsletter = ''
        contacts = ''

    context = {
        'newsletter': newsletter,
        'contacts': contacts,
    }

    return render(request, 'dashboard/pages/control.html', context)
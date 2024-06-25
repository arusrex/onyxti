from django.shortcuts import render
from home.models import NewsLetter, Contact

def dashboard(request):
    try:
        newsletter = NewsLetter.objects.all()
        contacts = Contact.objects.all()
    except Exception as e:
        print(f'Provavelmente a causa do erro é a ausência de dados ou da própria tabela no banco de dados, o erro é: {e}')
        newsletter = ''
        contacts = ''

    context = {
        'newsletter': newsletter,
        'contacts': contacts,
    }

    return render(request, 'dashboard/pages/control.html', context)
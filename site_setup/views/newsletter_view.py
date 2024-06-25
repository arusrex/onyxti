from django.shortcuts import redirect
from home.forms import NewsLetterForm
from django.contrib import messages
from site_setup.models import SiteSetup

def newsletter(request):
    settings = SiteSetup.objects.first()
    form = NewsLetterForm()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Obrigado por se inscrever em nosso sistema, estaremos enviando no seu email os destaques e novidades da {settings.site_name}') # type: ignore
            return redirect('home:index')
        else:
            messages.error(request, 'Erro ao se inscrever, tente novamente mais tarde!')
            return redirect('home:index')
    return redirect('home:index')
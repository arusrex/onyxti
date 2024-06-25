from django.shortcuts import redirect, render
from home.forms import NewsLetterForm
from django.contrib import messages
from site_setup.models import SiteSetup
from home.models import NewsLetter
from django.core.paginator import Paginator

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

def newsletters(request):
    objs = NewsLetter.objects.order_by('-created_at')

    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'dashboard/pages/newsletters.html', context)

def delete_newsletter(request, id):
    obj = NewsLetter.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    return redirect('home:newsletters')
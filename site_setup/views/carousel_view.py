from home.models import Carousel
from home.forms import BannerForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

def banner(request):
    if request.method == 'POST':
        banner_form = BannerForm(request.POST, request.FILES)
        if banner_form.is_valid():
            banner_form.save()
            messages.success(request, 'Saved !')
            return redirect(request, 'home:carousel')
    else:
        banner_form = BannerForm()
    
    banners = Carousel.objects.order_by('-id')

    paginator = Paginator(banners, 20)  # 10 objetos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'banner_form': banner_form,
        'carousel': page_obj,
    }

    return render(request, 'dashboard/pages/carousel.html', context)

def delete_banner(request, id):
    obj = Carousel.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted !')
        return redirect(request, 'home:carousel')
    else:
        messages.error(request, 'Erro, register not deleted')
        return redirect(request, 'home:carousel')

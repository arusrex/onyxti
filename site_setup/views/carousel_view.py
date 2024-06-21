from home.models import Carousel
from home.forms import BannerForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

def banners(request):
    objs = Carousel.objects.order_by('-id')
    form = BannerForm()

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved !')
            return redirect(request, 'home:carousel')

    paginator = Paginator(objs, 20)  # 20 objetos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/carousel.html', context)


def edit_banner(request, id):
    obj = Carousel.objects.get(id=id)

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated !')
            return redirect('home:carousel')
    else:
        update_form = BannerForm(instance=obj)

    context = {
        'obj': obj,
        'update_form': update_form,
    }

    return render(request, 'dashboard/partials/_edit_banner.html', context)

def delete_banner(request, id):
    obj = Carousel.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted !')
        return redirect('home:carousel')
    else:
        messages.error(request, 'Erro, register not deleted')
        return redirect('home:carousel')

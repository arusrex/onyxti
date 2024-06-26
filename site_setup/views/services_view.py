from django.shortcuts import render, redirect
from home.models import Services, ServicesItems
from home.forms import ServicesForm, ServicesItemsForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def dash_services(request):
    obj = Services.objects.first()
    form = ServicesForm(instance=obj)

    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
    
    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/services.html', context)

@login_required
def services_items(request):
    objs = ServicesItems.objects.order_by('-id')
    form = ServicesItemsForm()

    if request.method == 'POST':
        form = ServicesItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            redirect('home:services_items')

    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/services_items.html', context)

@login_required
def edit_service(request, id):
    obj = ServicesItems.objects.get(id=id)
    update_form = ServicesItemsForm(instance=obj)

    if request.method == 'POST':
        form = ServicesItemsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
    
    context = {
        'obj': obj,
        'update_form': update_form,
    }

    return render(request, 'dashboard/partials/_edit_services.html', context)

@login_required
def delete_service(request, slug):
    obj = ServicesItems.objects.get(slug=slug)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    
    return redirect('home:services_items')
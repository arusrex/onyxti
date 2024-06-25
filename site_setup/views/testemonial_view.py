from django.shortcuts import render, redirect
from home.models import Testemonial, TestemonialsItems
from home.forms import TestemonialForm, TestemonialItemsForm
from django.contrib import messages
from django.core.paginator import Paginator

def dash_testemonial(request):
    obj = Testemonial.objects.first()
    form = TestemonialForm(instance=obj)

    if request.method == 'POST':
        form = TestemonialForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:dash_testemonial')
        else:
            messages.error(request, 'Error!')
            return redirect('home:dash_testemonial')
    
    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/testemonials.html', context)

def testemonials(request):
    objs = TestemonialsItems.objects.order_by('-id')
    form = TestemonialItemsForm()

    if request.method == 'POST':
        form = TestemonialItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:testemonials')
        else:
            messages.error(request, 'Error!')
            return redirect('home:testemonials')
    
    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/testemonial_items.html', context)

def testemonial(request, id):
    obj = TestemonialsItems.objects.get(id=id)
    form = TestemonialItemsForm(instance=obj)

    if request.method == 'POST':
        form = TestemonialItemsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:testemonial', id=id)
        else:
            messages.error(request, 'Error!')
            return redirect('home:testemonial', id=id)
    
    context = {
        'obj': obj,
        'update_form': form,
    }

    return render(request, 'dashboard/partials/_edit_testemonial_items.html', context)

def delete_testemonial(request, id):
    obj = TestemonialsItems.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    return redirect('home:testemonials')
        
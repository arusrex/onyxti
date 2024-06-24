from home.models import NewIdeas, NewIdeasItems
from home.forms import NewIdeasForm, NewIdeasItemsForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

def new_ideas(request):
    obj = NewIdeas.objects.first()
    form = NewIdeasForm(instance=obj)

    if request.method == 'POST':
        form = NewIdeasForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:new_ideas')    
    
    context = {
        'obj':obj,
        'form': form,
        }
    
    return render(request, 'dashboard/pages/new_ideas.html', context)

def new_ideas_items(request):
    objs = NewIdeasItems.objects.order_by('-id')
    form = NewIdeasItemsForm()

    if request.method == 'POST':
        form = NewIdeasItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:new_ideas_items')
        
    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/new_idea_items.html', context)

def edit_new_idea(request, slug):
    obj = NewIdeasItems.objects.get(slug=slug)
    form = NewIdeasItemsForm(instance=obj)

    if request.method == 'POST':
        form = NewIdeasItemsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
            return redirect('home:new_ideas_items')
    
    context = {
        'obj': obj,
        'update_form': form,
    }

    return render(request, 'dashboard/partials/_edit_new_idea.html', context)

def delete_new_idea(request, slug):
    obj = NewIdeasItems.objects.get(slug=slug)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    
    return redirect('home:new_ideas_items')

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from home.models import BlogItems
from home.forms import BlogItemsForm
from django.contrib import messages

def blog_items(request):
    objs = BlogItems.objects.order_by('-created_at')
    form = BlogItemsForm()

    if request.method == 'POST':
        form = BlogItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved')
        else:
            messages.error(request, 'Error!')
        
        return redirect('home:blog_items')
    
    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/blog.html', context)

def edit_blog_item(request, slug):
    obj = BlogItems.objects.get(slug=slug)
    form = BlogItemsForm(instance=obj)

    if request.method == 'POST':
        form = BlogItemsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error')
        
        return redirect('home:edit_blog_item', slug=slug)
    
    context = {
        'obj': obj,
        'update_form': form,
    }

    return render(request, 'dashboard/partials/_edit_blog_item.html', context)

def delete_blog_item(request, slug):
    obj = BlogItems.objects.get(slug=slug)

    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    
    return redirect('home:blog_items')
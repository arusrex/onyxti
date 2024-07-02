from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from home.models import BlogItems
from home.forms import BlogItemsForm
from django.contrib import messages

def blog(request):
    objs = BlogItems.objects.order_by('-created_at')
    
    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'home/pages/blog.html', context)

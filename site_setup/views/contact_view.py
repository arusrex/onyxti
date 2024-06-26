from django.shortcuts import render, redirect
from home.models import Contact
from home.forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def contacts(request):
    objs = Contact.objects.order_by('-created_at')

    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'dashboard/pages/contacts.html', context)


@login_required
def delete_contact(request, id):
    obj = Contact.objects.get(id=id)

    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    return redirect('home:contacts')
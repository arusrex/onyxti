from django.shortcuts import render, redirect
from home.models import NewsLetter, Contact
from site_setup.forms import NewUserForm, EditUserForm, PasswordEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

def dashboard(request):
    try:
        newsletter = NewsLetter.objects.order_by('-created_at')[:5]
        contacts = Contact.objects.order_by('-created_at')[:5]
    except Exception as e:
        print(f'Provavelmente a causa do erro é a ausência de dados ou da própria tabela no banco de dados, o erro é: {e}')
        newsletter = ''
        contacts = ''

    context = {
        'newsletter': newsletter,
        'contacts': contacts,
    }

    return render(request, 'dashboard/pages/control.html', context)

def users(request):
    objs = User.objects.order_by('-id')
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')
        return redirect('home:users')
    
    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'form': form,
    }

    return render(request, 'dashboard/pages/users.html', context)

def edit_user(request, id):
    obj = User.objects.get(id=id)
    form = EditUserForm(instance=obj)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')
        return redirect('home:edit_user', id=id)
    
    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'dashboard/partials/_edit_user.html', context)

def edit_self(request):
    obj = request.user
    form = EditUserForm(instance=obj)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')
    
    context = {
        'form': form,
    }

    return render(request, 'dashboard/partials/_edit_user.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordEditForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')
        return redirect('home:change_password')
    else:
        form = PasswordEditForm(user=request.user)
    
    context = {
        'form': form,
    }

    return render(request, 'dashboard/partials/_change_password.html', context)

def delete_user(request, id):
    obj = User.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    else:
        messages.error(request, 'Error!')
    return redirect('home:users')

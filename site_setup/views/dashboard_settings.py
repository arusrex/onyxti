from django.shortcuts import render, redirect
from home.models import NewsLetter, Contact
from site_setup.models import MenuLinks
from site_setup.forms import NewUserForm, EditUserForm, PasswordEditForm, MenuLinksForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Success!')
                return redirect('home:dashboard')
            else:
                messages.error(request, 'Error!')
        else:
            messages.error(request, 'Error!')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    
    return render(request, 'dashboard/pages/authentication.html', context)

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Success!')
    return redirect('home:login')

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_user(request, id):
    obj = User.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    else:
        messages.error(request, 'Error!')
    return redirect('home:users')

@login_required
def menu_links(request):
    objs = MenuLinks.objects.all()
    form = MenuLinksForm()

    if request.method == 'POST':
        form = MenuLinksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')
        return redirect('home:menu_links')
    
    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj,
    }

    return render(request, 'dashboard/pages/menu_links.html', context)

@login_required
def edit_menu_links(request, id):
    obj = MenuLinks.objects.get(id=id)
    form = MenuLinksForm(instance=obj)

    if request.method == 'POST':
        form = MenuLinksForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved!')
        else:
            messages.error(request, 'Error!')

        return redirect('home:edit_menu_links', id=id)
    
    context = {
        'obj': obj,
        'update_form': form,
    }

    return render(request, 'dashboard/partials/_edit_menu_links.html', context)

@login_required
def delete_menu_links(request, id):
    obj = MenuLinks.objects.get(id=id)
    if obj:
        obj.delete()
        messages.success(request, 'Deleted!')
    
    return redirect('home:menu_links')

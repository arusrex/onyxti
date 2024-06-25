from django.shortcuts import render, redirect
from home.forms import ContactForm
from django.contrib import messages
from home.models import Contact

def contact(request):
    return render(request, 'home/pages/contact.html')

def new_contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso, entraremos em contato em breve!')
            return redirect('home:contact')
        else:
            messages.error(request, 'Algo deu errado, tente novamente mais tarde!')

    return redirect('home:contact')


    


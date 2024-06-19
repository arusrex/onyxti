from django.shortcuts import render

def index(request):
    return render(request, 'home/pages/index.html')

def blog(request):
    return render(request, 'home/pages/blog.html')

def contact(request):
    return render(request, 'home/pages/contact.html')

def about(request):
    return render(request, 'home/pages/about.html')

def services(request):
    return render(request, 'home/pages/services.html')
from django.shortcuts import render

def services(request):
    return render(request, 'home/pages/services.html')
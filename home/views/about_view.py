from django.shortcuts import render

def about(request):
    return render(request, 'home/pages/about.html')

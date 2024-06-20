from django.shortcuts import render

def blog(request):
    return render(request, 'home/pages/blog.html')
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/pages/control.html')

def site_setup(request):
    pass

from django.shortcuts import render
from home.models import Services, ServicesItems
from django.core.paginator import Paginator

def services(request):
    services = Services.objects.first()
    services_items = ServicesItems.objects.order_by('-id')

    paginator = Paginator(services_items, 9)
    page_number = request.GET.get('page')
    services_items = paginator.get_page(page_number)

    context = {
        'services': services,
        'services_items': services_items,
    }
    return render(request, 'home/pages/services.html', context)
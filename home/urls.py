from django.urls import path
from home.views import blog, contact, about, index, services
from site_setup.views import dashboard, banner, delete_banner

app_name = 'home'

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),

    # DASHBOARD
    path('dashboard/', dashboard, name="dashboard"),

    # CAROUSEL
    path('carousel/', banner, name="carousel"),
    path('delete_banner', delete_banner, name="delete_banner"),
]
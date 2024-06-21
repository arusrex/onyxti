from django.urls import path
from home.views import blog, contact, about, index, services
from site_setup.views import dashboard, team
from site_setup.views.carousel_view import *

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
    path('carousel/', banners, name="carousel"),
    path('edit_banner/<int:id>/', edit_banner, name="edit_banner"),
    path('delete_banner/<int:id>/', delete_banner, name="delete_banner"),

    # TEAM
    path('team/', team, name="team"),
]
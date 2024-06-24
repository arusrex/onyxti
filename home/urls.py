from django.urls import path
from home.views import blog, contact, about, index, services
from site_setup.views import dashboard, team
from site_setup.views.services_view import *
from site_setup.views.carousel_view import *
from site_setup.views.new_ideas_view import *

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

    # SERVICES
    path('dash_services/', dash_services, name="dash_services"),

    # SERVICES ITEMS
    path('services_items/', services_items, name="services_items"),
    path('edit_service/<int:id>/', edit_service, name="edit_service"),
    path('delete_service/<slug:slug>/', delete_service, name="delete_service"),

    #NEW IDEAS
    path('new_ideas/', new_ideas, name="new_ideas"),
    path('new_ideas_items/', new_ideas_items, name="new_ideas_items"),
    path('edit_new_idea/<slug:slug>/', edit_new_idea, name="edit_new_idea"),
    path('delete_new_idea/<slug:slug>/', delete_new_idea, name="delete_new_idea"),
]
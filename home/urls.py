from django.urls import path
from home.views import index, blog, contact, about, services

app_name = 'home'

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('contact', contact, name="contact"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
]
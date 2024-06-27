from django.urls import path
from home.views import blog, about, index, services
from site_setup.views import dashboard, team, dashboard_settings
from site_setup.views.services_view import *
from site_setup.views.carousel_view import *
from site_setup.views.new_ideas_view import *
from site_setup.views.testemonial_view import *
from site_setup.views.newsletter_view import *
from home.views.contact_view import *
from site_setup.views.contact_view import *
from site_setup.views.dashboard_settings import *

app_name = 'home'

urlpatterns = [
    path('', index, name="index"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),

    #AUTHENTICATION
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

    #USER
    path('users/', users, name="users"),
    path('edit_user/<int:id>/', edit_user, name="edit_user"),
    path('edit_self/', edit_self, name="edit_self"),
    path('change_password/', change_password, name="change_password"),
    path('delete_user/<int:id>/', delete_user, name="delete_user"),

    #SETTINGS
    path('settings/', dashboard_settings, name="settings"),

    #MENU LINKS
    path('menu_links/', menu_links, name="menu_links"),
    path('edit_menu_links/<int:id>/', edit_menu_links, name="edit_menu_links"),
    path('delete_menu_links/<int:id>/', delete_menu_links, name="delete_menu_links"),

    #CONTACTS
    path('contacts/', contacts, name="contacts"),
    path('new_contact/', new_contact, name="new_contact"),
    path('delete_contact/<int:id>/', delete_contact, name="delete_contact"),

    #NEWSLETTER
    path('newsletter/', newsletter, name="newsletter"),
    path('newsletters/', newsletters, name="newsletters"),
    path('delete_newsletter/<int:id>/', delete_newsletter, name="delete_newsletter"),

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

    #TESTEMONIALS
    path('dash_testemonial/', dash_testemonial, name="dash_testemonial"),
    path('testemonials/', testemonials, name="testemonials"),
    path('testemonial/<int:id>/', testemonial, name="testemonial"),
    path('delete_testemonial/<int:id>/', delete_testemonial, name="delete_testemonial"),
]
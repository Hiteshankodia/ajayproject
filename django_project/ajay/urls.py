from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name  = 'ajay-home'),
    path('about', views.about, name = 'ajay-about'), 
    path('contact', views.contact, name = 'ajay-contact'),
    path('services', views.services, name = 'ajay-services')   
]
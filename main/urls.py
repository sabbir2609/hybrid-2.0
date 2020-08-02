from django.urls import path
from .views import home,contact,about

urlpatterns = [
    path('',home,name='Home'),
    path('contact/',contact,name='Contact'),
    path('about/',about,name='About')
]
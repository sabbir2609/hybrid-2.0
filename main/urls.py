from django.urls import path
from .views import home,contact,about,user

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contact/', contact, name='Contact'),
    path('about/', about, name='about'),
    path('signup/', user, name='signup'),
]
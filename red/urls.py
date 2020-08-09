from django.urls import path
from .views import blood

urlpatterns = [
    path('',blood,name='Blood'),
   # path('donar/',donar,name='Donar'),
   # path('available-donar/', available-donar ,name='Available'),
]
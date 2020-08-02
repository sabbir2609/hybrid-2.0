from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def home(request):
    #testing value
    x = datetime.datetime.now()
    
    home = "Homepage"
    context = {'title':home,'time':x}
    return render(request, 'home.html', context)

def contact(request):
    t = "Contact"
    context = {'title':t}
    return render(request, 'contact.html', context)
    
def about(request):
    t = "About Us"
    context = {'title':t}
    return render(request, 'about.html', context)
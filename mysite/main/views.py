from django.shortcuts import render
from .models import Car

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',)


def private_leasing(request):
    return render(request=request,
                  template_name='main/private_leasing.html',
                  context={'cars': Car.objects.all})


def business_leasing(request):
    return render(request=request,
                  template_name='main/business_leasing.html',)


def contact(request):
    return render(request=request,
                  template_name='main/contact.html',)

from django.shortcuts import render
from .models import Car
from .forms import LoginForm
# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm, 'username': request.user.username})


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


def car(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request=request,
                  template_name='main/cars/car_details.html',
                  context={'car': car},)

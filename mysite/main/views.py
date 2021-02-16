from django.shortcuts import render, redirect
from .models import Car, User, Profile
from .forms import LoginForm, NewUserForm, RegisterProfileForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.urls import reverse

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm,
                           })


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


def profile(request):
    return render(request=request,
                  template_name='main/profile.html',)


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in: {username}")
                return redirect('/')

    messages.error(request,
                   f"login failed, the login details provided were either wrong or the given user has not yet been activated, if the latter, contact helpdesk")
    return redirect('main:homepage')


def logout_request(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('main:homepage')


def register(request):
    if request.method == 'POST':
        userForm = NewUserForm(request.POST)
        profileForm = RegisterProfileForm(request.POST)
        print(userForm.errors.as_data())
        print(request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.profile.profilePhoneNumber = request.POST['profilePhoneNumber']
            user.profile.profileCprNumber = request.POST['profileCprNumber']
            user.profile.profileAddress = request.POST['profileAddress']
            user.profile.profileCity = request.POST['profileCity']
            user.profile.profilePostalCode = request.POST['profilePostalCode']
            user.save()
            username = userForm.cleaned_data.get('username')
            login(request, user)

            messages.success(request, f"New account created: {username}")
            messages.success(request, f"Logged in: {username}")
            return redirect('main:homepage')
        else:
            for msg in userForm.error_messages:
                messages.error(
                    request, f"{msg}: {userForm.error_messages[msg]}")
            return redirect('main:homepage')

    form = UserCreationForm
    return render(request=request,
                  template_name='main:homepage',
                  context={'form': form, 'loginForm': LoginForm})

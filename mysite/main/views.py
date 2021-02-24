from django.shortcuts import render, redirect
from .models import Car, User, Profile, PrivateLease, CompanyLease, Company
from .forms import LoginForm, NewUserForm, RegisterProfileForm, UserForm, ProfileForm, ContactForm, CompanyForm, PrivateLeasingForm, BusinessLeasingForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from datetime import date

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={'loginForm': LoginForm,
                           'username': request.user.username,
                           'user_id': request.user.id,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm,
                           })


def private_leasing(request):
    return render(request=request,
                  template_name='main/private_leasing.html',
                  context={'cars': Car.objects.filter(carReadyForPrivateLeasing=True),
                           'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm, })


def business_leasing(request):
    return render(request=request,
                  template_name='main/business_leasing.html',
                  context={'cars': Car.objects.filter(carReadyForBusinessLeasing=True),
                           'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm, })


def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            your_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, your_email,
                          ['mort333c@edu.sde.dk'])
            except BadHeaderError:
                for msg in contact_form.error_messages:
                    messages.error(
                        request, f"{msg}: {contact_form.error_messages[msg]}")
    return render(request=request,
                  template_name='main/contact.html',
                  context={'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm,
                           'contact_form': contact_form})


def business_car(request, car_id):
    car = Car.objects.get(id=car_id)
    currentUser = request.user
    customerCompanies = Company.objects.filter(contactPerson=currentUser)
    today = date.today()
    todayFormatted = today.strftime("%Y-%m-%d")
    if request.method == 'POST':
        businessLeasingForm = BusinessLeasingForm(request.POST)
        print(businessLeasingForm.errors.as_data())
        if businessLeasingForm.is_valid():
            leaseStartDate = businessLeasingForm.cleaned_data['start_date']
            leaseEndDate = businessLeasingForm.cleaned_data['end_date']
            leaseDownpayment = businessLeasingForm.cleaned_data['down_payment']
            leaseMonthlyPrice = businessLeasingForm.cleaned_data['monthly_price']
            leaseMilesPerYear = businessLeasingForm.cleaned_data['miles_per_year']
            leaseCar = car
            print(businessLeasingForm.cleaned_data['company'])
            leaseCompany = Company.objects.get(id=businessLeasingForm.cleaned_data['company'])

            newBusinessLease = CompanyLease(leaseStartDate=leaseStartDate, leaseEndDate=leaseEndDate, leaseDownpayment=leaseDownpayment,
                                            leaseMonthlyPrice=leaseMonthlyPrice, leaseMilesPerYear=leaseMilesPerYear, leaseCar=leaseCar, leaseCustomerCompany=leaseCompany)

            newBusinessLease.save()

            car.carCurrentlyLeased = True
            car.save()

            return redirect("main:profile_page")

    return render(request=request,
                  template_name='main/businesscars/car_details.html',
                  context={'car': car,
                           'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm,
                           'businessLeasingForm': BusinessLeasingForm,
                           'today': todayFormatted,
                           'current_user': currentUser,
                           'customer_companies': customerCompanies})


def private_car(request, car_id):
    car = Car.objects.get(id=car_id)
    currentUser = request.user
    today = date.today()
    todayFormatted = today.strftime("%Y-%m-%d")
    if request.method == 'POST':
        privateLeasingForm = PrivateLeasingForm(request.POST)
        print(privateLeasingForm.errors.as_data())
        if privateLeasingForm.is_valid():
            leaseStartDate = privateLeasingForm.cleaned_data['start_date']
            leaseEndDate = privateLeasingForm.cleaned_data['end_date']
            leaseDownpayment = privateLeasingForm.cleaned_data['down_payment']
            leaseMonthlyPrice = privateLeasingForm.cleaned_data['monthly_price']
            leaseMilesPerYear = privateLeasingForm.cleaned_data['miles_per_year']
            leaseCar = car
            leaseCustomer = currentUser

            newPrivateLease = PrivateLease(leaseStartDate=leaseStartDate, leaseEndDate=leaseEndDate, leaseDownpayment=leaseDownpayment,
                                           leaseMonthlyPrice=leaseMonthlyPrice, leaseMilesPerYear=leaseMilesPerYear, leaseCar=leaseCar, leaseCustomer=leaseCustomer)

            newPrivateLease.save()

            car.carCurrentlyLeased = True
            car.save()

            return redirect("main:profile_page")

    return render(request=request,
                  template_name='main/privatecars/car_details.html',
                  context={'car': car,
                           'loginForm': LoginForm,
                           'username': request.user.username,
                           'registerUser': NewUserForm,
                           'registerProfile': RegisterProfileForm,
                           'privateLeasingForm': PrivateLeasingForm,
                           'today': todayFormatted,
                           'current_user': currentUser})


def profile_page(request):
    userCompanies = []
    if request.method == 'POST':
        # user = User.objects.get(id=user_id)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form.save()
        profile_form.save()
    elif request.method == 'GET':
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        userCompanies = Company.objects.filter(contactPerson=request.user.id)
    return render(request=request,
                  template_name='main/profile_page.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'privateLeases': PrivateLease.objects.filter(leaseCustomer=request.user),
                           'companyLeases': CompanyLease.objects.filter(leaseCustomerCompany__in=userCompanies),
                           'userCompanies': userCompanies,
                           'companyForm': CompanyForm})


def register_company(request):
    form = CompanyForm(request.POST)
    # print(form.errors.as_text())
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_text())
            messages.error(request, form.errors.as_data())

    return redirect('main:profile_page')


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
                   f"login failed, the login details provided wrong")
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

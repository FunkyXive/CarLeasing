from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets, ModelForm
from django.forms.widgets import TextInput, PasswordInput, DateInput
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'placeholder': 'Password'}))


class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilePhoneNumber', 'profileCprNumber',
                  'profileAddress', 'profileCity', 'profilePostalCode')


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user


class ContactForm(forms.Form):
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '10', 'style': 'resize: none; min-height: 100px'}), required=True)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilePhoneNumber', 'profileCprNumber',
                  'profileAddress', 'profileCity', 'profilePostalCode')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('contactPerson', 'companyName', 'companyAddress', 'companyCity',
                  'companyPostalCode', 'cvrNumber')


class PrivateLeasingForm(forms.Form):
    start_date = forms.DateField(required=True, widget=DateInput())
    end_date = forms.DateField(required=True)
    down_payment = forms.DecimalField(required=True)
    monthly_price = forms.DecimalField(required=True)
    miles_per_year = forms.IntegerField(required=True)
    car = forms.CharField(required=True)
    customer = forms.CharField(required=True)


class BusinessLeasingForm(forms.Form):
    start_date = forms.DateField(required=True, widget=DateInput())
    end_date = forms.DateField(required=True)
    down_payment = forms.DecimalField(required=True)
    monthly_price = forms.DecimalField(required=True)
    miles_per_year = forms.IntegerField(required=True)
    car = forms.CharField(required=True)
    company = forms.CharField()

from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("private_leasing", views.private_leasing, name="private_leasing"),
    path("business_leasing", views.business_leasing, name="business_leasing"),
    path("contact", views.contact, name="contact"),
    path("cars/<int:car_id>", views.car, name="car"),
]

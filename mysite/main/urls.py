from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register_company", views.register_company, name="register_company"),
    path("private_leasing", views.private_leasing, name="private_leasing"),
    path("business_leasing", views.business_leasing, name="business_leasing"),
    path("contact", views.contact, name="contact"),
    path("profilePage", views.profilePage, name="profilePage"),
    path("private_cars/<int:car_id>", views.private_car, name="private_cars"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("register", views.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

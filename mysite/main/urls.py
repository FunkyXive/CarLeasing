from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("private_leasing", views.private_leasing, name="private_leasing"),
    path("business_leasing", views.business_leasing, name="business_leasing"),
    path("contact", views.contact, name="contact"),
    path("profilePage", views.profilePage, name="profilePage"),
    path("cars/<int:car_id>", views.car, name="cars"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="root"),
    path("home/", views.home, name="home"),
    # path("profile/", views.profile, name="profile"),
    path("certifications/", views.certifications, name="certifications"),
    path("contact/", views.contact, name="contact"),
]

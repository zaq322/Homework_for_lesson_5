from django.urls import path
from .views import index, top_sellers, adver, register, login, profile, debug_method


urlpatterns = [
    path("", index, name="main-page"),
    path("top-seller/", top_sellers , name="top-sellers"),
    path("adver/", adver, name="advertisement-post"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("debug/", debug_method)
]
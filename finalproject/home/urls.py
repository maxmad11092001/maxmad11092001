from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name=("home")),
    path("login/", views.login, name=("login")),
    path("register/", views.register, name=("register")),
    path("admin/", views.admin, name=("admin")),
    path("customer/", views.customer, name=("customer")),
    path("history_rechard/", views.history_rechard, name=("history_rechard")),
    path("information/", views.information, name=("information")),
    path("listgame/", views.listgame, name=("listgame")),
    path("rechard/", views.rechard, name=("rechard")),
    path("news/", views.news, name=("news")),
    path("about/", views.about, name=("about")),
    path("service/", views.service, name=("service")),
    path("profile/", views.profile, name=("profile")),
]

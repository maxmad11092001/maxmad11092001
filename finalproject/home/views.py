from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "pages/home.html")


def login(request):
    return render(request, "pages/index.html")


def register(request):
    return render(request, "pages/register.html")


def admin(request):
    return render(request, "pages/admin.html")


def customer(request):
    return render(request, "pages/customer.html")


def history_rechard(request):
    return render(request, "pages/history_rechard.html")


def information(request):
    return render(request, "pages/information.html")


def listgame(request):
    return render(request, "pages/listgame.html")


def rechard(request):
    return render(request, "pages/rechard.html")


def news(request):
    return render(request, "pages/news.html")


def about(request):
    return render(request, "pages/about.html")


def service(request):
    return render(request, "pages/service.html")


def profile(request):
    return render(request, "pages/profile.html")

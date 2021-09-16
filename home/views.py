from django.shortcuts import render


def home(request):
    return render(request, "home/home.html")


def projects(request):
    return render(request, "home/projects.html")

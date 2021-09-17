from django.shortcuts import render


def home(request):
    return render(request, "home/home.html", {"title": "Home"})


def projects(request):
    return render(request, "home/projects.html", {"title": "Projects"})


def certifications(request):
    return render(request, "home/certifications.html", {"title": "Certifications"})


def contact(request):
    return render(request, "home/contact.html", {"title": "Contact"})

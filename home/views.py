from django.shortcuts import redirect, render
from .forms import MessageForm
from django.contrib import messages


def home(request):
    return render(request, "home/home.html", {"title": "Home"})


def projects(request):
    return render(request, "home/projects.html", {"title": "Projects"})


def certifications(request):
    return render(request, "home/certifications.html", {"title": "Certifications"})


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your message has been received.")
            return redirect("home")
    else:
        form = MessageForm()
    return render(
        request, "home/contact.html", {"title": "Contact", "form": MessageForm}
    )

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "main_app/home.html")

def about(request):
    context = {
        "title": "Über uns",
        "content": "Das ist eine Django WebApp Demonstration."
    }
    return render(request, "main_app/about.html", context)

def random(request):
    context = {
        "test": "test"
    }
    return render(request, "main_app/random.html", context)
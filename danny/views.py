from django.shortcuts import render

# Create your views here.
from danny.forms import registration


def homepage(request):
    return render(request, "homepage.html")


def index(request):
    student = registration()
    return render(request, "index.html",
                  {'form': student})

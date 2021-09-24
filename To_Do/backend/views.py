from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, "index.html", {})

def error_404(request, exception):
    return render(request, "404.html", {})
from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

def login(response):
    return render(response, "login.html", {"status": "invalid"})
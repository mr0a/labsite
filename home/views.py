from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(req):
    res = "<h1>Hello</h1>"
    res += "Login url: <a href='" + reverse('login') + "'>"+ "\n"
    res += "Logout url: " + reverse('logout') + "\n"
    return HttpResponse(res)
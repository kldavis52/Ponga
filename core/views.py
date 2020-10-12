from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Video, Comment

# Create your views here.


def landing_page(request):
    if request.user.is_authenticated:
        return render (request, 'landing_page.html')
    return render (request, 'landing_page.html')


def homepage(request):
    return render(request, "studiopal/homepage.html")

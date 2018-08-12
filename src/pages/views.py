from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse('<h1>Hello world!</h1>')


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse('<h1>Contact Page</h1>')


def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse('<h1>About Page</h1>')


def social_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return HttpResponse('<h1>Social Page</h1>')

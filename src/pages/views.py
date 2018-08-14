from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    my_context = {'my_text': 'This is a start page', 'my_title': 'Home Page'}
    return render(request, 'home.html', my_context)


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    my_context = {'my_text': 'Contact details can be found below', 'my_title': 'Contact details'}
    return render(request, 'contact.html', my_context)


def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    my_context = {'my_text': 'This is about us', 'my_title': 'About us'}
    return render(request, 'about.html', my_context)


def social_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    my_links = ('https://www.facebook.com/pkviatek', 'https://github.com/kviatek')
    my_context = {'my_text': 'Links to our social media can be found below', 'my_title': 'Social Media',
                  'links': my_links}
    return render(request, 'social.html', my_context)

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def features(request):
    return render(request, 'features.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def partners(request):
    return render(request, 'partners.html')


def report(request):
    return render(request, 'report.html')

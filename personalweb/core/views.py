from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


def portfolio(request):
    return render(request, 'core/portfolio.html')

def contacto(request):
    return render(request, 'core/contact.html')
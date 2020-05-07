from django.shortcuts import render

# Create your views here.
from portfolio.models import Project

def portfolio(request):
    projects    =   Project.objects.all()
    print('he', projects)
    return render(request, 'portfolio/portfolio.html', context={'projects':projects})
from django.shortcuts import render
from services.models import Service

# Create your views here.
def services(request):
    query   =   Service.objects.all()
    return render(request, 'services/services.html', {'query': query})
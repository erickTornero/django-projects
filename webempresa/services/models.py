from django.db import models

# Create your models here.

class ServiceModel(models.Model):
    title       =   models.CharField(max_length=200)
    subtitle    =   models.CharField(max_length=200)
    content     =   models.TextField()
    image       =   models.ImageField()
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)

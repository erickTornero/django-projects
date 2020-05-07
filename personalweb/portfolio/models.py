from django.db import models

# Create your models here.

class Project(models.Model):
    title       =   models.CharField(max_length=250)
    description =   models.TextField()
    image       =   models.ImageField(upload_to='projects')
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)
    learnmore   =   models.URLField(max_length=200, blank=True, null=True)


    
    def __str__(self):
        return self.title
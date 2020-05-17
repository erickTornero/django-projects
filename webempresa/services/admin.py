from django.contrib import admin

# Register your models here.
from services.models import ServiceModel

class ServiceModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ServiceModel, ServiceModelAdmin)
from django.contrib import admin
from social.models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', )

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='personal').exists():
            return ('created', 'updated', 'key', 'name') 
        else:
            return ('created', 'updated') 
admin.site.register(Link, LinkAdmin)
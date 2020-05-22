from django.contrib import admin
from pages.models import Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')
    list_editable   =   ('order', )
admin.site.register(Page, PageAdmin)
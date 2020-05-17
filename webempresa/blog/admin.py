from django.contrib import admin
from blog.models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =   ('created', 'updated')
    list_display    =   ('title', 'author', 'published', 'post_categorias')
    ordering        =   ('author', 'published')
    search_fields   =   ('title', 'content', 'categories__name')
    list_filter     =   ('author__username',)

    def post_categorias(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])

    post_categorias.short_description = 'Categories'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
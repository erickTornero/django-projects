from django.db import models
from django.utils.timezone import now
# Create your models here.
from django.contrib.auth.models import User

def post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'posts/{0}/{1}'.format(instance.title, filename)

class Category(models.Model):
    name        =   models.CharField(max_length=100)
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        =   'categoría'
        verbose_name_plural =   'categorías'
        ordering            =   ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title       =   models.CharField(max_length=255)
    content     =   models.TextField()
    published   =   models.DateTimeField(default=now)
    image       =   models.ImageField(upload_to=post_directory_path, null=True, blank=True)
    author      =   models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories  =   models.ManyToManyField(Category, verbose_name='categorías', related_name='get_posts')
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        =   'post'
        verbose_name_plural =   'posts'
        ordering            =   ['-created']

    def __str__(self):
        return self.title
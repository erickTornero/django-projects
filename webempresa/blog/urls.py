from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/category/<int:category_id>/', views.category, name='category')
]

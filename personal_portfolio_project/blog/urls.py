from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name='blog_mainpage'),
    path('post/<int:post_id>', views.post_page, name='post')
]

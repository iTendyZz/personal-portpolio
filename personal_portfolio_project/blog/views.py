from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def blog_page(request):
    posts = models.BlogApp.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_page(request, post_id):
    post = get_object_or_404(models.BlogApp, id=post_id)
    return render(request, 'blog/post.html', context={'post':post})
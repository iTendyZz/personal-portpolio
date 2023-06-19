from django.shortcuts import render
from . import models

# Create your views here.

def index_page(request):
    works = models.PortfolioProject.objects.all()
    return render(request, 'portfolio/index.html', context={"works": works})
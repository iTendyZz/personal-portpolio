from django.contrib import admin
from .models import PortfolioProject

# Register your models here.

admin.site.site_header = 'Админские настройки'

class PortfolioProjectEdit(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('url', 'title', 'id')
    search_fields = ('title', 'url', 'id', 'description')

admin.site.register(PortfolioProject, PortfolioProjectEdit)
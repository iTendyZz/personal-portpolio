from django.contrib import admin
from .models import BlogApp

# Register your models here.

admin.site.site_header = 'Админские настройки'

class BlogAppEdit(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'id', 'post')

admin.site.register(BlogApp, BlogAppEdit)
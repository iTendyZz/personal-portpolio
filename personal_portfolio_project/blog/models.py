from django.db import models
import datetime

# Create your models here.

class BlogApp(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    post = models.TextField(max_length=2000, verbose_name="Текст поста")
    media = models.ImageField(upload_to='blog/', verbose_name="Медиа")
    release_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edit_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title
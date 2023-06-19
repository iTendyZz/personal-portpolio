from django.db import models

# Create your models here.

class PortfolioProject(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    media = models.ImageField(upload_to='portfolio/', verbose_name="Медиа")
    url = models.URLField(verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тест'
    def __str__(self):
        return self.title

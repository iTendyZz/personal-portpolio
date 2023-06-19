# Generated by Django 4.2.2 on 2023-06-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('post', models.TextField(max_length=2000, verbose_name='Текст поста')),
                ('media', models.ImageField(upload_to='portfolio/', verbose_name='Медиа')),
                ('release_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-04 15:35

import core.logic.save_file
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/category', verbose_name='Изображение')),
                ('desc', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('sort', models.IntegerField(default=1, verbose_name='Сортировка')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.SlugField(unique=True, verbose_name='URL')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Тег новостей',
                'verbose_name_plural': 'Теги новостей',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('preview_title', models.CharField(max_length=100, verbose_name='Загловок (анонс)')),
                ('preview_image', models.ImageField(blank=True, null=True, storage=core.logic.save_file.UUIDFileStorage(), unique=True, upload_to='news/new__<django.db.models.fields.SlugField>/preview_images', verbose_name='Изображение (анонс)')),
                ('preview_desc', models.TextField(blank=True, null=True, verbose_name='Описание (анонс)')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, storage=core.logic.save_file.UUIDFileStorage(), unique=True, upload_to='news/new__<django.db.models.fields.SlugField>/images', verbose_name='Изображение')),
                ('desc', models.TextField(verbose_name='Контент')),
                ('view', models.IntegerField(default=0, verbose_name='Счётчик просмотров')),
                ('sort', models.IntegerField(default=1, verbose_name='Сортировка')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.NewsCategory', verbose_name='Категория')),
                ('tag', models.ManyToManyField(blank=True, to='core.NewsTag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='NewsView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.News', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Просмотренная новость',
                'verbose_name_plural': 'Просмотренные новости',
                'unique_together': {('user', 'new')},
            },
        ),
        migrations.CreateModel(
            name='NewsLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.News', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Понравившаяся новость',
                'verbose_name_plural': 'Понравившаяся новость',
                'unique_together': {('user', 'new')},
            },
        ),
        migrations.CreateModel(
            name='NewsBookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.News', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Закладка новостей',
                'verbose_name_plural': 'Закладки новостей',
                'unique_together': {('user', 'new')},
            },
        ),
    ]

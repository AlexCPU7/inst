# Generated by Django 2.2.1 on 2019-05-16 17:15

import core.logic.save_file
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StickerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.SlugField(unique=True, verbose_name='URL')),
                ('desc', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, storage=core.logic.save_file.UUIDFileStorage(), unique=True, upload_to='shop/images/tag__<django.db.models.fields.SlugField>', verbose_name='Изображение')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Тег новостей',
                'verbose_name_plural': 'Теги новостей',
            },
        ),
        migrations.CreateModel(
            name='TagProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.SlugField(unique=True, verbose_name='URL')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Тег новостей',
                'verbose_name_plural': 'Теги новостей',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('model_number', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Артикул')),
                ('active', models.BooleanField(default=1, verbose_name='Активность')),
                ('desc', models.TextField(blank=True, max_length=50000, null=True, verbose_name='Описание')),
                ('image_main', models.ImageField(blank=True, null=True, storage=core.logic.save_file.UUIDFileStorage(), unique=True, upload_to='shop/product/<django.db.models.fields.SlugField>/image_main', verbose_name='Главное изображение')),
                ('sort', models.IntegerField(default=1, verbose_name='Сортировка')),
                ('length', models.PositiveIntegerField(blank=True, null=True, verbose_name='Длинна')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Вес')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Цена, руб')),
                ('price_procurement', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1.0)], verbose_name='Цена закупки, руб')),
                ('meta_tag_title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Мета-тег title')),
                ('meta_tag_h1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Мета-тег H1')),
                ('meta_tag_description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Мета-тег description')),
                ('meta_tag_keywords', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Мета-тег keywords')),
                ('meta_tag_robots', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Мета-тег robots')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Category', verbose_name='Категория')),
                ('sticker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.StickerProduct', verbose_name='Стикеры')),
                ('tag', models.ManyToManyField(blank=True, to='shop.TagProduct', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]

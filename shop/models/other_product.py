from uuid import uuid4
from time import time

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.html import format_html

from shop.models.catalog import Category


class TagProduct(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    url = models.SlugField(_('URL'), max_length=50, unique=True)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Тег товара')
        verbose_name_plural = _('Теги товаров')

    def __str__(self):
        return self.title


def upload_path_handler_sticker_product(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    file_name = '{}_{}{}'.format(uuid4().hex, int(time()), ext)
    return "shop/stickers/{}/images/{}".format(instance.url, file_name)


class StickerProduct(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    url = models.SlugField(_('URL'), max_length=50, unique=True)
    desc = models.TextField(_('Описание'), blank=True, null=True, max_length=5000)
    image = models.ImageField(_('Изображение'),
                              upload_to=upload_path_handler_sticker_product,
                              unique=True, blank=True, null=True)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Стикер товара')
        verbose_name_plural = _('Стикеры товаров')

    def __str__(self):
        return self.title

    def image_tag(self):
        image_tag = format_html(
            '<img src=/media/{} height="150" />'.format(self.image)
        )
        return image_tag if self.image else '-'
    image_tag.short_description = 'Изоражение'

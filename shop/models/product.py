from uuid import uuid4
from time import time

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.html import format_html

from shop.models.catalog import Category
from shop.models.other_product import TagProduct, StickerProduct


def upload_path_handler_product(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    file_name = '{}_{}{}'.format(uuid4().hex, int(time()), ext)
    return "shop/products/{}/images/{}".format(instance.url, file_name)


class Product(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    model_number = models.PositiveIntegerField(_('Артикул'), unique=True,
                                               blank=True, null=True)
    active = models.BooleanField(_('Активность'), default=1)
    category = models.ForeignKey(Category, verbose_name=_('Категория'),
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    # is_active_category
    # сезон мб
    # производитель мб
    desc = models.TextField(_('Описание'), blank=True, null=True, max_length=50000)
    image_main = models.ImageField(_('Главное изображение'),
                                   upload_to=upload_path_handler_product,
                                   unique=True, blank=True, null=True)

    price = models.DecimalField(_('Цена, руб'), max_digits=12, decimal_places=2,
                                validators=[MinValueValidator(1.00)])
    price_procurement = models.DecimalField(_('Цена закупки, руб'),
                                            max_digits=12, decimal_places=2,
                                            validators=[MinValueValidator(1.00)])

    tag = models.ManyToManyField(TagProduct, verbose_name=_('Теги'), blank=True)
    sticker = models.ForeignKey(StickerProduct, verbose_name=_('Стикеры'),
                                blank=True, null=True,
                                on_delete=models.SET_NULL)

    length = models.PositiveIntegerField(_('Длинна'), blank=True, null=True)
    width = models.PositiveIntegerField(_('Ширина'), blank=True, null=True)
    height = models.PositiveIntegerField(_('Высота'), blank=True, null=True)
    weight = models.PositiveIntegerField(_('Вес'), blank=True, null=True)

    sort = models.IntegerField(_('Сортировка'), default=1)

    meta_tag_title = models.CharField(_('Мета-тег title'), max_length=500,
                                      blank=True, null=True)
    meta_tag_h1 = models.CharField(_('Мета-тег H1'), max_length=500, blank=True, null=True)
    meta_tag_description = models.CharField(_('Мета-тег description'), max_length=2000,
                                            blank=True, null=True)
    meta_tag_keywords = models.CharField(_('Мета-тег keywords'), max_length=2000,
                                         blank=True, null=True)
    meta_tag_robots = models.CharField(_('Мета-тег robots'), max_length=2000,
                                       blank=True, null=True)

    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return self.title

    def image_tag(self):
        image_tag = format_html(
            '<img src=/media/{} height="150" />'.format(self.image_main)
        )
        return image_tag if self.image_main else '-'
    image_tag.short_description = 'Главное изоражение'

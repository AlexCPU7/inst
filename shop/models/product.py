from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

from shop.models.catalog import Category


class Product(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    artikul(unique=True)
    active = models.BooleanField(_('Активность'), default=1)
    category = models.ForeignKey(Category, verbose_name=_('Категория'),
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    is_active_category
    сезон мб
    производитель мб
    desc = models.TextField(_('Описание'), blank=True, null=True, max_length=50000)
    # image = models.ImageField(_('Изображение'), upload_to='shop/category', blank=True, null=True)
    sort = models.IntegerField(_('Сортировка'), default=1)

    tag
    sticker

    length
    width
    height
    weight gram

    price = models.DecimalField(_('Цена, руб'), max_digits=12, decimal_places=2,
                                validators=MinValueValidator(1.00))
    price_procurement = models.DecimalField(_('Цена закупки, руб'), max_digits=12, decimal_places=2,
                                            validators=MinValueValidator(1.00))

    meta_tag_title = models.CharField(_('Мета-тег title'), max_length=500, blank=True, null=True)
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

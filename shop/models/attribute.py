from uuid import uuid4
from time import time

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.html import format_html

from shop.models.catalog import Category

group_types = (
    ('info', 'Характеристика'),
    ('offer', 'Коммерческое предложение')
)


class Group(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    category = models.ForeignKey(Category,
                                 verbose_name=_(u'Категория'),
                                 on_delete=models.SET_NULL,
                                 null=True)
    type = models.CharField('Тип', choices=group_types, max_length=20)
    is_filter = models.BooleanField(_('Активность в фильтре'), default=1)
    desc = models.TextField(_('Описание'), blank=True, null=True)

    class Meta:
        verbose_name = _('Группа атрибутов')
        verbose_name_plural = _('Группы атрибутов')

    def __str__(self):
        return self.title


class Attribute(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    group = models.ForeignKey(Group,
                              verbose_name=_(u'Группа атрибутов'),
                              on_delete=models.CASCADE)
    is_filter = models.BooleanField(_('Активность в фильтре'), default=1)

    class Meta:
        verbose_name = _('Группа атрибутов')
        verbose_name_plural = _('Группы атрибутов')

    def __str__(self):
        return self.title


class Offer(models.Model):
    # недоделанно
    # TODO связать группу/атрибуты/и ком. предложения
    offer = 1
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

# TODO отдельно связать атрибуты и товары по типу info

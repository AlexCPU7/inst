from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html


class Category(models.Model):
    """
    Product category.
    Sorting starts from the larger "sort"
    """
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    active = models.BooleanField(_('Активность'), default=1)
    parent_category = models.ForeignKey('self', verbose_name=_('Родительская категория'),
                                        on_delete=models.SET_NULL, blank=True, null=True)
    desc = models.TextField(_('Описание'), blank=True, null=True, max_length=3000)
    image = models.ImageField(_('Изображение'), upload_to='shop/category', blank=True, null=True)
    sort = models.IntegerField(_('Сортировка'), default=1)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title

    def image_tag(self):
        image_tag = format_html('<img src=/media/{} width="150" height="150" />'.format(self.image))
        return image_tag if self.image else '-'
    image_tag.short_description = 'Изображение'

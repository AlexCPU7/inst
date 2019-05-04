from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class NewsTag(models.Model):
    """
    Tags for News
    """
    title = models.CharField(_('Название'), max_length=50)
    url = models.SlugField(_('URL'), max_length=50, unique=True)
    active = models.BooleanField(_('Активность'), default=1)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Тег новостей')
        verbose_name_plural = _('Теги новостей')

    def __str__(self):
        return self.title


class NewsCategory(models.Model):
    """
    Category for news
    """
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    active = models.BooleanField(_('Активность'), default=1)
    image = models.ImageField(_('Изображение'), upload_to='news/category', blank=True, null=True)
    desc = models.TextField(_('Описание'), max_length=3000, blank=True, null=True)
    sort = models.IntegerField(_('Сортировка'), default=1)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Категория новостей')
        verbose_name_plural = _('Категории новостей')

    def __str__(self):
        return self.title

    def image_tag(self):
        image_tag = format_html(
            '<img src=/media/{} height="150" />'.format(self.image)
        )
        return image_tag if self.image else '-'

    image_tag.short_description = 'Изображение'

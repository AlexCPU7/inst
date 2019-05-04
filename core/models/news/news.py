from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from core.logic.save_file import UUIDFileStorage
from core.models.news.attribute_news import NewsCategory, NewsTag


class News(models.Model):
    """
    News
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=_('Автор поста'),
                               null=True,
                               default=1,
                               on_delete=models.SET_NULL)
    active = models.BooleanField(_('Активность'), default=1)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    category = models.ForeignKey(NewsCategory,
                                 verbose_name=_('Категория'),
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)

    preview_title = models.CharField(_('Загловок (анонс)'), max_length=100)
    preview_image = models.ImageField(_('Изображение (анонс)'),
                                      upload_to='news/new__{}/preview_images'.format(url),
                                      storage=UUIDFileStorage(),
                                      unique=True,
                                      blank=True, null=True)
    preview_desc = models.TextField(_('Описание (анонс)'), blank=True, null=True)

    title = models.CharField(_('Заголовок'), max_length=100)
    image = models.ImageField(_('Изображение'),
                              upload_to='news/new__{}/images'.format(url),
                              storage=UUIDFileStorage(),
                              unique=True,
                              blank=True, null=True)
    desc = models.TextField(_('Контент'))

    tag = models.ManyToManyField(NewsTag, verbose_name=_('Теги'), blank=True)
    view = models.IntegerField(_('Счётчик просмотров'), default=0)
    sort = models.IntegerField(_('Сортировка'), default=1)

    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title

    def image_tag(self):
        image_tag = format_html(
            '<img src=/media/{} height="150" />'.format(self.image)
        )
        return image_tag if self.image else '-'
    image_tag.short_description = 'Изображение'

    def preview_image_tag(self):
        image_tag = format_html(
            '<img src=/media/{} height="150" />'.format(self.preview_image)
        )
        return image_tag if self.preview_image else '-'
    preview_image_tag.short_description = 'Изображение (анонс)'

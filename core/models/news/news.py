from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class NewsTag(models.Model):
    """
    Tags for News
    """
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
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
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Категория новостей')
        verbose_name_plural = _('Категории новостей')

    def __str__(self):
        return ''


class News(models.Model):
    """
    News
    """
    # preview
    title = models.CharField(_('Название'), max_length=100)
    url = models.SlugField(_('URL'), max_length=100, unique=True)
    active = models.BooleanField(_('Активность'), default=1)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title


class NewsComment(models.Model):
    """
    Comments under the news
    """

    class Meta:
        verbose_name = _('Комментарий к новости')
        verbose_name_plural = _('Комментарии к новости')

    def __str__(self):
        return ''


class NewsLike(models.Model):
    """
    User liked the news
    """
    class Meta:
        verbose_name = _('Понравивщаяся новость')
        verbose_name_plural = _('Понравившаяся новость')

    def __str__(self):
        return ''


class NewsBookmarks(models.Model):
    """
    User have bookmarked the news
    """
    class Meta:
        verbose_name = _('Закладка новостей')
        verbose_name_plural = _('Закладки новостей')

    def __str__(self):
        return ''


class NewsView(models.Model):
    """
    User looked at the news
    """
    class Meta:
        verbose_name = _('Просмотренная новость')
        verbose_name_plural = _('Просмотренные новости')

    def __str__(self):
        return ''

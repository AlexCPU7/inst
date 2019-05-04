from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from core.models.news.news import News


class NewsView(models.Model):
    """
    User looked at the news
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_('Пользователь'),
                             on_delete=models.CASCADE)
    new = models.ForeignKey(News, verbose_name=_('Новость'), on_delete=models.CASCADE)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'new')
        verbose_name = _('Просмотренная новость')
        verbose_name_plural = _('Просмотренные новости')

    def __str__(self):
        return _('Пользователь "{}" просмотрел новость: {}'.format(self.user, self.new))


class NewsLike(models.Model):
    """
    User liked the news
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_('Пользователь'),
                             on_delete=models.CASCADE)
    new = models.ForeignKey(News, verbose_name=_('Новость'), on_delete=models.CASCADE)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'new')
        verbose_name = _('Понравившаяся новость')
        verbose_name_plural = _('Понравившаяся новость')

    def __str__(self):
        return _('Пользователю "{}" понравилась новость: {}'.format(self.user, self.new))


class NewsBookmarks(models.Model):
    """
    User have bookmarked the news
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_('Пользователь'),
                             on_delete=models.CASCADE)
    new = models.ForeignKey(News, verbose_name=_('Новость'), on_delete=models.CASCADE)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'new')
        verbose_name = _('Закладка новостей')
        verbose_name_plural = _('Закладки новостей')

    def __str__(self):
        return _('Пользователь "{}" добавил в закладки новость: {}'.format(self.user, self.new))

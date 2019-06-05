from uuid import uuid4
from time import time

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils.html import format_html

from core.models.user import User


class TagImage(models.Model):
    title = models.CharField(_('Тег'), max_length=30)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)


class Images(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Пользватель'))
    image = models.ImageField(_('Изображение'), upload_to='image/image', unique=True)
    desc = models.TextField(_('Описание'), blank=True, null=True, max_length=5000)
    is_public = models.BooleanField(_('Публичный'), default=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)
    # TODO само собой доделать
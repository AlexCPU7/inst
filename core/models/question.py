from django.db import models
from django.utils.translation import ugettext as _


class QuestionGroup(models.Model):
    title = models.CharField(_('Название'), max_length=100)
    active = models.BooleanField(_('Активность'), default=1)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Группа вопросов')
        verbose_name_plural = _('Группы вопросов')

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(_('Вопрос'), max_length=255)
    answer = models.TextField(_('Ответ'), max_length=3000)
    active = models.BooleanField(_('Активность'), default=1)
    group = models.ForeignKey(QuestionGroup, verbose_name=_('Группа'), on_delete=models.SET_NULL,
                              blank=True, null=True)
    create_dt = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Дата изменения'), auto_now=True)

    class Meta:
        verbose_name = _('Вопрос-ответ')
        verbose_name_plural = _('Вопрос-ответ')

    def __str__(self):
        return self.question

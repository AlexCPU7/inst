from django.db import models
# ticket


class Help(models.Model):
    title = models.CharField('Вопрос', max_length=255)

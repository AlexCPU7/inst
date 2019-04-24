from django.contrib import admin
from core.models.question import (Question,
                                  QuestionGroup)

admin.site.register(QuestionGroup)
admin.site.register(Question)

from django.contrib import admin

from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_test', 'question_type', 'poll')


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'poll_name', 'description_poll','start_date', 'end_date',)
    search_fields = ('poll_name', 'description_poll')


@admin.register(Answer)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_by','answer_text',)
    search_fields = ('question', 'answer_by')

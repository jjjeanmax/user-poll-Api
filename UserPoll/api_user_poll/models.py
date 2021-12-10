from django.db import models

from auth.models import Userauth
from .enums import TypeQuestions


class Poll(models.Model):
    poll_name = models.CharField(verbose_name='название опроса', max_length=255)
    description_poll = models.TextField(verbose_name='описание опроса')
    start_date = models.DateField(verbose_name='дата старта', auto_now_add=True, editable=False)
    end_date = models.DateField(verbose_name='дата окончания')

    def __str__(self):
        return self.poll_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question_test = models.TextField(verbose_name='текст вопроса', max_length=255)
    question_type = models.CharField(max_length=50, verbose_name='тип вопроса ',
                                     choices=TypeQuestions,
                                     default=TypeQuestions[0]
                                     )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return self.question_test

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer_by = models.ForeignKey(Userauth, on_delete=models.CASCADE)
    answer_text = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return f'Вопрос: {self.question} был ответен пользователем с ID: {self.answer_by}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

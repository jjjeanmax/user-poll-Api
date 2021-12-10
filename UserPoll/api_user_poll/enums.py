from django.db import models

RESPONSE_WITH_TEXT = 'ответ текстом'
SINGLE_CHOICE_ANSWER = 'ответ с выбором одного варианта'
ANSWER_WITH_MULTIPLE_OPTIONS = 'ответ с выбором нескольких вариантов'

TypeQuestions = [
    (RESPONSE_WITH_TEXT, 'ответ текстом'),
    (SINGLE_CHOICE_ANSWER, 'ответ с выбором одного варианта'),
    (ANSWER_WITH_MULTIPLE_OPTIONS, 'ответ с выбором нескольких вариантов')
]

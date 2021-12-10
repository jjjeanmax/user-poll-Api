from django.urls import path, include

from api_user_poll.views import (DeletePollView,
                                 CreatePollView,
                                 DeleteQuestionView,
                                 CreateQuestionView,
                                 GetActivPollView,
                                 GetUserAnswer,
                                 UpdatePollView,
                                 UpdateQuestionView)
qt = 'question'
pl = 'poll'
us = 'user'

urlpatterns = [

    path(f'{pl}/<id>/delete-poll/', DeletePollView.as_view(), name='DeletePoll'),
    path(f'{pl}/create-poll/', CreatePollView.as_view(), name='CreatePoll'),
    path(f'{pl}/update-poll/<int:pk>/', UpdatePollView.as_view(), name='UpdatePoll'),

    path(f'{qt}/delete-question/<id>', DeleteQuestionView.as_view(), name='DeleteQuestion'),
    path(f'{qt}/create-question/', CreateQuestionView.as_view(), name='CreateQuestion'),
    path(f'{qt}/update-question/<int:pk>/', UpdateQuestionView.as_view(), name='UpdateQuestion'),

    path(f'{us}/answers/<int:pk>/', GetUserAnswer.as_view(), name='user_answer'),
    path(f'{us}/activ-polls', GetActivPollView.as_view(), name='activ_polls'),

]

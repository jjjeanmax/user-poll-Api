import datetime

from django.db.models import F
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    DestroyAPIView,
    CreateAPIView,
)

from api_user_poll.models import Poll, Answer, Question
from api_user_poll.authentication import ApiClientAuthentication
from api_user_poll.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, UpdatePollSerializer, \
    UpdateQuestionSerializer


class DeletePollView(DestroyAPIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    lookup_field = 'id'
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class CreatePollView(CreateAPIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class UpdatePollView(APIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def put(request, pk, format=None):

        qs = Poll.objects.get(id =pk)
        serializer = UpdatePollSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteQuestionView(DestroyAPIView):
    lookup_field = 'id'
    queryset = Question.objects.all()
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer


class CreateQuestionView(CreateAPIView):
    queryset = Question.objects.all()
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer


class UpdateQuestionView(APIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def put(request, pk, format=None):

        try:
            qs = Question.objects.get(id =pk)
        except Question.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateQuestionSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetActivPollView(APIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        qs = Poll.objects.values('poll_name', 'description_poll', 'start_date', 'end_date').filter(
            end_date__lte=datetime.date.today())
        resp_list = []
        for ans in qs:
            resp_list.append({
                'poll_name': ans['poll_name'],
                'description_poll': ans['description_poll'],
                'start_date': ans['start_date'],
                'end_date': ans['end_date'],
            })
        serializer = PollSerializer(data=resp_list, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)


class GetUserAnswer(APIView):
    authentication_classes = (ApiClientAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, pk):
        qs = Answer.objects.values('answer_text', Question=F('question__question_test'),
                                   answerBy=F('answer_by__user_id')).filter(answer_by__user_id=pk)
        resp_list = []
        for ans in qs:
            resp_list.append({
                'question': ans['Question'],
                'answer_by': ans['answerBy'],
                'answer_text': ans['answer_text'],
            })
        serializer = AnswerSerializer(data=resp_list, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

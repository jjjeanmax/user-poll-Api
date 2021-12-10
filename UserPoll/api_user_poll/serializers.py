from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Poll, Question, Answer


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'poll_name',
            'description_poll',
            'end_date',
        ]


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'question_test',
            'question_type',
            'poll',
        ]


class AnswerSerializer(serializers.Serializer):
    question = serializers.CharField()
    answer_by = serializers.CharField()
    answer_text = serializers.CharField()

    class Meta:
        model = Answer
        fields = '__all__'


class UpdatePollSerializer(ModelSerializer):
    poll_name = serializers.CharField(required=False)
    description_poll = serializers.CharField(required=False)
    end_date = serializers.DateField(required=False)

    class Meta:
        model = Poll
        fields = [
            'poll_name',
            'description_poll',
            'end_date',
        ]


class UpdateQuestionSerializer(ModelSerializer):
    question_test = serializers.CharField(required=False)
    question_type = serializers.CharField(required=False)
    poll = serializers.CharField(required=False)

    class Meta:
        model = Poll
        fields = [
            'question_test',
            'question_type',
            'poll',
        ]

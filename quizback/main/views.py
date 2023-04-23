from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from main.models import Quiz, Question
from main.serializers import QuizSerializer, QuestionSerializer


class Test(APIView):

    def get(self, request, format=None):
        return JsonResponse({"result": 123})


class QuizList(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    # queryset = Question.objects.all()

    def get_queryset(self):
        params = self.request.query_params
        return Question.objects.filter(quiz_id=params.get('quiz_id')) \
                   .order_by('?')[:int(params.get('questionsInQuiz', 10))]

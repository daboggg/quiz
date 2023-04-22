from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from main.models import Quiz
from main.serializers import QuizSerializer


class Test(APIView):

    def get(self, request, format=None):
            return JsonResponse({"result":123})


class QuizList(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    # pagination_class = CompanyListPagination

    # def get_queryset(self):
    #     params = self.request.query_params
    #     return Quiz.objects.filter(name=).order_by('id')

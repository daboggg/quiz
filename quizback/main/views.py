from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


class Test(APIView):

    def get(self, request, format=None):
            return JsonResponse({"result":123})

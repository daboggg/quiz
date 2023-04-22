from django.urls import path

from main.views import *

urlpatterns = [
    path('test/', Test.as_view()),
    path('quizs/', QuizList.as_view()),
    path('questions/', QuestionList.as_view()),
    # path('dividends/<int:pk>/', DividendDetail.as_view()),
    # path('dividends/', DividendList.as_view()),
    # path('dividend_history/', dividendHistory),
    # path('dividends_for_chart/', DividendListForChart.as_view()),
]
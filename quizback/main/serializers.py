from rest_framework import serializers

from main.models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','name']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','text','is_right']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # company = CompanySerializer()
    # company = serializers.PrimaryKeyRelatedField(read_only=True)
    # currency = CurrencySerializer()
    # account = AccountSerializer()

    class Meta:
        model = Question
        fields = '__all__'
        # fields = ['id','date_of_receipt', 'company', 'currency',
        #           'payoff', 'date_of_receipt', 'account','user']
        depth = 1
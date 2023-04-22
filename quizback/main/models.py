from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100, verbose_name='Текст темы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    text = models.CharField(max_length=300, verbose_name='Текст Вопроса')
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, verbose_name='Тема')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.CharField(max_length=500, verbose_name='Текст ответа')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, verbose_name='Вопрос')
    is_right = models.BooleanField(default=False, verbose_name='Правильный ответ?')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'




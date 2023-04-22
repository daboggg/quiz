from django.contrib import admin

from main.models import Quiz, Question, Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'quiz')
#     list_display_links = ('quiz','text')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'is_right')
    list_display_links = ('text','question')


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz')
    list_display_links = ('quiz','text')
    inlines = [AnswerInLine,]


# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('company',)
#     search_fields = ('company',)
#     list_filter = ('date_of_receipt',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

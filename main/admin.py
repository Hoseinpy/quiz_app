from django.contrib import admin
from .models import QuizModel, CustomUser


@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['ip']

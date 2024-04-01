from django.urls import path, include
from .views import QuizAppView


urlpatterns = [
    path('', QuizAppView.as_view(), name='quiz-page')
]

from django.db import models
from django.contrib.auth.models import AbstractUser


class QuizModel(models.Model):
    question = models.CharField(max_length=100)
    current_answer = models.CharField(max_length=50)
    wrong_answer_1 = models.CharField(max_length=50)
    wrong_answer_2 = models.CharField(max_length=50)
    wrong_answer_3 = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.question 


class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)
    ip = models.CharField(max_length=20, default='0.0.0.0')
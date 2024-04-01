import random
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import QuizModel, CustomUser
from django.utils.crypto import get_random_string


@method_decorator(csrf_exempt, name='dispatch')
class QuizAppView(View):
    
    def get_user(self):
        ip = self.request.META.get('REMOTE_ADDR')
        user = CustomUser.objects.filter(ip=ip).first()
        return user

    def get_quiz(self):
        quiz = QuizModel.objects.all().first()
        return quiz

    def get_quiz_answer(self):
        if quiz := self.get_quiz():
            list_of_question = [quiz.current_answer, quiz.wrong_answer_1,
                                    quiz.wrong_answer_2, quiz.wrong_answer_3]
            random.shuffle(list_of_question)
            return list_of_question

    def get(self, request):
        # get user or create user with user system ip
        user = self.get_user()
        if user is None:
            username = get_random_string(8)
            ip = self.request.META.get('REMOTE_ADDR')
            user = CustomUser.objects.create(ip=ip, username=username)
            score = user.score

        score = user.score
        quiz = self.get_quiz()
        return render(request, 'main/quiz_page.html', {'q':quiz, 'answers':self.get_quiz_answer(), 'score':score, 'error':'no question'})

    def post(self, request: HttpRequest):
        user_answer = request.POST.get('user_answer')
        quiz = QuizModel.objects.filter(current_answer=user_answer)
        if quiz:
            user = self.get_user()
            user.score += 1
            user.save()
            quiz.delete()
            return redirect('quiz-page')

        return redirect('quiz-page')
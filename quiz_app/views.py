from django.shortcuts import render, redirect
from .forms import AddQuestionform
from .models import QuesModel
import time
import datetime
from django.contrib import messages
# Create your views here.
from .forms import AddQuestionform


def instructions(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'Quiz/instructions.html')


def home(request):
    if request.method == 'POST':
        questions = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        print(questions)
        for q in questions:
            total += 1

            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        print(context)
        return render(request, 'Quiz/result.html', context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)


def add_question(request):
    if request.user.is_staff:
        form = AddQuestionform()
        if request.method == 'POST':
            print(request.POST)
            form = AddQuestionform(request.POST)
            # print(form)
            op1 = request.POST.get('op1')
            op2 = request.POST.get('op2')
            op3 = request.POST.get('op3')
            op4 = request.POST.get('op4')
            ans = request.POST.get('ans')
            if form.is_valid():
                print("form valid")
                if (op1 != (op2 or op3 or op4)) and (op2 != (op3 or op4)) \
                        and (op3 != op4):
                    if QuesModel.objects.all().count() < 10:
                        print("in if 2")
                        form.save()
                    else:
                        messages.error(request, 'You can only add 10 questions in quiz')

                else:
                    messages.error(request, 'Each option should be unique, please try again')
                    context = {'form': form}
                    return render(request, 'Quiz/addQuestion.html', context)

                return redirect('home')

        context = {'form': form}
        print(context)
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')


def delete_question(request):
    if request.user.is_staff:
        print(request.POST)
        pk = request.POST.get("id")
        print(pk)
        questions = QuesModel.objects.all()
        QuesModel.objects.filter(id=pk).delete()
        context = {'questions': questions}
    return render(request, 'Quiz/delete_question.html', context)


def countdown(m):
    total_seconds = m * 60
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

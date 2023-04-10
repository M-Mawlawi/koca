from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from .models import Question,Exam,Answers,SlideShow
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    slideshow_obj = SlideShow.objects.all()
    context['slideshow'] = slideshow_obj
    return render(request,"index.html",context)

@login_required
def exam_redirect(request):
    questions = Question.objects.order_by('?')
    cache.set('questions', questions,3000)
    exam = Exam(user_id = request.user)
    exam.save()
    cache.set('exam_id', exam.id,6000)
    answered = dict.fromkeys(range(1,51))
    cache.set('answered', answered,3000)

    if request.user.users.expire < datetime.now():
        return render(request,"expired.html")
    else:
        return redirect('/exam/1')


@csrf_exempt
def exam(request,quest_no):
    # Check Session
    questions = cache.get('questions')
    if not questions:
        return redirect("index")

    context = {}
    questions = Paginator(questions,1)
    question = questions.get_page(quest_no)
    context['question'] = question

    exam_id = cache.get('exam_id')
    exam = Exam.objects.get(id = exam_id)
    context['created_at'] = (exam.created_at + timedelta(minutes=45)).strftime("%b %d, %Y %H:%M:%S")
    question_id = Question.objects.get(id = question[0].id)
    context['id'] = question[0].id
    try:
        sel_answer = Answers.objects.get(exam_id=exam,question_id = question_id)
        context['selected'] = sel_answer
    except:
        pass


    if request.POST:
        sent_answer = request.POST.get('answer')
        page = request.POST.get('page')
        id = request.POST.get('id')
        if id and sent_answer and page:
            q_id = Question.objects.get(id = id)

            answer = Answers.objects.filter(exam_id=exam,question_id = q_id)

            if answer:
                Answers.objects.filter(exam_id=exam,question_id = q_id).update(answer = sent_answer)
            else:
                answer = Answers(exam_id=exam,question_id = q_id,answer = sent_answer)
                answer.save()
                
            answer = Answers.objects.filter(exam_id=exam,question_id = q_id)

            if answer:
                answer = answer[0]

            context['selected'] = answer
            
            answered = cache.get('answered')
            if answered:
                answered.update({int(page):sent_answer})
            else:
                answered = {
                    page:sent_answer,
                }
                answered[1] = sent_answer
            cache.set('answered', answered,3000)
        if request.POST.get('exit'):
            return redirect("resault")
    
    context['answered'] = cache.get('answered')
    return render(request,"exam.html",context)


def resault(request):
    context = {}
    exam_id = cache.get('exam_id')
    if not exam_id:
        return redirect("index")
    answers = Answers.objects.filter(exam_id = exam_id)
    score = 0
    for answer in answers:
        if answer.answer == answer.question_id.t_answer:
            score += 2

    Exam.objects.filter(user_id = request.user,id=exam_id).update(score = score)
    cache.delete_many(['questions'])
    context['answers'] = answers
    context['resault'] = score
    return render(request,"resault.html",context)
    
@csrf_exempt
def signup(request):
    form = SignupForm()
    if request.POST:
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            raw_password = signupform.cleaned_data.get('password1')
            raw_username = signupform.cleaned_data.get('username')
            user = authenticate(request,username = raw_username,password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,signupform.non_field_errors())
            return redirect('signup')
    else:
        return render(request,'signup.html',{'form':form})

@csrf_exempt
def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,"error")
    return render(request,'login.html')

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')

def contact(request):
    return render(request,'contact.html')
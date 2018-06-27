# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer
from .forms import AskForm, AnswerForm, SignupForm, LoginForm

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    new_questions_list = Question.objects.new()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(new_questions_list, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def popular(request):
    popular_questions_list = Question.objects.popular()
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(popular_questions_list, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers_list = Answer.objects.filter(question_id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        # if user reaches the route via GET - by opening a question
        form = AnswerForm(initial={'question': question_id})

    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': answers_list,
        'form': form,
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        # if user reaches the route via GET - by creating a new question
        form = AskForm()
    return render(request, 'qa/ask_form.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            #TODO
            # must implement new user registration here
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            url = reverse('index')
            return HttpResponseRedirect(url)
    else:
        # if user reaches via GET - show form
        form = SignupForm()
        #form = UserCreationForm()
    return render(request, 'qa/signup_form.html', {'form': form})

def signin(request):
    messages = []
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                url = reverse('index')
                return HttpResponseRedirect(url)
            else:
                messages.append("Incorrent username or password")
    else:
        form = LoginForm()
    return render(request, 'qa/login_form.html', {'form': form, 'messages': messages})

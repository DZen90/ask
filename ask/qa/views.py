# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer

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
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': answers_list,
    })


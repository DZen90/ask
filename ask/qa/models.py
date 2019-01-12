# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.order_by('-added_at') # return latest added question

    def popular(self):
        return Question.objects.order_by('-rating') # return the most popular questions
    def search(self, query):
        return Question.objects.filter(title__icontains = query) # return questions whose title matches search query

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question-details', kwargs={'question_id': self.id})

class Answer(models.Model):
    text = models.CharField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

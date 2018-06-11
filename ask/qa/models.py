# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new():
        return Question.objects.order_by('-added_at') # return latest added question

    def popular():
        return Question.objects.order_by('-rating') # return the most popular questions

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.CharField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

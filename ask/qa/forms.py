from django import forms

from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(max_length=1000)
    
    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 121 # Random user for test
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=1000)
    question_id = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = 121 # Random user for test
        answer.save()
        return answer

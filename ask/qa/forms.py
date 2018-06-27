from django import forms
from django.core.exceptions import ValidationError
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(max_length=1000)
    
    def save(self):
        #question = Question(**self.cleaned_data)
        #question.author_id = 121  Random user for test, CHANGE IF new database
        #question.save()
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=1000)
    #question = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.HiddenInput())

    def save(self):
        #answer = Answer(**self.cleaned_data)
        #nswer.author_id = 121  Random user for test, CHANGE IF new database
        #answer.save()
        self.cleaned_data['author'] = self._user
        return Answer.objects.create(**self.cleaned_data)

class SignupForm(forms.Form):
    #username = forms.CharField(max_length=100)
    #email = forms.EmailField()
    #password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        return user


    #class Meta:
        #model = User
        #fields = ('username', 'email',)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


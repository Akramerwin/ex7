from django import forms
from django.forms import widgets
from webapp.models import Choice, Poll, Answer
from django.core.validators import BaseValidator, ValidationError
from django.utils.deconstruct import deconstructible

class q_form(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class c_form(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

class answer_form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['Choice_a']
        widgets = {'Choice_a': widgets.RadioSelect  }
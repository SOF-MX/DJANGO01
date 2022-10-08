#from attr import field, fields
from django import forms
#from matplotlib.pyplot import cla

from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model= Question
        fields= '__all__'
from django import forms
from .models import Questions, Answers


class Question(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('question', )

        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control'}),	
        }

class Answer(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('answer', )

        widgets = {
            'answer':forms.Textarea(attrs={'class': 'form-control'}),	
        }


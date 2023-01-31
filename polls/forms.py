from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Question

class NameForm(forms.Form):
    name = forms.IntegerField(label='Your name', min_value=0)
    subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)


# class QuestionCreateForm(forms.Form):
#     # question_text = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#
#     question_text = forms.CharField(label="Text: ", max_length=100, required=True)
#     pub_date = forms.DateTimeField(label="Date: ", initial=datetime.now())
#
#     def clean(self):
#         cleaned_data = super().clean()
#         return cleaned_data
#
#     def clean_question_text(self):
#         data = self.cleaned_data["question_text"]
#         if data == "123":
#             raise ValidationError("question_text cant be equal to 123")
#         return data

class QuestionCreateForm(forms.ModelForm):
    # question_text = forms.CharField(label="Text: ", max_length=100, required=True)

    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]

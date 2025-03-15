from django import forms


class QuestionForm(forms.Form):
    content = forms.CharField(max_length=200, required=True)

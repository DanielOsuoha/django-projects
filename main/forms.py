from django import forms
class CreateList(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    # check = forms.BooleanField(required=False)
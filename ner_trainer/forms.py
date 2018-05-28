from django import forms


class ModelTestForm(forms.Form):
    text = forms.CharField()

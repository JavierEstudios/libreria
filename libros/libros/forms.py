from django import forms

class Formulario(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    rating = forms.IntegerField()
    sinopsys = forms.CharField()
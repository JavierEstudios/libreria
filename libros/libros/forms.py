from django import forms

class Formulario(forms.Form):
    title = forms.CharField(label='título', max_length=100)
    author = forms.CharField(label='autor', max_length=50)
    rating = forms.IntegerField(label='valoración')
    sinopsys = forms.CharField(label='sinopsis')
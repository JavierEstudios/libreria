from django import forms
from .models import Libro

class Formulario(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ["title","author","rating","sinopsys"]
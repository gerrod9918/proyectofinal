from django import forms
from .models import Materia

class FormPub(forms.ModelForm):

    class Meta:
        model = Materia
        fields = ('nombre', 'credito', 'profesor',)

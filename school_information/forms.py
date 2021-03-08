from django import forms
from school_information.models import NoticBoard



class Notic_Board_Form(forms.ModelForm):
    class Meta:
        model = NoticBoard
        fields = ("__all__")
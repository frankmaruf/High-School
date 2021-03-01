from django import forms
from teachers.models import Teachers


class DateInput(forms.DateInput):
    input_type = 'date'


class TeachersForm(forms.ModelForm):
    birthDate = forms.DateField(widget=DateInput)

    def clean(self):
        all_clean_data = super().clean()
    class Meta:
        model = Teachers
        exclude = ['Join_Date','Update_Date',]
        fields = '__all__'
from django import forms
from school_information.models import Class,Department,YearOfStudent,Candidate,Subject
from students.models import Students
from django.core import validators
from django.core.exceptions import ValidationError,NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _


def check_for_number(value):
    if value[0] != "0" and value[1] != "1":
        raise forms.ValidationError("Number Must Start With 01")

def check_for_de_and_sub_roll(department,subject,sdclass,year,roll):
    department = Students.objects.filter(department_id=department)
    subject = Students.objects.filter(subject_id=subject)
    sdclass = Students.objects.filter(Class_id=sdclass)
    year = Students.objects.filter(year_id=year)
    roll = Students.objects.filter(roll=roll)
    if year.count() and sdclass.count() and department.count() and subject.count() and roll.count():
        raise ValidationError("Roll alredy exist")


def check_for_class_and_roll(sdclass,roll):
    roll = Students.objects.filter(roll=roll)
    sdclass = Students.objects.filter(Class_id=sdclass)
    if roll.count() and sdclass.count():
        raise ValidationError("Roll already exist in same class")

def check_for_birthcertificate(value):
    num_of_birth = Students.objects.filter(birth_certificate=value)
    if num_of_birth.count():
        raise ValidationError(_(
            "%(value) is already exist"
        ), params={"value":value,})



class DateInput(forms.DateInput):
    input_type = 'date'


class StudentsForm(forms.ModelForm):
    roll = forms.CharField(widget=forms.TextInput(attrs={'type':"number"}),max_length=20,)
    contract = forms.CharField(widget=forms.TextInput(attrs={'type':"number"}),max_length=11,min_length=11,validators=[check_for_number,])
    birthDate = forms.DateField(widget=DateInput,)
    birth_certificate = forms.CharField(widget=forms.TextInput(attrs={'type':"number"}),max_length=17,min_length=17)
    father_NID = forms.CharField(widget=forms.TextInput(attrs={'type':"number"}),max_length=14,min_length=14)
    mother_NID = forms.CharField(widget=forms.TextInput(attrs={'type':"number"}),max_length=14,min_length=14)



    def __init__(self, *args, **kwargs):
        super(StudentsForm, self).__init__(*args, **kwargs)


    def clean(self):
        all_clean_data = super().clean()
        department = all_clean_data['department']
        subject = all_clean_data['subject']
        roll = all_clean_data['roll']
        Class = all_clean_data['Class']
        year = all_clean_data['year']

        if department and subject and Class and year and roll:
            if check_for_de_and_sub_roll(department,subject,Class,year,roll):
                raise ValidationError("Roll are already exist")
        #
        if Class and roll:
            if check_for_class_and_roll(Class,roll):
                raise ValidationError("Roll already exist")
    class Meta:
        model = Students
        exclude = ['Join_Date','Update_Date','candidate_of']
        fields = "__all__"


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['Join_Date','Update_Date','candidate_of','birth_certificate','birthDate','gender']
        fields = "__all__"
from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from school_manager.models import UserProfileInfo



class DateInput(forms.DateInput):
    input_type = 'date'



class EditeProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email:",widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"email"}))
    first_name = forms.CharField(label="First Name:",max_length=100,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"First Name"}))
    last_name = forms.CharField(label="Last Name:",max_length=100,widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Last Name"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs["placeholder"] = 'username'
        self.fields['username'].label = 'Enter Your Username'
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].help_text = '<span class = "form-text text-muted"><small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 4 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></small></span>'



        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirmation password'
        self.fields['password2'].help_text = '<span class = "form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



class CustomUserProfileInfoCreationForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DateInput)
    class Meta:
        model = UserProfileInfo
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(CustomUserProfileInfoCreationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-control'

        self.fields['profile_pic'].widget.attrs['class'] = 'form-control'

        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['placeholder'] = 'Write Your Bio'
        self.fields['bio'].help_text = '<span class = "form-text text-muted"><small>Hello World</small></span>'


        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'date-month-year'
        self.fields['birth_date'].help_text = '<span class = "form-text text-muted"><small>date-month-year</small></span>'

        self.fields['birth_Certificate'].widget.attrs['class'] = 'form-control'
        self.fields['birth_Certificate'].widget.attrs['placeholder'] = 'Birth Certificate'

        self.fields['NID'].widget.attrs['class'] = 'form-control'
        self.fields['NID'].widget.attrs['placeholder'] = 'NID Number'

        self.fields['contract_number'].widget.attrs['class'] = 'form-control'
        self.fields['contract_number'].widget.attrs['placeholder'] = 'Contract Number'

        self.fields['Social_ID'].widget.attrs['class'] = 'form-control'
        self.fields['Social_ID'].widget.attrs['placeholder'] = 'Social Account'

        self.fields['Present_Address'].widget.attrs['class'] = 'form-control'
        self.fields['Present_Address'].widget.attrs['placeholder'] = 'Present Address'

        self.fields['Permanent_Address'].widget.attrs['class'] = 'form-control'
        self.fields['Permanent_Address'].widget.attrs['placeholder'] = 'Permanent Address'




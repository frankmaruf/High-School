from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfileInfo(models.Model):
    Gender_Choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # Additional
    gender = models.CharField(choices=Gender_Choices, blank=False, max_length=6)
    profile_pic = models.ImageField(upload_to='HeadMaster_Manager', blank=True)
    bio = models.TextField(max_length=400, blank=True)
    birth_date = models.DateField(blank=False)
    birth_Certificate = models.CharField(max_length=17)
    NID = models.CharField(max_length=14, primary_key=True,blank=False)
    contract_number = models.CharField(max_length=11,blank=False)
    Social_ID = models.URLField(blank=True)
    Present_Address = models.CharField(blank=False, max_length=200)
    Permanent_Address = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return "Name: "+self.user.username


    class Meta:
        verbose_name_plural = "User Info"


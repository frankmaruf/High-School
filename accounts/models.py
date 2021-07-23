from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Common_fields(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="Student",blank=True,null=True)
    contract_number = models.BigIntegerField(blank=False)
    email = models.CharField(max_length=200, unique=True,blank=False)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,unique=True)
    is_headmaster = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=True)
    is_school_staff = models.BooleanField(default=True)
    is_student  = models.BooleanField(default=True)
    present_Address = models.CharField(max_length=250,blank=False)
    permanent_Address = models.CharField(max_length=250,blank=False)
    birth_certificate = models.BigIntegerField(blank=False,unique=True)
    birthDate = models.DateField(blank=False,null=True)
    Join_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract=True

class User(AbstractUser,Common_fields):
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.email

class Headmaster(User):
    def __str__(self):
        return self.email
class Teacher(User):
    is_staff = None
    is_admin = None
    is_superuser = None
    is_school_staff = None
    is_student = None

    def __str__(self):
        return self.email

class School_Staff(User):
    is_staff = None
    is_admin = None
    is_superuser = None
    is_teacher = None
    is_student = None
    def __str__(self):
        return self.email

class School_Staff(User):
    is_staff = None
    is_admin = None
    is_superuser = None
    is_teacher = None
    is_school_staff = None
    def __str__(self):
        return self.email

from django.db import models
from school_information.models import Subject,Class,Department
# Create your models here.


class Teachers(models.Model):
    gender_choice = (
        ('Male','Male'),
        ('Female','Female')
    )
    name = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to = "Teachers",blank = True,null = True)
    gender = models.CharField(choices=gender_choice,max_length=10,)
    NID = models.BigIntegerField(blank=False,unique=True)
    birth_certificate = models.BigIntegerField(blank=False,unique=True)
    birthDate = models.DateField(blank=False,null=True)
    contract_number = models.CharField(max_length=11,blank=False)
    email = models.EmailField(blank=True,max_length=100)
    father_name = models.CharField(max_length=150,blank=False)
    mother_name = models.CharField(max_length=150,blank=False)
    present_Address = models.CharField(max_length=250,blank=False)
    permanent_Address = models.CharField(max_length=250,blank=False)
    teaching_deaprtment = models.ManyToManyField(Department,blank=True)
    teaching_subjects = models.CharField(max_length=200,blank=True)
    teaching_class = models.ManyToManyField(Class,blank=False)
    Join_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Teachers List"



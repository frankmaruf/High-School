from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone
from school_information.models import YearOfStudent,Department,Class,Examiner,Subject
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver , Signal
from django.db.models.signals import pre_init , pre_save,post_save
# Create your models here.

class Students(models.Model):

    Gender_Choices = (
        ('Male','Male'),
        ('Female','Female')
    )
    name = models.CharField(max_length=150,blank=False)
    profile_pic = models.ImageField(upload_to="Student",blank=True,null=True)
    Class = models.ForeignKey(Class,null=True,on_delete=models.SET_NULL)
    gender = models.CharField(blank=False,choices=Gender_Choices,max_length=20)
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL,blank=True)
    subject = models.ForeignKey(Subject,null=True,on_delete=models.SET_NULL,blank=True)
    roll = models.CharField(blank=False,max_length=20)
    year = models.ForeignKey(YearOfStudent,null=True,on_delete=models.SET_NULL)
    examiner =models.ForeignKey(Examiner,null=True,on_delete=models.SET_NULL,blank=True)
    birth_certificate = models.CharField(blank=False,unique=True,max_length=17)
    birthDate = models.DateField(blank=False,null=True)
    email = models.EmailField(blank=True)
    father_name = models.CharField(max_length=150,blank=False)
    mother_name = models.CharField(max_length=150,blank=False)
    father_NID = models.CharField(blank=False,max_length=14)
    mother_NID = models.CharField(blank=False,max_length=14)
    contract = models.CharField(blank=False,max_length=11)
    present_Address = models.CharField(max_length=250,blank=False)
    permanent_Address = models.CharField(max_length=250,blank=False)
    Join_Date = models.DateTimeField(auto_now=True)
    Update_Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('students:student_detail', args=[str(self.birth_certificate)])

    class Meta:
        verbose_name_plural = "Student List"

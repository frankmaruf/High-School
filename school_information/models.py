from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class YearOfStudent(models.Model):
    year = models.PositiveSmallIntegerField(blank=False)
    slug = models.SlugField(max_length=100, unique=True,blank=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.year)
        super(YearOfStudent,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.year)

class Department(models.Model):
    department_name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.department_name)
        super(Department,self).save(*args,**kwargs)

    def __str__(self):
        return self.department_name

class Examiner(models.Model):
    # Examiner_Choices = (
    #     ('P.S.C', 'Primary School Certificate'),
    #     ('J.S.C','Junior School Certificate'),
    #     ('S.S.C','Secondary School Certificate'),
    #
    # )
    examiner_title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True,blank=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.examiner_title)
        super(Examiner,self).save(*args,**kwargs)

    def __str__(self):
        return self.examiner_title


class Class(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True,blank=True)


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Class,self).save(*args,**kwargs)


    def __str__(self):
        return self.name

class Subject(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Subject,self).save(*args,**kwargs)

    def __str__(self):
        return self.name


class NoticBoard(models.Model):
    title = models.CharField(max_length=250, blank=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    details = models.TextField(blank=False)
    pdf = models.FileField(blank=True, upload_to = "Notic_Board/pdf")
    image = models.ImageField(upload_to = 'Notic_Board', blank = True)
    added_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=False,blank=True)

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(NoticBoard,self).save(*args,**kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('school_information:notice_board_details',
        args = [self.slug,
        self.added_date.day,
        self.added_date.month,
        self.added_date.year])



from django.contrib import admin
from students import models
# Register your models here.

# class StudentsAdmin(admin.ModelAdmin):
#     list_display = ('Sd_Name','Sd_Roll',)
#     search_fields = ['Sd_Name','Sd_Roll']
#     ordering = ['-Sd_Roll']
#     fields = ('Sd_Name','Sd_Class','Sd_Profile_Pic','Sd_Year','Sd_Birth_Certificate','Sd_Department',
#                     'Sd_Roll','Sd_BirthDate','Sd_Email',
#                     'Sd_Father_Name','Sd_Mother_Name',
#                     'Sd_Father_NID','Sd_Mother_NID',
#                     'Sd_Contract','Sd_Present_Address',
#                     'Sd_Permanent_Address')
#
#
admin.site.register(models.Students)
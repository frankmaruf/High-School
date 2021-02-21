from django.contrib import admin
from school_information.models import YearOfStudent,Department,Class,Examiner,Subject
# Register your models here.


admin.site.register(YearOfStudent)
admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Examiner)
admin.site.register(Subject)
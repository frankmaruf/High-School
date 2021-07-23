from django.contrib import admin
from school_information.models import YearOfStudent,Department,Class,Candidate,Subject,NoticBoard
# Register your models here.


admin.site.register(YearOfStudent)
admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Candidate)
admin.site.register(Subject)
admin.site.register(NoticBoard)
from django.urls import path,include
from students import views
app_name = 'students'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('student/<certificate>/',views.student_detail, name='student_detail'),
    path('add_students/', views.StudentsAdd, name='add_students'),
    path('edit_student/<certificate>/', views.EditStudent, name='edit_student'),
]
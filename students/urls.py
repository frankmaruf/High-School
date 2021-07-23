from django.urls import path,include
from students import views
app_name = 'students'

urlpatterns = [
    path('',views.index, name = 'index'),
    #path('student/<certificate>/',views.student_detail, name='student_detail'),
    path('student/<certificate>/',views.Student_detail.as_view(), name='student_detail'),
    path('add_students/', views.StudentsAdd, name='add_students'),
    path('edit_student/<certificate>/', views.EditStudent, name='edit_student'),
    path('delete_student/<certificate>/', views.DeleteStudent, name='delete_student'),
]
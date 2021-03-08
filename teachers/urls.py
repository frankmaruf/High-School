from django.urls import path,include
from teachers import views
app_name = 'teachers'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:certificate>/',views.teachers_profile ,name = 'profile'),
    path('add_teachers/',views.TeachersAdd,name = 'add_teachers'),
    path('<int:certificate>/edite_teacher/',views.EditTeacher,name ='edite_teachers'),
    path('<int:certificate>/delete_teacher/',views.DeleteTeacher,name ='delete_teachers'),

]
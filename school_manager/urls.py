from django.urls import path,include
from school_manager import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'school_manager'

urlpatterns = [
    path('',views.manager_list,name = 'index'),
    path('edit_profile/',views.edit_prifile,name = 'edit_profile'),
    path('change_password/',views.change_password,name = 'change_password'),
    path('<username>/',views.manager_profile,name='profile'),
]
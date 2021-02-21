from django.urls import path,include
from school_information import views
app_name = 'school_information'

urlpatterns = [
    path('',views.index, name = 'index')

]
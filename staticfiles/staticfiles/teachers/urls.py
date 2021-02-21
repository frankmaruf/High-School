from django.urls import path,include
from teachers import views
app_name = 'teachers'

urlpatterns = [
    path('',views.index, name = 'index')

]
from django.urls import path,include
from headmaster import views
app_name = 'headmaster'

urlpatterns = [
    path('',views.index, name = 'index')

]
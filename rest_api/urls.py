from django.urls import include, path
from rest_framework import routers
from rest_api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.apiOverview,name='api-overview'),
    path('students-list/',views.students_list,name = 'students-list'),
    path('students-detail/<str:birth_certificate>/',views.students_detail,name = 'students-detail'),
    path('students-create/',views.students_create,name = 'students-create'),
    path('students-update/<str:birth_certificate>/',views.students_update,name = 'students-update'),
    path('students-delete/<str:birth_certificate>/',views.students_delete,name = 'students-delete'),
]
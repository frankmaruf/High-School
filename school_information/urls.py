from django.urls import path,include
from school_information import views
app_name = 'school_information'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('notice_board',views.notice_board,name = "notice_board"),
    path('<slug>/<int:day>/<int:month>/<int:year>/',views.notice_details,name = 'notice_board_details'),
    path('<slug>/<int:day>/<int:month>/<int:year>/edite/',views.notice_board_edite,name = "notice_board_edite")

]
from django.urls import path
from schoolapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'schoolapp'

urlpatterns = [
    path('home/', views.Index, name ='index'),
    path('about/', views.About, name = 'about'),
    # path('studentdetail/<int:stdid>/', views.StudentDetail, name ='detail1'),
    # path('teacherdetail/<int:tid>/', views.TeacherDetail, name ='detail2'),
    path('studentslist/', views.StudentListView,name='studentlist'),
    path('teacherslist/', views.TeacherListView,name='teacherlist'),
    
]


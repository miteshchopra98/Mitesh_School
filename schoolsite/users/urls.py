from django.urls import path, include
from users import views as userviews
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'


urlpatterns = [
    path('studentreg/', userviews.Student_Register, name='studentreg'),
    path('teacherreg/', userviews.Teacher_Register, name='teacherreg'),
    path('adminreg/', userviews.Admin_Register, name='adminreg'),
    path('login/',userviews.Login_view, name = 'login'),
    path('logout/', userviews.Logout_view, name='logout'),
    path('studentprofile/<int:pid>/', userviews.StudentProfileView, name = 'studentprofile'),
    path('teacherprofile/<int:pid>/', userviews.TeacherProfileView, name = 'teacherprofile'),
    path('adminprofile/<int:pid>/', userviews.AdminProfileView, name='adminprofile'),
    path('studentcomp/<int:pid>/', userviews.CompetitionApply, name = 'competitionapply'),
    path('compform/', userviews.CompetitionForm, name = 'competitionform'),
    path('product/', userviews.Products, name='product'),
    path('order/<int:pid>/', userviews.Orders, name='order'),
    path('addproduct/', userviews.CreateProducts, name='addproduct'),
    path('updateproduct/', userviews.UpdateProducts, name='updateproduct'),
    path('delproduct/', userviews.DeleteProducts, name='delproduct'),
    
    
]


from django.contrib import admin

from users.models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'role')
admin.site.register(User, UserAdmin)







class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id')

admin.site.register(StudentProfile, StudentProfileAdmin)





class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'teacher_id')

admin.site.register(TeacherProfile, TeacherProfileAdmin)






class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ('st_mk','English','Hindi','Marathi','Maths','Science','Total')

admin.site.register(StudentMarks, StudentMarksAdmin)








class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('comp', 'sport')

admin.site.register(StudentCompetition, CompetitionAdmin)






class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'prod_id','prod_price')

admin.site.register(Product,ProductAdmin)








class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_by', 'prod_ordered', 'order_count')

admin.site.register(Order,OrderAdmin)



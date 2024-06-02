from multiprocessing import context
from django.shortcuts import *
from django.http import *
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Student, StudentCompetition,Teacher
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
User = get_user_model()


# Create your views here.


def Index(request):
    comp1 = StudentCompetition.objects.filter(comp__isnull=True)
    
    student = Student.student.all()
    context ={
        'comp1':comp1,
        'student':student
        }

    return render(request, 'schoolapp/index.html', context)

def StudentListView(request):
    studentlist = Student.student.all()
    
    context ={
        'studentlist': studentlist
        }

    return render(request, 'schoolapp/students.html', context)

def TeacherListView(request):
    teacherlist = Teacher.teacher.all()
    
    context ={
        'teacherlist': teacherlist
        }

    return render(request, 'schoolapp/teachers.html', context)

def About(request):

    context ={
        }

    return render(request, 'schoolapp/aboutus.html', context)

# def StudentDetail(request, stdid):
#     student = Student.student.get(id=stdid)
#     context={
#         'student': student
#         }
#     return render(request, 'schoolapp/student_details.html', context)

# def TeacherDetail(request, tid):
#     teacher = Teacher.teacher.get(id=tid)
#     context={
#         'teacher': teacher
#         }
#     return render(request, 'schoolapp/teacher_details.html', context)